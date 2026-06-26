import pathlib
import sys

# Makes `from pages.login_page import LoginPage` work from any file under tests/.
sys.path.insert(0, str(pathlib.Path(__file__).parent))
