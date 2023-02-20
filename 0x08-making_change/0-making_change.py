#!/usr/bin/python3
""" Make change on Coins."""


def makeChange(coins, total):
    """ Implementation of the make change."""
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1
    if total == 0:
        return num_coins
    else:
        return -1
