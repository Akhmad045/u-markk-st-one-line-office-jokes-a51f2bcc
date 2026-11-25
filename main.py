"""One-Line Office Jokes — make.fun entry.

Writes a single one-line joke about office life to /output/entry.txt.
Plain text, one line, 115 characters.
"""

import os

LINE = (
    "I set my status to 'in a meeting' so I could eat lunch, "
    "and now three people have booked meetings with my sandwich."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
