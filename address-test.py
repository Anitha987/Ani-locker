import pyperclip
import unittest
from address import Address

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
      """
      self.assertEqual(self.new_address.username,"Anitha987")
      self.assertEqual(self.new_address.email,"anithaumuhire@gmail.com")
      self.assertEqual(self.new_address.password,"kigali555")
    def test_save_address(self):
      '''
      test_save_contact test case to test case to test if the contact act object is saved into the address_list
      '''
      self.new_address.save_address()
      self.assertEqual(len(Address.address_list),1)
    def tearDown(self):
        '''tearDown method will help us to clean up once  each test has been run
        '''
        Address.address_list=[]
    def test_save_multiple_address(self):
      '''
      test_save_multiple_address to check if we can save multiple address objects to our address_list
      '''
      self.new_address.save_address()   
      test_address=Address("Ronah","ronah@gmail.com","ronah123")
      test_address.save_address()
      self.assertEqual(len(Address.address_list),2)
    def test_delete_address(self):
      '''
      test_delete_address help to test if in our address we can be able to remove one of our address list
      '''
      self.new_address.save_address()
      test_address=Address("Ronah","ronah@gmail.com","ronah123")
      test_address.save_address()
      self.new_address.delete_address()
      self.assertEqual(len(Address.address_list),1) 
    def test_find_address(self):
      '''
      test_find_address help to testif we want to search one of our information
      '''
      self.new_address.save_address()
      test_address=Address("Ronah","ronah@gmail.com","ronah123")
      test_address.save_address()
      found_address = Address.find_by_email("ronah@gmail.com")
      self.assertEqual(found_address.email,test_address.email)
    def test_address_exists(self):
      '''
      test and see bty the time our address is not found to return a boolean.
      '''
      self.new_address.save_address
      test_address=Address("Ronah","ronah@gmail.com","ronah123")
      test_address.save_address()
      address_exists=Address.address_exist("ronah@gmail.com")
      self.assertTrue(address_exists)  
    def test_copy_email(self):
      '''
      Test to confirm that we are copying the email address  from a found address  
      '''
      self.new_address.save_address()
      Address.copy_email("anithaumuhire@gmail.com")
      self.assertEqual(self.new_address.email,pyperclip.paste())
if __name__ == '__main__':
    unittest.main()
  