import random
import matplotlib.pyplot as plt

from tqdm import tqdm


def coinToss(n: int, prob_tail: float = 0.5):
    n_tail = 0
    record = []
    coin = {0: "Head", 1: "Tail"}

    for _ in range(n):
        if random.random() <= prob_tail:
            n_tail += 1
            record.append(coin[1])
        else:
            record.append(coin[0])

    return n_tail, n, record


def simulate(n_rounds: int, n_coins: int, prob_tail: float = 0.5) -> dict:
    results = dict()

    for _ in tqdm(range(n_rounds), desc="Simulating..."):
        n_tails, n, _ = coinToss(n_coins, prob_tail)
        res = round(n_tails / n, 7)
        if res not in results.keys():
            results[res] = 0
        results[res] += 1

    return dict(sorted(results.items()))


def draw_curve(results: dict, n_coins: int, p_tail: int = 0.5):
    probs = results.keys()
    freqs = results.values()

    plt.figure(figsize=(12, 18))
    plt.xlabel("Ratio of n_tails to n")
    plt.ylabel("Frequency")
    plt.bar(probs, freqs, color="maroon", width=1 / n_coins)

    plt.savefig(f'output_{p_tail}.png')
    
    plt.show()


n_rounds = 500000
n_coins = 500
results = simulate(n_rounds, n_coins, 0.7)
draw_curve(results, n_coins, 0.7)
results = simulate(n_rounds, n_coins)
draw_curve(results, n_coins)
