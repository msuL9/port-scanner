port-scanner
Overview
This is a modular Python-based TCP port scanner that checks if ports on a target host are open, closed, or filtered. It uses Python's socket library for core functionality and supports fast scanning of large port ranges via threading. Designed for educational and testing purposes only—do not use on unauthorized systems.
Features

Scans individual or ranges of TCP ports (e.g., 1-1024).
Detects port statuses: "open", "closed", or "filtered" (timeout).
Parallel scanning with threading for speed (e.g., 1000+ ports in seconds).
CLI interface with argparse for easy usage.
Modular design: Core logic in src/scanner.py, entry point in main.py.
100% test coverage using pytest and coverage, with mocked sockets for isolation.
Error handling for invalid inputs and scanning exceptions.
Sorted output for consistent results.

Requirements

Python 3.13.6 (or compatible).
Dependencies (listed in requirements.txt):
textpytest==8.3.2
coverage==7.6.1
No runtime dependencies beyond Python stdlib (socket, logging, concurrent.futures, argparse).

Setup

Clone the repository:
textgit clone <your-repo-url>
cd port_scanner_project

Create and activate virtual environment:
textpython -m venv venv
venv\Scripts\activate

Install dependencies:
textpip install -r requirements.txt


Usage
Run the scanner via CLI from the project root:
textpython main.py <host> --ports <range> --timeout <seconds>

<host>: Target IP or hostname (e.g., localhost, scanme.nmap.org).
--ports: Port range (default: 20-1024, format: start-end like 1-1000).
--timeout: Connection timeout in seconds (default: 1.0).

Examples:

Scan localhost ports 80-85 quickly:
textpython main.py localhost --ports 80-85 --timeout 0.5
Output:
textPort 80: open
Port 81: closed
...

Scan remote host ports 1-1024:
textpython main.py scanme.nmap.org --ports 1-1024

Invalid range:
textpython main.py localhost --ports invalid
Output: "Invalid port range. Use format like 1-1000."

Supports fast scanning of large ranges via threading (adjust max_workers in src/scanner.py if needed).
Testing

Run tests with coverage:
textcoverage run -m pytest

Generate report:
textcoverage report -m
Expected: 100% coverage for src/scanner.py and main.py.


Tests cover: open/closed/filtered ports, errors, multi-port scanning.
Uses pytest fixtures and monkeypatching for socket isolation.

Project Structure
textport_scanner_project/
├── main.py              # CLI entry point
├── requirements.txt     # Dependencies
├── src/
│   ├── __init__.py
│   └── scanner.py       # Core scanning logic
├── tests/
│   ├── __init__.py
│   └── test_scanner.py  # Unit tests
└── venv/                # Virtual environment (gitignore this)
Limitations

TCP connect scan only (no SYN/UDP).
Use ethically; test on authorized hosts like scanme.nmap.org.
Threading speed depends on system/network; may hit OS socket limits for very large ranges.

Contributing
Fork the repo, create a branch, add changes, test for 100% coverage, and submit a PR.
License
MIT License. See LICENSE file for details. (Create LICENSE with standard MIT text if needed.)
