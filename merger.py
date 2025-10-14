import sys
from pathlib import Path
import shutil

# ANSI Colors
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

def merge_txt_files(original_file, new_file):
    # Checking files existence
    orig_path = Path(original_file)
    new_path = Path(new_file)

    if not orig_path.exists():
        print(f"File {RED}{original_file}{RESET} was not found.")
        sys.exit(1)
    if not new_path.exists():
        print(f"File {RED}{new_file}{RESET} was not found.")
        sys.exit(1)

    # Creating backup copy
    backup_path = orig_path.with_suffix(orig_path.suffix + ".bak")
    shutil.copy2(orig_path, backup_path)
    print(f"Created backup: {YELLOW}{backup_path.name}{RESET}")

    # Reading both files, removing empty and duplicate lines
    with open(orig_path, "r", encoding="utf-8") as f:
        original_lines = set(line.strip() for line in f if line.strip())

    with open(new_path, "r", encoding="utf-8") as f:
        new_lines = set(line.strip() for line in f if line.strip())

    # counting total, added and removed lines
    before_count = len(original_lines)
    merged = original_lines.union(new_lines)
    after_count = len(merged)

    added_count = len(merged - original_lines)
    removed_count = len(original_lines - merged)

    # Saving back to the original file
    with open(orig_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(merged)))

    print(f"File '{GREEN}{original_file}{RESET}' was updated.") 
    print(f"Total lines: {GREEN}{after_count}{RESET}.") 
    print(f"Added lines:{GREEN}{added_count}{RESET}. Removed lines: {GREEN}{removed_count}{RESET}.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merger.py <original.txt> <new.txt>")
        sys.exit(1)

    original_file = sys.argv[1]
    new_file = sys.argv[2]

    merge_txt_files(original_file, new_file)
