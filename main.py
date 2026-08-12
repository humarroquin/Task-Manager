def main():
    is_running = True
    while is_running:
        user_choice = input("""What do you want to do?

    1. Add task
    2. List tasks
    3. Complete task
    4. Quit

Select a number: """)

        if user_choice == "1":
            print("Adding task...")

        elif user_choice == "2":
            print("Listing tasks...")

        elif user_choice == "3":
            print("Completing task...")

        elif user_choice == "4":
            print("Quit...")
            is_running = False


if __name__ == "__main__":
    main()
