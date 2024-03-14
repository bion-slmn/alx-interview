#!/usr/bin/python3
'''
defines a prime game and find the winner of the game
'''


def isWinner(x, nums):
    '''
    Determines the winner of the prime game using game theory.

    Parameters:
    x (int): Number of rounds to play.
    nums (list of int): A list where each element represents the total
                        number of numbers to play in a round.

    Returns:
    str or None: The winner of the prime game, or None
                if the scores of the players are equal.

    The prime game involves multiple rounds of finding
    prime numbers within a given range of numbers.
    Two players, 'Ben' and 'Maria', take turns playing.
    'Maria' starts the game.
    The player who finds the last prime number in each round earns a point.
    The function returns the name of the winner based on
    the accumulated points after 'x' rounds.
    If both players have the same score, it returns None.
    '''

    player = 'Maria'
    last_player = ''
    player_score = {'Ben': 0, 'Maria': 0}

    for rounds in range(x):
        for n in nums:
            p = 2
            # ben becomes the winner cause maria will fail
            if n < p:
                player_score['Ben'] += 1
                continue

            prime = [True for i in range(n+1)]

            while p <= n:
                if prime[p] is True:

                    last_player = player
                    for i in range(p, n+1, p):
                        prime[i] = False
                    player = 'Maria' if player == 'Ben' else 'Ben'

                p += 1

            player_score[last_player] += 1

    if player_score['Ben'] == player_score['Maria']:
        return None
    return (max(player_score, key=player_score.get))
