import socket
import logging
from typing import List, Dict

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
    """Scan multiple ports on the host."""
    results = []
    for port in ports:
        results.append(scan_port(host, port, timeout))
    return results