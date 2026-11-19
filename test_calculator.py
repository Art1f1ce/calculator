from calculator import add, subtract, multiply, divide, circleArea

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(6, 2) == 3

def test_multiply():
    assert multiply(3, 5) == 15

def test_subtract():
    assert subtract(9, 4) == 5

def test_divide_uneven():
    #Arrange
    a, b = 5, 2
    #Act
    result = divide(a, b)
    #Assert
    assert result == 2.5

def test_circleArea():
    assert circleArea(-4) == "Error"