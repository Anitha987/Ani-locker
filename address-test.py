import unittest
form address import Address

 class TestAddress(unittest.TestCase):
   """
   Test class that defines test cases for the class of address.

   Args:
       unittest.TestCase:TestCase class that helps in creating test cases
   """  
  def setUp(self):
   """ 
   this setUp method will be run after each test cases.
   """
   self.new_address=Address("Anitha987","anithaumuhire@gmail.com","kigali555")
  def test_init(self):
    """
    the  init above will test if our objects are initialized well
    """"
    self.assertEqual(self.new_Address username,"Anitha987")
    self.assertEqual(self.new_Address email,"anithaumuhire@gmail.com")
    self.assertEqual(self.new_Address username,"kigali555")

    if_name_=='_main_':
      unittest.main()
