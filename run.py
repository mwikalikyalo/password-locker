from lib2to3.pygram import python_grammar_no_print_statement
import random

from click import prompt
from user import User
from credentials import Credentials

def create_new_credential(page_name, username, account_password):
    """Function to create a new account and its credentials"""
    new_credential = Credentials(page_name, username, account_password)
    return new_credential

def save_new_credential(credentials):
    """Function to save the newly created account and password"""
    credentials.save_credentials()

def find_credentials(page_name):
    """Function that finds credentials based on account_name given"""
    return Credentials.find_by_name(page_name)

def confirm_existing_credentials(name):
    """Method that checks whether a particular account and its credentials exist based on searched account_name"""
    return Credentials.find_by_name(name)

def display_credentials():
    """Function which displays all saved credentials"""
    return Credentials.display_credentials()

def delete_credentials(credentials):
    """Method that deletes credentials"""
    return Credentials.delete_credentials(credentials)

def main():

    while True:
        print("Welcome to the Password Locker.")
        print('\n')
        print("Use these prompts to select an option: Create New User use 'P1': Login to your account use 'P2': Display accounts use 'P3' To exit password locker 'P4'")
        prompt = input().lower()
        print('\n')

        #create new user for password locker
        if prompt == 'P1':
            print("Create a Username")
            created_user_name = input()

            print("Select a Password")
            created_user_password = input()

            print("Confirm Your Password")
            confirm_password = input()

            while confirm_password != created_user_password:
                print("Sorry your passwords did not match!")
                print("Enter a password")
                created_user_password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Congratulations {created_user_name}! You have created your new account.")
                print('\n')
                print("Proceed to Log In to your Account")
                print("Username")
                entered_username = input()
                print("Your Password")
                entered_password = input()

            while entered_username != created_user_name or entered_password != created_user_password:
                print("You entered a wrong username or password")
                print("Username")
                entered_userName = input()
                print("Your Password")
                entered_password = input()

            #logged on section
            else:
                print(f"Welcome: {entered_username} to your Account")
                print('\n')
                print("Select an option below to continue: ")
                print('\n')
                
                while True:
                    print("1: View Your saved credentials")
                    print("2: Add new credentials")
                    print("3: Remove credentials")
                    print("4: Search credentials")
                    print("5: Log Out")
                    selected = input()

                #add new credentials
                    if selected == '2':
                        while True:
                            print("Continue to add? y/n")
                            choice = input()
                            if choice == 'y'or'Y':
                                print("Enter The Account Name")
                                page_name = input()
                                print("Enter a password")
                                print("To generate random password enter letter 'a' or 'c' to create your own password")
                                letter = input().lower()
                                if letter == 'a':
                                    account_password = random.randint(111111, 1111111)
                                    print(f"Account: {page_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')
                                elif letter == 'c':
                                    print("Create your password")
                                    account_password = input()
                                    print(f"Account: {page_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')
                                else:
                                    print("Please enter a valid Code")

                                save_new_credential(create_new_credential(
                                    page_name, account_password))
                            elif choice == 'c':
                                break
                            else:
                                print("Please use 'y' for yes or 'n' for no!")

                    #display credentials
                    elif selected == '1':
                            while True:
                                print("Below is a list of all your credentials")
                                if display_credentials():

                                  for credential in display_credentials():
                                    print(f"PAGE NAME:{Credentials.page_name}")
                                    print(f"PASSWORD:{Credentials.password}")

                                else:
                                  print('\n')
                                  print("You don't seem to have any contacts yet")
                                  print('\n')

                                print("Back to Menu? y/n")
                                back = input().lower()
                                if back == 'y':
                                  break
                                elif back == 'n':
                                  continue
                                else:
                                  print("Please Enter a valid code")
                                continue

                    #logout
                    elif selected == '5':
                        print("WARNING! You will loose all your credentials if you log out. Are you sure? y/n")
                        logout = input().lower()

                        if logout == 'y':
                            print("You have Successfully logged out")
                            break
                        elif logout == 'n':
                            continue

                    #remove credentials   
                    elif selected == '3':
                        while True:
                            print("Search for credential to delete")
                            search_name = input()
                            print("")

                           


if __name__ == '__main__':
    main()