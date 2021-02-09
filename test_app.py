import os
import unittest
import modules.utils

class TestUtils(unittest.TestCase):
    def test_Last_Number(self):
        test_list = [
        {"customer_id" : 1,"customer_name" : "Marcus","status" : "Accepted"},
        {"customer_id" : 2,"customer_name" : "Steve","status" : "Accepted"},
        {"customer_id" : 3,"customer_name" : "John","status" : "Accepted"}]
        # testing Last_Num gives the correct next number. 4
        result = modules.utils.Last_Num(test_list)
        self.assertEqual(result, "4") #(result, expected): assertEquals checks if result equals expected 
        self.assertEqual(modules.utils.Last_Num([]), "1") # test what happens when passing an emppty list


class TestDataPersistance(unittest.TestCase):
    def test_FromCSV(self):
        print("")
        
if __name__ == "__main__":
    unittest.main()
