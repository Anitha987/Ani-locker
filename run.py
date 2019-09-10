# from login import Login
#!/usr/bin/env python3.6
from address import Address
from credential import Credential
def create_address(username,email,password):
  """
  Function to  create a new contact
  """
  new_address=Address(username,email,password)
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
def check(username,password):
  '''

  '''
  checking=Credential.check(username,password)
  return checking

def find_address(email):
  '''
  Function that finds an address by email and returns the contact
  '''
  return Address.find_by_email(email)
def check_existing_address(email):
  '''
  Function that check if the address exists with that email and return a Boolean
  '''
  return Address.address_exist(email)
def display_address():
  '''
  Function that returns all the saved address
  '''
  return Address.display_address()  
def login_address():
  '''
  function that help our users to login
  '''
  return Address.login_address()  
def create_credential(username,email,password,account):
  '''  
  function to createa new credential
  '''
  new_credential=Credential(username,email,password,account)
  return new_credential
def save_credential(credential):
  '''
  function to save credential
  '''
  credential.save_credential()
def del_credential(credential):
  '''
  function to delete a credential
  '''
  credential.delete_credential()
def find_credential(email):
  '''
  function that finds a credential by email and returns the credential
  '''
  return Credential.find_by_email(email)
def check_existing_credentials(email):
  '''
  function that check if a credential exists with that email and return a boolean
  '''
  return Credential.credential_exist(email) 
def display_credentials():
  '''
  function that returns all the saved credentials
  '''
  return Credential.display_credentials()
def main():
  print("welcome to your address list.what is your name?") 
  user_name=input()
  print(f"hi {user_name}.what would you like to do?")
  print('\n') 
  while True:
          print("use these short codes:ca-create a  new address,log- login ,da-display address,de-delete address,fa-find address,,ex-exit the address list")
          short_code=input().lower()
          if short_code=='ca':
            print("New Address")
            print("-" *10)

            print("username")
            username=input()

            print("email")
            email=input()

            print("password")
            password=input()

            save_address(create_address(username,email,password)) 
            print ('\n')
            print(f"New Address {username}created")
            print ('\n')
          # elif short_code =='log':
          #   print(' enter your username:  ')
          #   print('\n')
          #   username=input("enter your user name").strip()
          #   password=str(input("enter your password"))
          #   user_exist=check("username and password")
          #   if user_exist==username:
          #     while True:
          #       print("use these short code:un-username")
          #       short_code=input().lower()
              
          

          elif short_code == 'da':
              if display_address():
                print("Here is a list of your address")
                print('\n')

                for address in display_address():
                        print(f"{address.username} {address.email}.....{address.password}")

                print('\n')
              else:
                print('\n')
                print("You dont seem to have any address saved yet")
                print('\n')

          elif short_code == 'fa':

              print("Enter the address you want to search for")

              search_address = input()
              if check_existing_address(search_address):
                      search_address = find_address(search_address)
                      print(f"{search_address.username} {search_address.email}")
                      print('-' * 20)

                      print(f"email.......{search_address.email}")
                     
              else:
                      print("That address does not exist")
          elif short_code == 'de':
            print("your address has been deleted")
          elif short_code == "ex":
              print("See you.......")
              break
          else:
              print("I really didn't get that. Please use the short codes")
              break
          print("use these short codes:cc-create a  new credential,log-login ,dc-display credential,dc-delete credential,fc-find credential,,ex-exit the credential list")
          short_code=input().lower()
          if short_code=='cc':
            print("New credential")
            print("-" *10)

            print("username")
            username=input()

            print("email")
            email=input()

            print("password")
            password=input()

            print("account")
            account=input()

            save_credential(create_credential(username,email,password,account)) 
            print ('\n')
            print(f"New Credential {username}created")
            print ('\n')
          elif short_code == 'log':
            print(' enter your username:  ')
            print('\n')
            username=input("enter your user name").strip()
            account=input("enter your account").strip()
            password=str(input("enter your password"))
            user_exist=check(username,password)
            if user_exist==username:
              while True:
                print("use these short code:un-username")
                short_code=input().lower()
          

          elif short_code == 'dc':
              if display_credentials():
                print("Here is a list of your credential")
                print('\n')

                for credential in display_credentials():
                        print(f"{credential.username} {credential.email}.....{credential.password}")

                print('\n')
              else:
                print('\n')
                print("You don't seem to have any credential saved yet")
                print('\n')

          elif short_code == 'fc':

              print("Enter the credential you want to search for")

              search_credential = input()
              if check_existing_credentials(search_credential):
                      search_credential = find_credential(search_credential)
                      print(f"{search_credential.username} {search_credential.email}")
                      print('-' * 20)

                      print(f"email.......{search_credential.email}")
                      
              else:
                      print("That credential does not exist")
          elif short_code == 'dc':
            print("your credential has been deleted")
          elif short_code == "ex":
              print("See you.......")
              break
          else:
              print("I really didn't get that. Please use the short codes")         


if __name__ == '__main__':

    main()
