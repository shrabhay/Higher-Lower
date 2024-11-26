from game_data import data
import random


def get_random_account():
    """
    Picks and returns a random item from the data list which contains different Instagram accounts and their associated info.
    :return: Random item (account) from the data list.
    """
    return random.choice(data)


def format_account(account):
    """
    Returns the formatted string of the details contained in the Instagram account.
    :param account: Instagram account picked from the data list, that contains name, description, and country.
    :return: Formatted string of the account details.
    """
    return f"{account['name']}, a {account['description']}, from {account['country']}."


def more_followers(a_followers, b_followers):
    """
    Determines which account has more Instagram followers.
    :param a_followers: Instagram follower count of account A.
    :param b_followers: Instagram follower count of account B.
    :return: The account (a or b) that has more followers.
    """
    if a_followers > b_followers:
        return 'a'
    return 'b'
