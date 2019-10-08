from Prime import isPrime
import time

def test_small_2():
    time.sleep(2)
    assert isPrime(2) == True

def test_small_3():
    time.sleep(2)
    assert isPrime(3) == True

def test_small_21():
    time.sleep(2)
    assert isPrime(21) == False

