#!/usr/bin/python3

import subprocess
import os


def add_user(user_name):
    result = subprocess.run(["sudo", "useradd", user_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"user {user_name} added successfully.")
    else:
        print(f"Error : {result.stderr}")


def modify_user(user_name, new):
    result = subprocess.run(["sudo", "usermod", "-l", new, user_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{user_name} updated to {new} successfully.")
    else:
        print(f"Error : {result.stderr}")


def delete_user(user_name):
    result = subprocess.run(["sudo", "userdel", "-r", user_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"user {user_name} deleted successfully.")
    else:
        print(f"Error : {result.stderr}")


def list_users():
    print("Users : ")
    with open("/etc/passwd", "r") as f:
        for line in f:
            username=line.split(':')[0]
            print(username)

def add_group(group_name):
    result = subprocess.run(["sudo", "groupadd", group_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"group {group_name} added successfully.")
    else:
        print(f"Error : {result.stderr}")

def modify_group(group_name,new):
    result = subprocess.run(["sudo","groupmod", "-n",new, group_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{group_name} updated to {new} successfully.")
    else:
        print(f"Error : {result.stderr}")

def delete_group(group_name):
    result = subprocess.run(["sudo", "groupdel",group_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"group {group_name} deleted successfully.")
    else:
        print(f"Error : {result.stderr}")

def list_groups():
    print("Groups : ")
    with open("/etc/group", "r") as f:
        for line in f:
            group_name=line.split(':')[0]
            print(group_name)

def disable_user(user_name):
    result = subprocess.run(["sudo", "usermod","-L", user_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"user {user_name} account disabled successfully.")
    else:
        print(f"Error : {result.stderr}")

def enable_user(user_name):
    result = subprocess.run(["sudo", "usermod","-U", user_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"user {user_name} account enabled successfully.")
    else:
        print(f"Error : {result.stderr}")

def change_password(user_name,password):
    cmd = f"echo '{user_name}:{password}' | sudo chpasswd"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{user_name}'s password updated successfully.")
    else:
        print(f"Error : {result.stderr}")

def main():
    if os.geteuid() != 0:
        print("Please run this script with sudo.")
        return

    while True:
        print("\n***** Manager Menu: ***** ")
        print("1. Add User")
        print("2. Modify User")
        print("3. Delete User")
        print("4. List Users")
        print("5. Add Group")
        print("6. Modify Group")
        print("7. Delete Group")
        print("8. List Groups")
        print("9. Disable User")
        print("10. Enable User")
        print("11. Change Password")
        print("12. About")
        print("13. Exit")
        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            username = input("Enter username to add : ")
            add_user(username)
        elif choice == 2:
            username = input("Enter username to modify : ")
            new_user = input("Enter new username : ")
            modify_user(username, new_user)
        elif choice == 3:
            username = input("Enter username to delete : ")
            delete_user(username)
        elif choice == 4:
            list_users()
        elif choice == 5:
            groupname = input("Enter group name  to add : ")
            add_group(groupname)
        elif choice == 6:
            groupname = input("Enter name of group to modify : ")
            new_group = input("Enter new name : ")
            modify_group(groupname,new_group)
        elif choice == 7:
            groupname = input("Enter group name to delete : ")
            delete_group(groupname)
        elif choice == 8:
            list_groups()
        elif choice == 9:
            username = input("Enter username to disable : ")
            disable_user(username)
        elif choice == 10:
            username = input("Enter username to enable : ")
            enable_user(username)
        elif choice == 11:
            username = input("Enter username to change its password : ")
            new_password = input("Enter new password : ")
            change_password(username,new_password)
        elif choice == 12:
            print("\nLinux User & Group Manager v1.")
        elif choice == 13:
            print("Exiting Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
