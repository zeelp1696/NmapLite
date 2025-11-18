# Make helpers importable from scanner_modules
from .tcp_scanner import tcp_connect_scan
from .service_detect import service_name_for_port, grab_banner
from .utils import parse_ports, resolve_target, print_results, save_results
