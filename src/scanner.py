import socket
import logging
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO)

def scan_port(host: str, port: int, timeout: float = 1.0) -> Dict[str, str]:
    """Scan a single port on the host."""
    result = {"port": str(port), "status": "closed"}
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        conn_result = sock.connect_ex((host, port))
        if conn_result == 0:
            result["status"] = "open"
        sock.close()
    except socket.timeout:
        result["status"] = "filtered"
    except Exception as e:
        logging.error(f"Error scanning port {port}: {e}")
    return result

def scan_ports(host: str, ports: List[int], timeout: float = 1.0) -> List[Dict[str, str]]:
    """Scan multiple ports on the host using threading for speed."""
    results = []
    with ThreadPoolExecutor(max_workers=100) as executor:  # Adjust max_workers if needed (e.g., for very large ranges)
        future_to_port = {executor.submit(scan_port, host, port, timeout): port for port in ports}
        for future in as_completed(future_to_port):
            results.append(future.result())
    # Sort results by port for consistent output
    results.sort(key=lambda x: int(x["port"]))
    return results