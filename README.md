# port-scanner

## Overview
This is a modular Python-based TCP port scanner that checks if ports on a target host are open, closed, or filtered. It uses Python's `socket` library for core functionality and supports fast scanning of large port ranges via threading. Designed for educational and testing purposes only—do not use on unauthorized systems.

## Features
- Scans individual or ranges of TCP ports (e.g., 1-1024).
- Detects port statuses: "open", "closed", or "filtered" (timeout).
- Parallel scanning with threading for speed (e.g., 1000+ ports in seconds).
- CLI interface with argparse for easy usage.
- Modular design: Core logic in `src/scanner.py`, entry point in `main.py`.
- 100% test coverage using `pytest` and `coverage`, with mocked sockets for isolation.
- Error handling for invalid inputs and scanning exceptions.
- Sorted output for consistent results.

## Requirements
- Python 3.13.6 (or compatible).
- Dependencies (listed in `requirements.txt`):
  ```
  pytest==8.3.2
  coverage==7.6.1
  ```
  No runtime dependencies beyond Python stdlib (`socket`, `logging`, `concurrent.futures`, `argparse`).

## Setup
1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd port_scanner_project
   ```
2. Create and activate virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the scanner via CLI from the project root:
```
python main.py <host> --ports <range> --timeout <seconds>
```
- `<host>`: Target IP or hostname (e.g., `localhost`, `scanme.nmap.org`).
- `--ports`: Port range (default: `20-1024`, format: `start-end` like `1-1000`).
- `--timeout`: Connection timeout in seconds (default: `1.0`).

Examples:
- Scan localhost ports 80-85 quickly:
  ```
  python main.py localhost --ports 80-85 --timeout 0.5
  ```
  Output:
  ```
  Port 80: open
  Port 81: closed
  ...
  ```
- Scan remote host ports 1-1024:
  ```
  python main.py scanme.nmap.org --ports 1-1024
  ```
- Invalid range:
  ```
  python main.py localhost --ports invalid
  ```
  Output: "Invalid port range. Use format like 1-1000."

Supports fast scanning of large ranges via threading (adjust `max_workers` in `src/scanner.py` if needed).

## Testing
1. Run tests with coverage:
   ```
   coverage run -m pytest
   ```
2. Generate report:
   ```
   coverage report -m
   ```
   Expected: 100% coverage for `src/scanner.py` and `main.py`.
- Tests cover: open/closed/filtered ports, errors, multi-port scanning.
- Uses `pytest` fixtures and monkeypatching for socket isolation.

## License
MIT License. See LICENSE file for details.
