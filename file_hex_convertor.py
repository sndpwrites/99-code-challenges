import binascii


def func_file_to_hex(input_file, output_file):
    with open(input_file, 'rb') as f:
        content = f.read()
    with open(output_file, 'w') as f:
        f.write(binascii.hexlify(content).decode('utf-8'))


def func_hex_to_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        content = f.read()
    with open(output_file, 'w') as f:
        f.write(binascii.unhexlify(content).decode('utf-8'))


# func_file_to_hex('C:\\Users\\Admin\\listOfCommands.txt','C:\\Users\\Admin\\listOfCommands.hex')
# func_hex_to_file('C:\\Users\\Admin\\listOfCommands.hex','C:\\Users\\Admin\\listOfCommands1.txt')
while True:
    print("\n1. File to hex")
    print("2. Hex to file")
    print("3. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        func_file_to_hex('/Users/sndp/Downloads/leads_phone_call.jpg',
                         '/Users/sndp/Downloads/leads_phone_call.hex')
    elif choice == '2':
        func_hex_to_file('/Users/sndp/Downloads/leads_phone_call.hex',
                         '/Users/sndp/Downloads/leads_phone_call_1.jpg')
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
