import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Produit": ["iPhone", "TV", "Laptop", "Cable", "iPhone", "TV", "Laptop", "Cable"],
    "Mois": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar", "Apr", "Apr"],
    "Ville": ["Casablanca", "Rabat", "Casablanca", "Fes", "Rabat", "Casablanca", "Fes", "Rabat"],
    "Ventes": [1200, 800, 950, 300, 1400, 750, 1100, 280]
}

df = pd.DataFrame(data)

df.groupby("Produit")["Ventes"].sum().plot(kind="bar", color="steelblue")
plt.title("Ventes par Produit")
plt.ylabel("Total Ventes")
plt.show()

df.groupby("Mois")["Ventes"].sum().plot(kind="bar", color="orange")
plt.title("Ventes par Mois")
plt.show()

df.groupby("Ville")["Ventes"].sum().plot(kind="bar", color="green")
plt.title("Ventes par Ville")
plt.show()
