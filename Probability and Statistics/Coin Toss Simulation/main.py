import matplotlib.pyplot as plt
import numpy as np

from tqdm import tqdm
from collections import Counter


def simulate(n_rounds: int, n_coins: int, prob_tail: float = 0.5) -> dict:
    results = np.zeros(n_rounds)

    for i in tqdm(range(n_rounds), desc="Simulating..."):
        res = np.random.rand(n_coins, 1)
        results[i] += round(np.sum(res <= prob_tail) / n_coins, 7)

    return Counter(results.tolist())


def draw_curve(results: dict, n_coins: int, p_tail: int = 0.5):
    probs = results.keys()
    freqs = results.values()

    plt.figure(figsize=(12, 18))
    plt.xlabel("Ratio of n_tails to n")
    plt.ylabel("Frequency")
    plt.bar(probs, freqs, color="maroon", width=n_coins)

    plt.savefig(f"output_{p_tail}.png")

    plt.show()


n_rounds = 500000
n_coins = 50000
results = simulate(n_rounds, n_coins, 0.7)
draw_curve(results, n_coins, 0.7)
results = simulate(n_rounds, n_coins)
draw_curve(results, n_coins)
