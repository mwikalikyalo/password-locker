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

        if prompt == 'P1':
            print("Create a UserName")
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
            else:
                    print(f"Welcome: {entered_userName} to your Account")
                    print('\n')