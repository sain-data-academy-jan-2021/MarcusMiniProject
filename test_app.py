import os
from modules.utils import Last_Num

# test to see if it gets the last customer id, and adds 1 to it
def test_Last_Number():
    #assemble
    test_list = [
    {"customer_id" : 1,"customer_name" : "Marcus","status" : "Accepted"},
    {"customer_id" : 2,"customer_name" : "Steve","status" : "Accepted"},
    {"customer_id" : 3,"customer_name" : "John","status" : "Accepted"}]
    expected = "4"
    #act
    actual = Last_Num(test_list)
    # Assert
    assert expected == actual
    print("Passed test 1")
test_Last_Number()
    
# #Test to see what happens if an empty table is passed to the function
def TestEmptyTablePassed():
    #assemble
    emptytable = []
    expected = "1"
    #act
    actual = Last_Num(emptytable)
    # Assert
    assert expected == actual
    print("Passed test 2")
TestEmptyTablePassed()
