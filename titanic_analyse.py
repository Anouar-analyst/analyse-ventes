import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Question 1
df["Survived"].value_counts().plot(kind="bar", color=["red","green"])
plt.title("Morts vs Survivants")
plt.show()

# Question 2
df.groupby("Sex")["Survived"].mean().plot(kind="bar", color=["blue","orange"])
plt.title("Taux de survie : Femmes vs Hommes")
plt.show()

# Question 3
df.groupby("Pclass")["Survived"].mean().plot(kind="bar", color=["gold","silver","brown"])
plt.title("Taux de survie par classe")
plt.show()
