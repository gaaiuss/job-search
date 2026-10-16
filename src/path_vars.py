from datetime import datetime
from pathlib import Path

TIME_NOW = datetime.now().strftime("%Y%m%d_%H%M%S")
ROOT_DIR = Path(__file__).parent.parent

# ENV
DOTENV_PATH = ROOT_DIR / ".env"

# Drivers

## Windows
EDGE_DRIVER = ROOT_DIR / "driver" / "msedgedriver.exe"
CHROME_DRIVER = ROOT_DIR / "driver" / "chromedriver.exe"

## Linux
FIREFOX_DRIVER = ROOT_DIR / "driver" / "geckodriver"
