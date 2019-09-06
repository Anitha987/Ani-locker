class Address:
    """
    created a Class that will generate user's info
    """
    address_list=[]
    def __init__(self,username,email,password):

        '''
    _init_method which is going to help us define      properties for all our objects.
      Args:
            
        '''
        self.username=username
        self.email= email
        self.password =  password
    def save_address(self):
      '''
      save address method will help us to save address  objects into address-list
      '''
      Address.address_list.append(self)
    def delete_address(self):
      '''
      delete_address method deletes asavedaddress in case we want to remove one from our address_list
      '''
      Address.address_list.remove(self)  
    @classmethod
    def find_by_email(cls,email):
      '''
      method that takes in an email and returns an address that matches that email.

      Args:
        email:email to search for
      Returns: 
        address of person that  matches the email
      '''
      for address in cls.address_list:
        if address.email==email:
          return address
    @classmethod
    def address_exist(cls,email):
      '''
      Method that checks if our entered email exists from the  address list.
      Args:
          email:email to search if it exists
      Returns:
        Boolean:True or false depending ifthe address provided exists
      '''
      for address in cls.address_list:
        if address.email==email:
          return True
      return False  
    @classmethod
    def display_address(cls):
      '''
      method that returns our address list
      '''
      return cls.address_listy              
 
           
