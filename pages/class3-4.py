import random

number_to_guess = random.randint(1, 100)

min_user_guess = 1
max_user_guess = 100

while True:
    user_guess = int(input(f"請輸入{min_user_guess}到{max_user_guess}之間的數字: "))

    if user_guess < number_to_guess:
        print("太低了！")
        if user_guess > min_user_guess:
            min_user_guess = user_guess
    elif user_guess > number_to_guess:
        print("太高了！")
        if user_guess < max_user_guess:
            max_user_guess = user_guess
    else:
        print("恭喜你！你猜對了！")
        break
