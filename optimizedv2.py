import csv
from dataclasses import dataclass
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
    Nettoyage des données et prépare le rapport d'exploration
    """

    shares = []
    invalid_lines = 0

    with open(file_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Ignore l'en-tête

        for row in reader:
            try:
                name=row[0]
                price=float(row[1])
                profit_percent=float(row[2].strip().replace("%", ""))
            except(ValueError, IndexError):
                invalid_lines += 1
                continue
            if price <=0 or profit_percent <=0:
                invalid_lines += 1
                continue
            shares.append(
                Share(
                    name=name,
                    price=price,
                    profit_percent=profit_percent
                )
            )
    return shares, invalid_lines

def exploration_report(shares, invalid_lines):
    """
    Affiche un rapport d'exploration du jeu de données.
    """

    print("\n========== RAPPORT D'EXPLORATION ==========\n")

    print(f"Nombre d'actions valides : {len(shares)}")
    print(f"Nombre d'actions ignorées : {invalid_lines}")

    prices = [share.price for share in shares]
    profits = [share.profit_percent for share in shares]

    print("\n----- Prix -----")
    print(f"Minimum : {min(prices):.2f} €")
    print(f"Maximum : {max(prices):.2f} €")
    print(f"Moyenne : {sum(prices) / len(prices):.2f} €")

    print("\n----- Profit (%) -----")
    print(f"Minimum : {min(profits):.2f} %")
    print(f"Maximum : {max(profits):.2f} %")
    print(f"Moyenne : {sum(profits) / len(profits):.2f} %")

    print("\n----- Répartition -----")
    print(f"Actions < 10 € : {sum(share.price < 10 for share in shares)}")
    print(f"Actions > 50 € : {sum(share.price > 50 for share in shares)}")
    print(f"Actions > 10 % de profit : {sum(share.profit_percent > 10 for share in shares)}")

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

    shares, invalid_lines = load_shares("data/dataset2.csv")
    exploration_report(shares, invalid_lines)
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