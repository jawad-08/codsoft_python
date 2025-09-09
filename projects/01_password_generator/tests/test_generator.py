# simple pytest tests for generator functions
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from password_generator.generator import generate_password
from password_generator.strength import estimate_entropy

def test_length_default():
    p = generate_password()
    assert len(p) == 12

def test_custom_length():
    p = generate_password(length=20)
    assert len(p) == 20

def test_charset_presence():
    p = generate_password(length=30, use_upper=True, use_lower=True, use_digits=True, use_special=True)
    assert any(c.islower() for c in p)
    assert any(c.isupper() for c in p)
    assert any(c.isdigit() for c in p)
    assert any(c in "!@#$%^&*()-_=+[]{};:,.<>?/" for c in p)

def test_passphrase_words():
    p = generate_password(use_passphrase=True, words=3)
    assert len(p.split("-")) == 3 or len(p.split(" ")) == 3

def test_entropy_positive():
    p = generate_password(length=10)
    e = estimate_entropy(p)
    assert e > 0
