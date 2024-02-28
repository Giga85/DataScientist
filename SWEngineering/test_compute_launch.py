from unit_test import days_until_launch
from test_driven import  email_validator

def test_days_until_launch_5():
    assert(days_until_launch(4, 9) == 5)
    
def test_days_until_launch_4():
    assert(days_until_launch(22, 26) == 4)

def test_days_until_launch_0():
    assert(days_until_launch(253, 253) == 0)

def test_days_until_launch_0_negative():
    assert(days_until_launch(83, 64) == 0)
    
def test_days_until_launch_1():
    assert(days_until_launch(9, 10) == 1)



def test_email_validatorT(): 
    assert email_validator('juno@email.com') == True

def test_email_validatorF(): 
    assert email_validator('juno@email@.com') == False