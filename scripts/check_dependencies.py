from pathlib import Path
import re
import sys

allowed = {"requests"}

requirements = Path("requirements.txt").read_text().splitlines()

for line in requirements:
    line = line.strip()

    if not line or line.startswith("#"):
        continue

    name = re.split(r"[<>=!~\[\s]", line, maxsplit=1)[0].lower()

    if name not in allowed:
        print(f"SECURITY ALERT: Unapproved dependency: {name}")
        sys.exit(1)

    print(f"APPROVED: {name}")

print("Dependency security check passed.")
