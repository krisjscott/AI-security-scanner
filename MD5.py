import hashlib
def hash_password_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

user_password = "securepassword"
hashed_password = hash_password_md5(user_password)
print(f"MD5 hash of '{user_password}': {hashed_password}")
