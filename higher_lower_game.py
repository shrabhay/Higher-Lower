"""
This program emulates a simple Higher Lower game. Online game available at https://www.higherlowergame.com/.
"""


from art import logo, vs
from functions import get_random_account, format_account, more_followers
import os
os.system('clear')

score = 0
game_on = True
A = get_random_account()
B = get_random_account()
print(logo)

while game_on:
    while B == A:
        B = get_random_account()

    print(f"Compare A: {format_account(A)}")
    print(vs)
    print(f"Against B: {format_account(B)}")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    os.system('clear')
    print(logo)

    if user_answer == more_followers(a_followers=A['follower_count'], b_followers=B['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}.")
        A = B
    else:
        game_on = False
        print(f"Sorry, that's wrong. Final score: {score}.")
