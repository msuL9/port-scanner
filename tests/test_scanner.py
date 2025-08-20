import pytest
import socket  # Added this import to fix 'name "socket" is not defined' error
from src.scanner import scan_port, scan_ports

@pytest.fixture
def mock_socket(monkeypatch):
    class MockSocket:
        def __init__(self, *args, **kwargs):
            pass
        def settimeout(self, *args):
            pass
        def connect_ex(self, *args):
            return 0  # Simulate open by default
        def close(self):
            pass

    monkeypatch.setattr("socket.socket", MockSocket)

def test_scan_port_open(mock_socket):
    result = scan_port("localhost", 80)
    assert result["status"] == "open"

def test_scan_port_closed(monkeypatch):
    def mock_connect_ex(*args):
        return 1  # Simulate closed
    monkeypatch.setattr("socket.socket.connect_ex", mock_connect_ex)
    result = scan_port("localhost", 80)
    assert result["status"] == "closed"

def test_scan_port_filtered(monkeypatch):
    def mock_connect_ex(*args):
        raise socket.timeout
    monkeypatch.setattr("socket.socket.connect_ex", mock_connect_ex)
    result = scan_port("localhost", 80)
    assert result["status"] == "filtered"

def test_scan_port_error(monkeypatch):
    def mock_connect_ex(*args):
        raise Exception("Test error")
    monkeypatch.setattr("socket.socket.connect_ex", mock_connect_ex)
    result = scan_port("localhost", 80)
    assert result["status"] == "closed"  # Default on error

def test_scan_ports(mock_socket):
    results = scan_ports("localhost", [80, 443])
    assert len(results) == 2
    assert all(r["status"] == "open" for r in results)