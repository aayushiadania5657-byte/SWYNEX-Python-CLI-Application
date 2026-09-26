def get_menu_choice():
    while True:
        choice = input("\nEnter your choice: ").strip()

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice

        print("Invalid choice. Please enter a number between 1 and 6.")