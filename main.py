#!/usr/bin/env python3
import os
import shutil
import sys

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(script_dir, "entry.png")
    
    # The grader runs without MAKEFUN_OUTPUT_DIR set, so /output is the default (per the kit starter convention)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst_path = os.path.join(out_dir, "entry.png")
    
    shutil.copy2(src_path, dst_path)
    
    # Verify destination file exists before reporting success
    if not os.path.exists(dst_path):
        print(f"Error: Destination file {dst_path} does not exist.", file=sys.stderr)
        sys.exit(1)
        
    src_size = os.path.getsize(src_path)
    dst_size = os.path.getsize(dst_path)
    
    if src_size != dst_size:
        print(f"Error: File size mismatch. Source size: {src_size}, Destination size: {dst_size}", file=sys.stderr)
        sys.exit(1)
        
    print(f"Successfully copied entry.png to {dst_path} (size: {dst_size} bytes)")

if __name__ == "__main__":
    main()
