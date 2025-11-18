import socket
import errno

def tcp_connect_state(ip: str, port: int, timeout: float) -> str:
    """
    Return 'open', 'closed', or 'filtered' using TCP connect_ex:
      - 0 => open
      - ECONNREFUSED => closed
      - timeout/unreachable => filtered
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        err = s.connect_ex((ip, port))
        if err == 0:
            return "open"
        if err == errno.ECONNREFUSED:  # 111 Linux, 10061 Windows
            return "closed"
        if err in (
            errno.ETIMEDOUT,
            getattr(errno, "EHOSTUNREACH", 113),
            getattr(errno, "ENETUNREACH", 101),
        ):
            return "filtered"
        return "closed"
    except socket.timeout:
        return "filtered"
    except Exception:
        return "closed"
    finally:
        try:
            s.close()
        except Exception:
            pass
