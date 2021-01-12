import argparse
import getpass

def user_vars(args):
    if str(args.number) == "None":
        args.number = input("Enter a number: ")
    
    if str(args.password) == "None":
        args.password = getpass.getpass("Enter password: ")


def main():
    parser = argparse.ArgumentParser(description='Test Credentials')
    parser.add_argument('--number')
    parser.add_argument('--password')
    args = parser.parse_args()

    user_vars(args)

    print(args)

main()