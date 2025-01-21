def main():
    print("Supermarket\n===========")

    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    total_sum = 0

    while True:
        try:
            choice = int(input("Please select product (1-10) 0 to Quit: "))
            if choice == 0:
                break
            elif 1 <= choice <= 10:
                price = prices[choice - 1]
                total_sum += price
                print(f"Product: {choice} Price: {price}")
            else:
                print("Invalid selection. Please choose a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Total: {total_sum}")

    while True:
        try:
            payment = int(input("Payment: "))
            if payment >= total_sum:
                change = payment - total_sum
                print(f"Change: {change}")
                break
            else:
                print("Not enough payment. Please enter an amount greater than or equal to the total.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
