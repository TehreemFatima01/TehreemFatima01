# Question 1
def countdown():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Countdown finished!\n")

# Question 2
def even_numbers():
    num = 2
    while num <= 20:
        print(num)
        num += 2
    print()

# Question 3
def sum_n_numbers():
    n = int(input("Enter a number: "))
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    print("Sum from 1 to", n, "is", total, "\n")

# Question 4
def input_validation():
    while True:
        num = int(input("Enter a number between 1 and 100: "))
        if 1 <= num <= 100:
            print("Valid number entered.\n")
            break
        else:
            print("Invalid number, try again.")

# Question 5
def print_string():
    s = input("Enter a string: ")
    i = 0
    while i < len(s):
        print(s[i])
        i += 1
    print()

# Question 6
def password_check():
    correct = "admin123"
    while True:
        pw = input("Enter password: ")
        if pw == correct:
            print("Access granted!\n")
            break
        else:
            print("Wrong password, try again.")

# Question 7
def guess_game():
    secret = 5
    guess = 0
    while guess != secret:
        guess = int(input("Guess the number (1 to 10): "))
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
    print("Correct guess!\n")

# Question 8
def count_digits():
    num = int(input("Enter a number: "))
    count = 0
    if num == 0:
        count = 1
    while num != 0:
        num = num // 10
        count += 1
    print("Total digits:", count, "\n")

# Question 9
def multiplication_table():
    num = int(input("Enter a number: "))
    i = 1
    while i <= 10:
        print(num, "x", i, "=", num * i)
        i += 1
    print()

# Question 10
def average_numbers():
    total = 0
    count = 0
    while True:
        num = int(input("Enter number (-1 to stop): "))
        if num == -1:
            break
        total += num
        count += 1
    if count == 0:
        print("No numbers entered.")
    else:
        print("Average is:", total / count)
    print()


# Main menu
def main():
    while True:
        print("Menu:")
        print("1. Countdown")
        print("2. Even Numbers")
        print("3. Sum of Numbers")
        print("4. Input Validation")
        print("5. Print String Characters")
        print("6. Password Check")
        print("7. Guessing Game")
        print("8. Count Digits")
        print("9. Multiplication Table")
        print("10. Average Calculator")
        print("0. Exit")

        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            countdown()
        elif choice == "2":
            even_numbers()
        elif choice == "3":
            sum_n_numbers()
        elif choice == "4":
            input_validation()
        elif choice == "5":
            print_string()
        elif choice == "6":
            password_check()
        elif choice == "7":
            guess_game()
        elif choice == "8":
            count_digits()
        elif choice == "9":
            multiplication_table()
        elif choice == "10":
            average_numbers()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


# Start program
main()
