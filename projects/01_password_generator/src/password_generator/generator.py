"""
Password generator utilities.
"""
import random
import string
from typing import List

AMBIGUOUS = set("il1Lo0O")

# small built-in wordlist for passphrases 
DEFAULT_WORDS = [
    "apple","orange","banana","river","mountain","sun","moon","star","forest","ocean",
    "cloud","stone","paper","table","chair","coffee","garden","shadow","ember","spark",
    "pixel","matrix","rocket","comet","atlas","zenith","orbit","harbor","pioneer","cobalt"
]

def generate_password(length: int = 12,
                      use_upper: bool = True,
                      use_lower: bool = True,
                      use_digits: bool = True,
                      use_special: bool = True,
                      exclude_ambiguous: bool = False,
                      use_passphrase: bool = False,
                      words: int = 4,
                      separator: str = "-") -> str:
    """
    Generate a password or passphrase.
    If use_passphrase is True -> return 'words' words joined by separator.
    Otherwise build a character pool and sample randomly.
    """
    if use_passphrase:
        chosen = [random.choice(DEFAULT_WORDS) for _ in range(max(1, words))]
        return separator.join(chosen)

    pool = ""
    if use_lower:
        pool += string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_special:
        pool += "!@#$%^&*()-_=+[]{};:,.<>?/"

    if exclude_ambiguous:
        pool = "".join(ch for ch in pool if ch not in AMBIGUOUS)

    if not pool:
        raise ValueError("At least one character set must be selected (lower/upper/digits/special).")

    return "".join(random.choice(pool) for _ in range(max(1, length)))
