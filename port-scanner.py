import socket
import concurrent.futures
import argparse
from datetime import datetime

def scan_port(target_ip, port):
    """Scan a single port on the target IP."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1-second timeout to avoid hanging
        result = sock.connect_ex((target_ip, port))
        sock.close()
        return port if result == 0 else None
    except Exception:
        return None

def scan_ports(target_ip, start_port, end_port, threads=100):
    """Scan a range of ports using multithreading."""
    open_ports = []
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...")
    start_time = datetime.now()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_port = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1)}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            try:
                if future.result():
                    open_ports.append(port)
            except Exception:
                pass
    
    end_time = datetime.now()
    print(f"Scan completed in {end_time - start_time}")
    return open_ports

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Network Port Scanner")
    parser.add_argument("target_ip", help="Target IP address to scan (e.g., 127.0.0.1)")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads (default: 100)")
    args = parser.parse_args()
    
    open_ports = scan_ports(args.target_ip, args.start, args.end, args.threads)
    if open_ports:
        print("Open ports:")
        for port in sorted(open_ports):
            print(f"Port {port} is open")
    else:
        print("No open ports found in the range.")