class Credential:
  """
  create a class credential  to hold our user accounts
  """
  credential_list[]
  def _init_(self,username,email,password,account)
  """
  _init_method will help us by the time  we want to use initialise all our objects 
  """
  self.username=username
  self.email=email
  self.password =password
  self.account=account
  def save_credential(self):
      '''
      save credential method will help us to save credential objects into credential-list
      '''
      Credential.credential_list.append(self)
