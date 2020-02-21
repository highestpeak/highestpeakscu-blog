import hashlib

from configOperate import Setting

SECRET_KEY = Setting().get().get("secret_key")

def hash_pass(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def articleKey():
    return hash_pass(SECRET_KEY+"article")

def repoKey():
    return hash_pass(SECRET_KEY+"repo")

def tagKey():
    return hash_pass(SECRET_KEY+"tag")
