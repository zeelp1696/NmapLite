#!/usr/bin/env python3
"""
NmapLite (modular) — TCP connect scanner with optional banner grabbing
"""

import argparse
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict

from scanner_modules.utils import parse_ports, resolve_target, print_results, save_results
from scanner_modules.tcp_scanner import tcp_connect_scan
from scanner_modules.service_detect import service_name_for_port, grab_banner


def scan_ports(ip: str, ports: List[int], threads: int, timeout: float, detect_service: bool) -> List[Dict]:
    results: List[Dict] = []

    def task(p: int) -> Dict:
        is_open = tcp_connect_scan(ip, p, timeout)
        row = {"port": p, "state": "open" if is_open else "closed", "service": None, "banner": None}
        if is_open:
            row["service"] = service_name_for_port(p)
            if detect_service:
                row["banner"] = grab_banner(ip, p)
        return row

    with ThreadPoolExecutor(max_workers=threads) as exe:
        futmap = {exe.submit(task, p): p for p in ports}
        for fut in as_completed(futmap):
            try:
                res = fut.result()
                if res["state"] == "open":
                    results.append(res)
            except Exception:
                pass

    return sorted(results, key=lambda r: r["port"])


def main():
    parser = argparse.ArgumentParser(description="NmapLite (modular) — TCP connect port scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port spec, e.g. 22,80,443 or 1-1000 or mixed")
    parser.add_argument("--threads", type=int, default=50, help="Thread count (default: 50)")
    parser.add_argument("--timeout", type=float, default=1.0, help="TCP connect timeout seconds (default: 1.0)")
    parser.add_argument("-sV", "--service-detect", action="store_true", help="Attempt basic banner grabbing")
    parser.add_argument("-o", "--output", help="Output filename")
    parser.add_argument("--format", choices=["json", "csv", "txt"], default="json", help="Output format (default: json)")
    args = parser.parse_args()

    resolved = resolve_target(args.target)
    if not resolved:
        print(f"Error: could not resolve '{args.target}'")
        sys.exit(1)

    try:
        ports = parse_ports(args.ports)
    except ValueError as e:
        print(f"Error parsing ports: {e}")
        sys.exit(1)

    print("NmapLite (modular) — TCP Connect Scanner")
    print("---------------------------------------")
    print(f"Target:  {args.target} ({resolved})")
    print(f"Ports:   {args.ports}")
    print(f"Threads: {args.threads}  Timeout: {args.timeout}s  ServiceDetect: {args.service_detect}")

    started = datetime.now()
    open_results = scan_ports(
        ip=resolved, ports=ports, threads=args.threads, timeout=args.timeout, detect_service=args.service_detect
    )
    finished = datetime.now()

    print_results(open_results, started, finished)

    if args.output:
        try:
            save_results(open_results, args.output, args.format, started, finished)
            print(f"Saved results to: {args.output}")
        except Exception as e:
            print(f"Failed to save results: {e}")


if __name__ == "__main__":
    main()
