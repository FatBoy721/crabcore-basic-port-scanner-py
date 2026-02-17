import socket

try:
    target = input("Enter target IP or website: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    if start_port < 0 or end_port > 65535 or start_port > end_port:
        print("Invalid port range.")
        exit()

except ValueError:
    print("Please enter valid numbers for ports.")
    exit()

print("\nScanning...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        result = sock.connect_ex((target, port))

        if result == 0:
            print("Port", port, "is OPEN")

    except socket.error:
        print("Connection error on port", port)

    sock.close()

print("\nScan complete.")

#FatBoy721