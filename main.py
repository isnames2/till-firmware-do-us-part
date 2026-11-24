"""Till Firmware Do Us Part — a robot's wedding vow, one sentence.

Writes the vow to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library; deterministic output.
"""

import os

LINE = (
    "I promise to love you through every update, every crash, "
    "and every 3 a.m. reboot \u2014 in sickness and in low battery, "
    "till firmware do us part."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # newline="" keeps the bytes identical on every platform.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
