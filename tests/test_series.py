from math_series.math_series import fibonacci , sum_series , lucas

# fib_array=[0, 1, 1, 2, 3, 5, 8, 13]
#fib_nth=[0th,1st,2th,....]

def test_fibonacci_0():
    expected=0
    actual=fibonacci(0)
    assert actual==expected
    
def test_fibonacci_1():
    expected=1
    actual=fibonacci(1)
    assert actual==expected  


def test_fibonacci_2():
    expected=1
    actual=fibonacci(2)
    assert actual==expected  


def test_fibonacci_3():
    expected=2
    actual=fibonacci(3)
    assert actual==expected 

def test_fibonacci_minus_number():
    expected='invalid input'
    actual=fibonacci(-3)
    assert actual==expected 

def test_fibonacci_string():
    expected='invalid input'
    actual=fibonacci('q')
    assert actual==expected 
        
        
# lucas_array=[2, 1, 3, 4, 7, 11, 18, 29]

def test_lucas_0():
    expected=2
    actual=lucas(0)
    assert actual==expected 


def test_lucas_1():
    expected=1
    actual=lucas(1)
    assert actual==expected   


def test_lucas_2():
    expected=3
    actual=lucas(2)
    assert actual==expected


def test_lucas_3():
    expected=4
    actual=lucas(3)
    assert actual==expected   


def test_lucas_minus_number():
    expected='invalid input'
    actual=lucas(-3)
    assert actual==expected 

def test_lucas_3():
    expected='invalid input'
    actual=lucas('q')
    assert actual==expected              


def sum_series_one_parameter_0():
    expected=0
    actual=sum_series(0)
    assert actual==expected

def sum_series_one_parameter_4():
    expected=3
    actual=sum_series(4)
    assert actual==expected  


def sum_series_three_parameters_lucas_0():
    expected=2
    actual=sum_series(0)
    assert actual==expected

def sum_series_not_lucas_not_fib_4():
    actual=sum_series(4,2,3)
    expected=13   
    assert actual==expected

def sum_series_not_lucas_not_fib_2():
    actual=sum_series(2,5,6)   
    expected=11
    assert actual==expected 



           
