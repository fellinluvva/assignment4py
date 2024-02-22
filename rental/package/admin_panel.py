from user import User


def view_all_users(users):
    print("\nAll Users:")
    for user in users:
        print(user)


def add_new_user(users):
    user_id = input("Enter user ID: ")
    balance = float(input("Enter balance: "))
    users.append(User(user_id, balance))
    print("User added successfully.")


def main(users):
    while True:
        print("\nAdmin Panel:")
        print("1. View all users")
        print("2. Add new user")
        print("3. Exit Admin Panel")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_users(users)
        elif choice == "2":
            add_new_user(users)
        elif choice == "3":
            print("Exiting Admin Panel...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
