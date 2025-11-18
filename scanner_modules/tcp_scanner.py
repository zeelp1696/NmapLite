import socket

def tcp_connect_scan(ip: str, port: int, timeout: float) -> bool:
    """Return True if port is open using TCP connect_ex, False otherwise."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        return s.connect_ex((ip, port)) == 0
    except Exception:
        return False
    finally:
        try:
            s.close()
        except Exception:
            pass
