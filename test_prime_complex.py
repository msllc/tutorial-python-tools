from prime import isPrime
import time

def test_small_0():
    assert isPrime(0) == False

def test_small_1():
    assert isPrime(1) == False

def test_small_negative():
    assert isPrime(-7) == False

def test_small_21():
    time.sleep(2)
    assert isPrime(21) == False

