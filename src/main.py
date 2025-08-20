import argparse
from src.scanner import scan_ports

def main():
    parser = argparse.ArgumentParser(description="Basic Network Port Scanner")
    parser.add_argument("host", help="Target host IP or hostname")
    parser.add_argument("--ports", default="20-1024", help="Port range (e.g., 1-1000)")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout in seconds")
    args = parser.parse_args()

    try:
        start_port, end_port = map(int, args.ports.split("-"))
        ports = list(range(start_port, end_port + 1))
    except ValueError:
        print("Invalid port range. Use format like 1-1000.")
        return

    results = scan_ports(args.host, ports, args.timeout)
    for result in results:
        print(f"Port {result['port']}: {result['status']}")

if __name__ == "__main__":
    main()