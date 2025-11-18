import csv
import ipaddress
import json
import socket
from datetime import datetime
from typing import List, Dict, Optional

def parse_ports(spec: str) -> List[int]:
    ports = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            start = int(a)
            end = int(b)
            if start > end or start < 0 or end > 65535:
                raise ValueError(f"Invalid range: {part}")
            ports.update(range(start, end + 1))
        else:
            p = int(part)
            if p < 0 or p > 65535:
                raise ValueError(f"Invalid port: {p}")
            ports.add(p)
    if not ports:
        raise ValueError("No valid ports parsed")
    return sorted(ports)

def resolve_target(target: str) -> Optional[str]:
    try:
        ipaddress.ip_address(target)
        return target
    except ValueError:
        pass
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return None

def print_results(open_results: List[Dict], started: datetime, finished: datetime) -> None:
    duration = (finished - started).total_seconds()
    if not open_results:
        print("\nNo open TCP ports found.")
        print(f"Completed in {duration:.2f} seconds.")
        return
    print("\nPORT       STATE   SERVICE             BANNER")
    print("-" * 72)
    for r in open_results:
        port_str = f"{r['port']}/tcp"
        state = r["state"]
        svc = r["service"] or "unknown"
        banner = (r["banner"][:44] + "...") if r["banner"] and len(r["banner"]) > 47 else (r["banner"] or "")
        print(f"{port_str:<10} {state:<6}  {svc:<18} {banner}")
    print(f"\nFound {len(open_results)} open ports")
    print(f"Completed in {duration:.2f} seconds")

def save_results(open_results: List[Dict], filename: str, fmt: str,
                 started: datetime, finished: datetime) -> None:
    meta = {
        "start_time": started.isoformat(),
        "end_time": finished.isoformat(),
        "duration_seconds": (finished - started).total_seconds()
    }
    if fmt == "json":
        out = {"scan_info": meta, "results": open_results}
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
    elif fmt == "csv":
        with open(filename, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["port", "state", "service", "banner"])
            w.writeheader()
            w.writerows(open_results)
    elif fmt == "txt":
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Scan Results\n")
            f.write(f"Started:  {meta['start_time']}\n")
            f.write(f"Finished: {meta['end_time']}\n")
            f.write(f"Duration: {meta['duration_seconds']:.2f}s\n\n")
            for r in open_results:
                f.write(f"Port {r['port']}/tcp: {r['state']}  service={r['service'] or 'unknown'}\n")
                if r["banner"]:
                    f.write(f"  Banner: {r['banner']}\n")
    else:
        raise ValueError("Unknown format")
