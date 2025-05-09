# disk_fill.py

import shutil
import os

def fill_disk_until(min_free_mb: int, path: str):
    block = b'\0' * (1024 * 1024)  # 1MB block
    file_path = os.path.join(path, "disk_fill.bin")
    os.makedirs(path, exist_ok=True)

    with open(file_path, "wb") as f:
        while True:
            free = shutil.disk_usage(path).free
            if free <= min_free_mb * 1024 * 1024:
                print(f"Stopped writing: free space is {free // (1024 * 1024)} MB.")
                break
            try:
                f.write(block)
            except Exception as e:
                print("Write error:", e)
                break

if __name__ == "__main__":
    # Reserve 10MB
    fill_disk_until(min_free_mb=10, path="/Users/Shared")
