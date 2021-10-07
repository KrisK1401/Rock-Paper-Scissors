import random


def play():
    user = input("Pick your weapon: 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It seems you think alike'

    # r > s, p > r, s > p
    if is_win(user, computer):
        return 'You have won this round'

    return 'You lose fool!'


def is_win(player, opponent):
    # true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
