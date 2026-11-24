"""One-line entry for Till Firmware Do Us Part: writes the line the judge reads to /output/entry.txt."""

import os

LINE = (
    "We promised till firmware do us part — then the update bricked me and you married a newer model with better battery life."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
