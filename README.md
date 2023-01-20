# Network-port-scanner
This is a Python script that uses the pyfiglet, sys, socket, and termcolor libraries to create a simple network port scanner.
This is a Python script that uses the pyfiglet, sys, socket, and termcolor libraries to create a simple network port scanner. It first displays an ASCII art banner using the pyfiglet library and prompts the user to enter the IP address of the target device they want to scan. It then prompts the user to enter the range of ports they want to scan, from a starting port to an ending port.

The script then uses a for loop to iterate through the range of ports specified by the user. For each port, it creates a socket connection and sets a default timeout of 0.5 seconds. If the connection is successful, the script will print that the port is open. If the connection is unsuccessful, the script will move on to the next port in the range.

The script also includes error handling for the cases when the user interrupts the scan or if the host is not responding. Finally, the script will display a message indicating that the scan is complete.

This is a simple script and it only check open ports on target IP, it will not give you any information about the services running on that port.
