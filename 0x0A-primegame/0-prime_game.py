#!/usr/bin/python3
""" Prime Game."""


def isWinner(x, nums):
    """
    Determine who wins the most rounds of the prime game.

    Args:
    - x: number of rounds
    - nums: list of n for each round

    Returns:
    - Name of the player that won the most rounds.
      If the winner cannot be determined, return None.
    """
    def sieve(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i ** 2, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    def play_game(n):
        primes = sieve(n)
        current_player = "Maria"
        while primes:
            found_move = False
            for p in primes:
                if n % p == 0:
                    found_move = True
                    primes.remove(p)
                    current_player = "Ben" if current_player == "Maria" else "Maria"
                    break
            if not found_move:
                break
        return current_player

    maria_wins = ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
