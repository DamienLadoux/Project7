import csv
from dataclasses import dataclass
from itertools import combinations
import time

@dataclass
class Share:
    name: str
    price: float
    profit_percent: float

    @property
    def profit(self):
        return self.price * self.profit_percent / 100

def load_shares(file_path):
    """
    Lit le fichier CSV et retourne une liste d'objets Share.
    """

    shares = []

    with open(file_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)  # Ignore l'en-tête

        for row in reader:
            shares.append(
                Share(
                    name=row[0],
                    price=float(row[1]),
                    profit_percent=float(row[2].strip().replace("%", ""))
                )
            )
    return shares

def optimized_solution(shares):
    best_combination = []
    best_cost = 0
    best_profit = 0

    shares.sort(key=lambda share: share.profit_percent, reverse=True)
    for share in shares:
        if best_cost + share.price <= 500:
            best_combination.append(share)
            best_cost += share.price
            best_profit += share.profit
    return best_combination, best_cost, best_profit

def main():

    shares = load_shares("data/actions.csv")
    start = time.perf_counter()
    best_combination, best_cost, best_profit = optimized_solution(shares)
    end = time.perf_counter()
    print("\nMeilleure combinaison :")
    for share in best_combination:
        print(share.name)
    print(f"\nCoût total : {best_cost:.2f} €")
    print(f"Bénéfice total : {best_profit:.2f} €")
    print(f"Temps d'exécution : {end-start:.6f} secondes")

if __name__ == "__main__":
    main()