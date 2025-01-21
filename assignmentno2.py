def main():
    shopping_list = []

    while True:
        print("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?: ", end="")
        choice = input().strip()

        if choice == "1":
            item = input("What will be added?: ").strip()
            shopping_list.append(item)

        elif choice == "2":
            list_length = len(shopping_list)
            print(f"There are {list_length} items in the list.")
            try:
                index = int(input("Which item is deleted?: ").strip())
                if 0 <= index < list_length:
                    shopping_list.pop(index)
                else:
                    print("Incorrect selection.")
            except ValueError:
                print("Incorrect selection.")

        elif choice == "3":
            print("The following items remain in the list:")
            for item in shopping_list:
                print(item)
            break

        else:
            print("Incorrect selection.")

# Run the main function
if __name__ == "__main__":
    main()