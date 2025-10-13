import sys
from pathlib import Path

def merge_txt_files(original_file, new_file):
    # Checking files existence
    orig_path = Path(original_file)
    new_path = Path(new_file)

    if not orig_path.exists():
        print(f"File {original_file} was not found.")
        sys.exit(1)
    if not new_path.exists():
        print(f"File {new_file} was not found.")
        sys.exit(1)

    # Reading both files, removing empty and duplicate lines
    with open(orig_path, "r", encoding="utf-8") as f:
        original_lines = set(line.strip() for line in f if line.strip())

    with open(new_path, "r", encoding="utf-8") as f:
        new_lines = set(line.strip() for line in f if line.strip())

    merged = original_lines.union(new_lines)

    # Saving back to the original file
    with open(orig_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(merged)))

    print(f"File '{original_file}' was updated. Total lines: {len(merged)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merger.py <original.txt> <new.txt>")
        sys.exit(1)

    original_file = sys.argv[1]
    new_file = sys.argv[2]

    merge_txt_files(original_file, new_file)
