import time
import os
from dotenv import load_dotenv

load_dotenv()

_cache = {}

ttl = int(os.getenv("CACHE_TTL", 86400))

def make_cache_key(name: str, date: str, sign: str, lang: str) -> str:
    return f"{name}-{date}-{sign}-{lang}"

def get_cached(key: str):
    if key in _cache:
        value, expiry = _cache[key]
        if expiry > time.time():
            return value
        else:
            del _cache[key]
    return None

def set_cache(key: str, value: str, ttl: int = ttl):
    _cache[key] = (value, time.time() + ttl)
