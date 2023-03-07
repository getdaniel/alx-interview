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
    # Check for invalid input
    if x < 1 or not nums:
        return None

    # Initialize counters for Maria and Ben's wins
    marias_wins = 0
    bens_wins = 0

    # Play the game for each round
    for i in range(x):
        n = nums[i]  # Get the value of n for this round
        primes = [True] * (n+1)  # Initialize a list of primes

        # Use the Sieve of Eratosthenes algorithm to generate primes
        for p in range(2, int(n**0.5)+1):
            if primes[p]:
                for i in range(p*p, n+1, p):
                    primes[i] = False

        # Count the number of primes in the range [1, n]
        primes_count = 0
        for j in range(2, n+1):
            if primes[j]:
                primes_count += 1

        # Determine the winner of this round
        if primes_count % 2 == 1:
            marias_wins += 1
        else:
            bens_wins += 1

    # Determine the overall winner
    if marias_wins == bens_wins:
        return None
    elif marias_wins > bens_wins:
        return 'Maria'
    else:
        return 'Ben'
