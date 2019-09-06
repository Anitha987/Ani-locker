from address import address
  def create_address(username,email,password,account)
  """
  Function to  create a new contact
  """
  new_address=Address(username,email,password,account)
  return new_address
  def save_address(address):
    '''
    Function to save address
    '''
    address.save_address()
  def del_address(address):
    '''
    Function to delete an address
    '''
    address.delete_address()  
  def find_address(email):
  '''
  Function that finds a contact by address and returns the contact
  '''
  return Address.find_by_email(email) 