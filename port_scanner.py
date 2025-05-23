import socket
import threading
import argparse
from queue import Queue
import sys
import time
from datetime import datetime


NUMBER_OF_THREADS = 100 
SOCKET_TIMEOUT = 0.5 
print_lock = threading.Lock()


def port_scan(q, target_ip):
    """
    Takes a port from the queue and tries to connect to it on the target IP.
    """
    while not q.empty():
        port = q.get()
        # Create a new socket for each thread/port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Set a timeout for the connection attempt
            s.settimeout(SOCKET_TIMEOUT)
            # Try to connect (connect_ex returns 0 if successful, error code otherwise)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                with print_lock:
                    print(f"[+] Port {port:<5} is open")

        except (socket.timeout, socket.error) as e:
            print(f"[!] Error on port {port}: {e}")
            pass
        finally:
            s.close()
            q.task_done() # Signal that this task is complete


def main(target_host, port_range_str):
    """
    Sets up threads and a queue to scan the target host and ports.
    """
    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"\n[INFO] Scanning target: {target_host} ({target_ip})")
        print(f"[INFO] Time started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)
    except socket.gaierror:
        print(f"[ERROR] Hostname could not be resolved: {target_host}")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
        sys.exit(1)

    
    ports_to_scan = []
    try:
        if '-' in port_range_str:
            start_port, end_port = map(int, port_range_str.split('-'))
            if 0 < start_port <= end_port <= 65535:
                ports_to_scan = range(start_port, end_port + 1)
            else:
                raise ValueError("Invalid port range.")
        else:
            port = int(port_range_str)
            if 0 < port <= 65535:
                ports_to_scan = [port]
            else:
                raise ValueError("Invalid port number.")
    except ValueError as e:
        print(f"[ERROR] Invalid port specification: {port_range_str}. {e}")
        print("[INFO] Use a single port (e.g., 80) or a range (e.g., 1-1024).")
        sys.exit(1)

    #Setup Queue and Threads
    q = Queue()
    for port in ports_to_scan:
        q.put(port)

    start_time = time.time()

    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=port_scan, args=(q, target_ip), daemon=True)
        t.start()

    #Wait for Queue to be Empty
    q.join()

    end_time = time.time()

    # Print Results
    print("-" * 50)
    print(f"[INFO] Scanning Completed.")
    print(f"[INFO] Time finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[INFO] Duration: {end_time - start_time:.2f} seconds.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simple Python Port Scanner with Threading.",
        epilog="Example: python_port_scanner.py -t example.com -p 1-1000"
    )
    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target host (IP address or hostname) to scan."
    )
    parser.add_argument(
        "-p", "--ports",
        required=True,
        help="Port(s) to scan. Use a single number (e.g., 80) or a range (e.g., 1-1024)."
    )
    args = parser.parse_args()

    main(args.target, args.ports)