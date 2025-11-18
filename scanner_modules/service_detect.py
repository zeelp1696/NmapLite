import socket
from typing import Optional

COMMON_PORT_NAMES = {
    20: "ftp-data", 21: "ftp", 22: "ssh", 23: "telnet", 25: "smtp", 53: "dns",
    67: "dhcp", 68: "dhcp", 69: "tftp", 80: "http", 110: "pop3", 123: "ntp",
    135: "msrpc", 137: "netbios-ns", 138: "netbios-dgm", 139: "netbios-ssn",
    143: "imap", 161: "snmp", 162: "snmptrap", 389: "ldap", 443: "https",
    445: "microsoft-ds", 465: "smtps", 514: "syslog", 587: "submission",
    636: "ldaps", 993: "imaps", 995: "pop3s", 1433: "ms-sql", 1521: "oracle",
    3306: "mysql", 3389: "rdp", 5432: "postgresql", 5900: "vnc", 6379: "redis",
    8080: "http-proxy", 8443: "https-alt", 27017: "mongodb"
}

def service_name_for_port(port: int) -> str:
    try:
        return socket.getservbyport(port)
    except Exception:
        return COMMON_PORT_NAMES.get(port, "unknown")

def grab_banner(ip: str, port: int, timeout: float = 2.0) -> Optional[str]:
    """Minimal banner grabbing for open ports."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((ip, port))
        if port in (80, 8080, 8000, 8008, 8888, 8443):
            s.sendall(b"HEAD / HTTP/1.0\r\nHost: example\r\n\r\n")
        else:
            s.sendall(b"\r\n")
        data = s.recv(512)
        s.close()
        if not data:
            return None
        return data.decode("utf-8", errors="ignore").strip()
    except Exception:
        return None
