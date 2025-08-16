# port-scanner

AA multithreaded Python tool to scan for open ports on a target IP, identifying potential services/vulnerabilities. Built with `socket` and `concurrent.futures`. For educational purposes only.

## Features
- Scans port ranges with customizable threads.
- Validates target IP before scanning.
- CLI arguments for flexibility.

## Installation
1. Clone the repo: 
git clone https://github.com/msuL9/port-scanner.git
cd port-scanner

## Usage
Run via CLI:
python port_scanner.py <target_ip> [--start <port>] [--end <port>] [--threads <num>]</num></port></port>

Example: Scan localhost ports 1-100: python port_scanner.py 127.0.0.1 --start 1 --end 100

## Disclaimer
- Use only on your own networks/devices. Unauthorized scanning is illegal.
- Not for production; educational tool.

## License
MIT License (see LICENSE file).
