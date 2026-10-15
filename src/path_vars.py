from datetime import datetime
from pathlib import Path

TIME_NOW = datetime.now().strftime("%Y%m%d_%H%M%S")
ROOT_DIR = Path(__file__).parent.parent

# ENV
DOTENV_PATH = ROOT_DIR / ".env"
# DRIVER_PATH = ROOT_DIR / "driver" / "chromedriver.exe"
WIN_DRIVER_PATH = ROOT_DIR / "driver" / "geckodriver.exe"
LINUX_DRIVER_PATH = ROOT_DIR / "driver" / "geckodriver"
