# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "httpx>=0.28.1",
# ]
# ///
import httpx

print(f"HTTPX {httpx.__version__}")

def main() -> None:
    print("Hello from quick_report.py!")


if __name__ == "__main__":
    main()
