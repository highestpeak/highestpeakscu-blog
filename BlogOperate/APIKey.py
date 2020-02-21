import hashlib

from config import secret_key


def hash_pass(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def articleKey():
    return hash_pass(secret_key+"article")

def repoKey():
    return hash_pass(secret_key+"repo")

def tagKey():
    return hash_pass(secret_key+"tag")
