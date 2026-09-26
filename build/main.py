#!/usr/bin/env python3
"""
Top Notch Auto Sales — static site builder.

Regenerates every HTML page in dist/ from the Python page templates in build/.
Run this after editing any file in build/ (page_*.py, common.py, vehicle_data.py).

Usage:
    python3 build/main.py
"""
import subprocess
import sys
import os

BUILD_DIR = os.path.dirname(os.path.abspath(__file__))

PAGE_SCRIPTS = [
    "page_home.py",
    "page_inventory.py",
    "page_about.py",
    "page_request.py",
    "page_contact.py",
    "page_sold.py",
]

def main():
    for script in PAGE_SCRIPTS:
        path = os.path.join(BUILD_DIR, script)
        print(f"Running {script}...")
        result = subprocess.run([sys.executable, path], capture_output=True, text=True)
        print(result.stdout.strip())
        if result.returncode != 0:
            print(f"ERROR in {script}:", result.stderr, file=sys.stderr)
            sys.exit(1)
    print("\nBuild complete. Output written to dist/")

if __name__ == "__main__":
    main()
