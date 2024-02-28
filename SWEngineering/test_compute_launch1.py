from test_driven import  email_validator
def test_email_validatorT(): 
    assert email_validator('juno@email.com') == True

def test_email_validatorF(): 
    assert email_validator('juno@email@.com') == False