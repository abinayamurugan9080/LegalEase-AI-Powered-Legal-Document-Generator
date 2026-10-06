import os
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
API_URL = os.getenv("API_URL", "http://localhost:8000")
LOGO_PATH = os.path.join(BASE_DIR, "Image", "Logo.png")
INVERSE_LOGO_PATH = os.path.join(BASE_DIR, "Image", "inverseLogo.png")
FOOTER_TEXT = "LegalEase Inc. | contact@legalease.com | All Rights Reserved."
