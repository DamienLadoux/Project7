import csv
from dataclasses import dataclass
from itertools import combinations


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

def brute_force(shares):

    best_combination = []
    best_cost = 0
    best_profit = 0

    for size in range(1, len(shares) + 1):
        for combination in combinations(shares, size):
            total_cost = sum(share.price for share in combination)
            total_profit = sum(share.profit for share in combination)
            if total_cost <= 500:
                if total_profit > best_profit:
                    best_profit = total_profit
                    best_cost = total_cost
                    best_combination = combination
    return best_combination, best_cost, best_profit

def main():

    shares = load_shares("data/actions.csv")
    best_combination, best_cost, best_profit = brute_force(shares)
    print("\nMeilleure combinaison :")
    for share in best_combination:
        print(share.name)
    print(f"\nCoût total : {best_cost:.2f} €")
    print(f"Bénéfice total : {best_profit:.2f} €")


if __name__ == "__main__":
    main()