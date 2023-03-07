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
    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        # initialize a list of booleans to keep track of which numbers are prime
        primes = [True] * (n+1)
        primes[0] = primes[1] = False
        # mark all multiples of primes as composite
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n+1, i):
                    primes[j] = False
        turn = 0  # 0 for Maria, 1 for Ben
        while True:
            # find the smallest remaining prime
            p = next((p for p in range(2, n+1) if primes[p]), None)
            if not p:
                # no more primes left, the current player loses
                wins["Ben" if turn == 0 else "Maria"] += 1
                break
            # remove p and its multiples from the set
            for i in range(p, n+1, p):
                primes[i] = False
            # switch to the other player's turn
            turn = 1 - turn
    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
