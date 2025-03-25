import tempfile
import os
from pathlib import Path

temp_dir = tempfile.gettempdir()
LOG_DIR = Path(temp_dir) / "KYC Robot Logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

INFO = "info"
DEBUG = "debug"
WARNING = "warning"
ERROR = "error"
CRITICAL = "critical"
