# Network Security Scanner

A Python-based TCP network security scanner developed to explore networking and security fundamentals.

## Overview

This project scans a specified IP address or hostname across a user-defined range of TCP ports. It identifies open ports, resolves the target IP address, identifies standard service names, and reports the total scan time.

The project was developed as a hands-on exercise to strengthen understanding of TCP/IP networking, Python socket programming, and basic network security concepts.

## Features

- TCP port scanning
- User-defined target IP address or hostname
- Custom starting and ending ports
- DNS/hostname resolution
- Basic TCP service identification
- Scan duration measurement
- Input validation and error handling
- Command-line interface

## Technologies

- Python 3
- TCP/IP
- Python Socket Library
- Linux/Unix command-line concepts
- Git & GitHub

## Usage

Clone the repository:

```bash
git clone https://github.com/abdul27c/network-security-scanner.git
cd network-security-scanner

Run a scan:

python3 scanner.py 127.0.0.1 --start 1 --end 100

Example:

==================================================
Network Security Scanner
==================================================
Target: 127.0.0.1
Port range: 1-100
Resolved IP: 127.0.0.1

Scanning 127.0.0.1...
--------------------------------------------------

Port 53: OPEN (domain)

==================================================
Scan Summary
==================================================
Target: 127.0.0.1
Ports scanned: 1-100
Open ports found: 1
Scan duration: 0.03 seconds

Scan complete.


Concepts Demonstrated
TCP connection establishment
IP addresses and ports
TCP services
Socket programming
Network reconnaissance fundamentals
Command-line argument handling
Exception handling
Basic security monitoring concepts
Future Improvements

Potential future improvements include:

Multithreaded scanning
More detailed service detection
Outputting results to CSV or JSON
Configurable connection timeouts
Logging scan results
Additional security analysis



Ethical Use

This tool is intended for educational purposes and authorized security testing only. Scan systems and networks only when you have permission to do so.