import ipaddress

def calculate_cidr_range(cidr):
    try:
        # Create an IPv4 network object
        network = ipaddress.ip_network(cidr, strict=False)

        # Get the network range
        first_ip = network.network_address
        last_ip = network.broadcast_address
        total_ips = network.num_addresses

        # Return the result
        return {
            "CIDR": str(cidr),
            "First IP": str(first_ip),
            "Last IP": str(last_ip),
            "Total IPs": total_ips
        }
    
    except ValueError:
        return "Invalid CIDR block"

# Example usage
cidr = "192.168.1.0/27"
result = calculate_cidr_range(cidr)

# Display the result
for key, value in result.items():
    print(f"{key}: {value}")
