from app.products_app import *

def test_enlarge(): # name this function anything, but hopefully something corresponding to the function it is testing
    result = enlarge(3)
    assert result == 300  ## assert --> what our expectations are. Our desired results
