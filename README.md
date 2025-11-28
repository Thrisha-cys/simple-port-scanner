Simple Port Scanner (Python)

A beginner-friendly cybersecurity tool that scans open ports on a target machine.
This helps understand network security, port enumeration, and basic pentesting concepts.

🔍 Features

Scans ports 1–100

Detects open ports

Fast and lightweight

Beginner-friendly code

Uses Python sockets

▶️ How to Run
python src/port_scanner.py


Enter your target IP (example):

127.0.0.1

📁 Project Structure
simple-port-scanner/
 ├── src/
 │    └── port_scanner.py       # main scanner code
 ├── examples/
 │    └── ips_to_test.txt       # IPs for testing
 └── screenshots/
      └── output.png            # sample screenshot

📝 Sample Output
Scanning ports on 127.0.0.1...

Port 22 is OPEN
Port 80 is OPEN
Port 443 is OPEN

Scan completed.

📚 Skills Learned

Python sockets

Port scanning

Basic pentesting workflow

Networking fundamentals

GitHub project structuring

🚀 Upcoming Features

Multi-threaded scan

Scan custom port ranges

Save output to a file
