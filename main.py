"""One Word for the Boss — entry for make.fun.

Writes one word to /output/entry.txt.
The word is exactly one word describing our boss, funny and true, and nothing else.
"""
import os

WORD = "Meetings"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")

if __name__ == "__main__":
    main()
