from math import sqrt

def isPrime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number > 2:
        for i in range(2, int(sqrt(number))):
            if number % i == 0:
                return False
        return True


def test_small_2():
    assert isPrime(2) == False

def test_small_3():
    assert isPrime(3) == True

def test_small_21():
    assert isPrime(21) == False
