import os
import re
import sys


def find_misused_class_attributes(root_dirs):
    pattern = re.compile(r'<[^>]*\sclass=')
    found = False
    for root_dir in root_dirs:
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(('.jsx', '.tsx', '.js', '.ts')):
                    path = os.path.join(dirpath, filename)
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            for i, line in enumerate(f, 1):
                                if pattern.search(line):
                                    if not found:
                                        found = True
                                    print(f"{path}:{i}: {line.rstrip()}")
                    except Exception as e:
                        print(f"Error reading {path}: {e}")
    return found


if __name__ == "__main__":
    directories = sys.argv[1:] or ["components", "pages", "ar-pages"]
    print(f"Scanning directories: {directories}")
    has_errors = find_misused_class_attributes(directories)
    if has_errors:
        sys.exit(1)
