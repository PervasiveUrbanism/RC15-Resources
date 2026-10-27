"""Send eight LED states to the Arduino using newline-terminated serial messages.

Run:
    python -m pip install pyserial
    python led_serial.py COM3

You can also import encode_states() and send_states() from another Python script,
including a compatible Grasshopper Python environment with pyserial installed.
"""

from __future__ import annotations

import argparse
import time
from typing import Iterable


def encode_states(states: Iterable[int | bool] | str) -> bytes:
    """Return exactly eight ASCII 0/1 characters followed by a newline."""
    if isinstance(states, str):
        bits = states
    else:
        values = list(states)
        if len(values) != 8 or any(
            not isinstance(v, (int, bool)) or v not in (0, 1) for v in values
        ):
            raise ValueError("Provide exactly eight states, each 0/1 or True/False.")
        bits = "".join(str(int(v)) for v in values)

    if len(bits) != 8 or any(bit not in "01" for bit in bits):
        raise ValueError("The command must contain exactly eight 0/1 characters.")
    return (bits + "\n").encode("ascii")


def send_states(port, states: Iterable[int | bool] | str) -> None:
    """Write one LED command to an already open pySerial port."""
    data = encode_states(states)
    written = port.write(data)
    if written != len(data):
        raise IOError("Not all LED command bytes were written.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Demo: move one LED along a row.")
    parser.add_argument("port", help="Arduino serial port, e.g. COM3 or /dev/ttyACM0")
    parser.add_argument("--delay", type=float, default=0.25, help="Seconds per step")
    args = parser.parse_args()

    if args.delay <= 0:
        parser.error("--delay must be greater than zero")

    import serial  # Only required when connecting to hardware

    with serial.Serial(args.port, baudrate=9600, timeout=1, write_timeout=1) as board:
        time.sleep(2)  # Many Arduino boards reset when a serial connection opens.
        for index in range(8):
            states = [int(i == index) for i in range(8)]
            send_states(board, states)
            time.sleep(args.delay)
        send_states(board, [0] * 8)


if __name__ == "__main__":
    main()
