import os
from dotenv import load_dotenv
import google.generativeai as genai
from MD5 import hash_password_md5
from SQLinjection import get_user_data
import prompt
import inspect
from Database_pass import connect_db
from colorama import init, Fore, Style

init(autoreset = True)
INFO = Fore.CYAN
WARNING = Fore.YELLOW
ERROR = Fore.RED
SUCCESS = Fore.GREEN
NORMAL = Style.NORMAL

FAULT_KEYWORDS = {"error", "vulnerab", "weak", "hardcod", "issue", "fault", "danger", "secret", "password", "api_key"}

def print_colored(text, level="info"):
    if level == "info":
        print(INFO + text + NORMAL)
    elif level == "warning":
        print(WARNING + text + NORMAL)
    elif level == "error":
        print(ERROR + text + NORMAL)
    elif level == "success":
        print(SUCCESS + text + NORMAL)
    else:
        print(text)

def print_response_colored(response_text):
    lt = response_text.lower()
    if any(k in lt for k in FAULT_KEYWORDS):
        print(ERROR + response_text + NORMAL)
    else:
        print(SUCCESS + response_text + NORMAL)


malicious_username = "'admin' OR '1'=='1'"
user_password = "securepassword"
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")
# response = model.generate_content("Say 'Hello, security scanner!' if you can hear me.")

print("=" * 50)
print("Analyzing SQL Injection Example...")
print("=" * 50)
response = model.generate_content(prompt.security_prompt.format(code=inspect.getsource(get_user_data)))
print(response.text)# Test with hardcoded credentials
print("\n" + "=" * 50)
print("Analyzing Hardcoded Credentials Example...")
print("=" * 50)
response = model.generate_content(prompt.security_prompt.format(code=inspect.getsource(connect_db)))
print(response.text)# Test with weak cryptography
print("\n" + "=" * 50)
print("Analyzing Weak Cryptography Example...")
print("=" * 50)
response = model.generate_content(prompt.security_prompt.format(code=inspect.getsource(hash_password_md5)))
print(response.text)
