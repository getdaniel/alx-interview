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
    # Helper function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Function to play a single game
    def play_game(n):
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        player = 0  # Maria goes first, so player 0 is Maria and player 1 is Ben
        while primes:
            p = primes[0]  # Choose the smallest prime
            if player == 0:
                player = 1
            else:
                player = 0
            for i in range(p, n + 1, p):
                if i in primes:
                    primes.remove(i)
        return player

    # Play x rounds of the game and keep track of the winners
    winners = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = play_game(n)
        if winner is not None:
            if winner == 0:
                winners["Maria"] += 1
            else:
                winners["Ben"] += 1

    # Determine the overall winner
    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Maria"] < winners["Ben"]:
        return "Ben"
    else:
        return None
