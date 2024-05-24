# hay 2 maneras de administrar sistemas en Python:
# os.system
#subprocess.run

import os   
# os system va a ejecutar bash
# los comandos entre "" son de bash y se quedan así

def add_user(): # solicitar nombre 
    username=input("Enter name of the user to admin")

# si existe usuario
    check_user=os.system(f"getent passwd {username}")

    if check_user==0:
        print(f"The username '{username}' already exists")
        return
    
    # 
    confirm = input(f"o you want to add {username} to the system?").lower()

    if confirm == 'y':
        result = os.system(f"suo useradd -m {username}")
        if result ==0:
            print(f"User {username} added auccessfully!")
        else:
            print(f"Failed to add {username}")

    else:
        print("user addition cancelled")

if __name__=="__main__":
    add_user()

