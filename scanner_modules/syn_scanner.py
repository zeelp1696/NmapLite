"""
Optional: SYN scan with Scapy (root/admin needed).
This file is not used by default; keep it for later experiments.
"""
from typing import Literal, Optional

def syn_scan_port(target: str, port: int, timeout: float = 1.0) -> Optional[Literal["open","closed","filtered"]]:
    try:
        from scapy.all import IP, TCP, sr1, conf  # type: ignore
        conf.verb = 0
    except Exception:
        return None

    try:
        resp = sr1(IP(dst=target)/TCP(dport=port, flags="S"), timeout=timeout)
        if resp is None:
            return "filtered"
        if resp.haslayer(TCP):
            flags = resp.getlayer(TCP).flags
            if flags == 0x12:  # SYN+ACK
                _ = sr1(IP(dst=target)/TCP(dport=port, flags="R"), timeout=timeout)
                return "open"
            if flags == 0x14:  # RST+ACK
                return "closed"
        return "filtered"
    except Exception:
        return None
