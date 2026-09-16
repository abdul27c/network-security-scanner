import argparse
import socket
import time


def scan_port(target, port, timeout=0.5):
    """Check whether a TCP port is accepting connections."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((target, port))
        return result == 0
    except socket.error:
        return False
    finally:
        sock.close()


def get_service_name(port):
    """Return the standard TCP service name for a port."""
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"


def scan_ports(target, start_port, end_port):
    """Scan a range of TCP ports."""
    open_ports = []

    print(f"\nScanning {target}...")
    print("-" * 50)

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            service = get_service_name(port)
            print(f"Port {port}: OPEN ({service})")
            open_ports.append((port, service))

    return open_ports


def main():
    parser = argparse.ArgumentParser(
        description="Simple TCP Network Security Scanner"
    )

    parser.add_argument(
        "target",
        help="IP address or hostname to scan"
    )

    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="Starting port (default: 1)"
    )

    parser.add_argument(
        "--end",
        type=int,
        default=1024,
        help="Ending port (default: 1024)"
    )

    args = parser.parse_args()

    if not 1 <= args.start <= 65535:
        parser.error("Starting port must be between 1 and 65535")

    if not 1 <= args.end <= 65535:
        parser.error("Ending port must be between 1 and 65535")

    if args.start > args.end:
        parser.error("Starting port must be less than or equal to ending port")

    print("=" * 50)
    print("Network Security Scanner")
    print("=" * 50)
    print(f"Target: {args.target}")
    print(f"Port range: {args.start}-{args.end}")

    start_time = time.time()

    try:
        target_ip = socket.gethostbyname(args.target)
        print(f"Resolved IP: {target_ip}")
    except socket.gaierror:
        print(f"Error: Could not resolve '{args.target}'")
        return

    open_ports = scan_ports(
        target_ip,
        args.start,
        args.end
    )

    elapsed_time = time.time() - start_time

    print("\n" + "=" * 50)
    print("Scan Summary")
    print("=" * 50)
    print(f"Target: {args.target}")
    print(f"Ports scanned: {args.start}-{args.end}")
    print(f"Open ports found: {len(open_ports)}")
    print(f"Scan duration: {elapsed_time:.2f} seconds")

    if open_ports:
        print("\nOpen ports:")
        for port, service in open_ports:
            print(f"  - {port}: {service}")
    else:
        print("\nNo open ports found.")

    print("\nScan complete.")


if __name__ == "__main__":
    main()
