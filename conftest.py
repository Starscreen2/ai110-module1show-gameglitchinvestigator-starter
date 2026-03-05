import sys
from pathlib import Path


# Ensure the project root is on sys.path so tests can import top-level modules
PROJECT_ROOT = Path(__file__).resolve().parent
root_str = str(PROJECT_ROOT)
if root_str not in sys.path:
    sys.path.insert(0, root_str)

