# Built-in networking library. It lets us connect to IPs and ports.
import socket
# Makes our script usable from the command line with flags like --host and --ports.
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Simple TCP port scanner")
    parser.add_argument("--host", required=True,
                        help="Target IP address or hostname")
    parser.add_argument("--ports", required=True,
                        help="Port range (e.g., 20-80)")
    return parser.parse_args()