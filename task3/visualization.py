import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.style.use("ggplot")
# datasheet load
df = pd.read_csv("books_dataset.csv")
# datasheet check
print("=" * 50)
print("First 5 Rows")
print(df.head())

print("=" * 50)
print("Dataset Information")
print(df.info())

print("=" * 50)
print("Statistical Summary")
print(df.describe())

print("=" * 50)
print("Column Names")
print(df.columns)
# price coloumn clean
df["Price"] = df["Price"].str.replace("Â£", "", regex=False)
df["Price"] = df["Price"].astype(float)

print(df.head())

print("\nMissing Values")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)
# charts folder

os.makedirs("charts", exist_ok=True)
# histogram

plt.figure(figsize=(8,5))

plt.hist(df["Price"], bins=10)

plt.title("Price Distribution")

plt.xlabel("Price")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("charts/histogram.png")

plt.show()
# barchart

top10 = df.head(10)

plt.figure(figsize=(12,6))

plt.bar(top10["Book Name"], top10["Price"])

plt.xticks(rotation=90, fontsize=8)

plt.title("Top 10 Books Price")

plt.xlabel("Book Name")

plt.ylabel("Price")

plt.tight_layout()

plt.savefig("charts/bar_chart.png")

plt.show()
# piechart
top5 = df.head(5)

plt.figure(figsize=(7,7))

plt.pie(
    top5["Price"],
    labels=top5["Book Name"],
    autopct="%1.1f%%"
)

plt.title("Price Share of Top 5 Books")

plt.tight_layout()

plt.savefig("charts/pie_chart.png")

plt.show()

# linechart

plt.figure(figsize=(8,5))

plt.plot(df.index, df["Price"], marker="o")

plt.title("Book Prices")

plt.xlabel("Book Number")

plt.ylabel("Price")

plt.grid(True)

plt.savefig("charts/line_chart.png")

plt.show()
# seaborn histogram

plt.figure(figsize=(8,5))

sns.histplot(df["Price"], bins=10, kde=True)

plt.title("Histogram using Seaborn")

plt.savefig("charts/seaborn_histogram.png")

plt.show()

# box plot

plt.figure(figsize=(5,6))

sns.boxplot(y=df["Price"])

plt.title("Price Box Plot")

plt.savefig("charts/boxplot.png")

plt.show()
# summary
print("\n----- Price Summary -----")
print("Maximum Price :", df["Price"].max())
print("Minimum Price :", df["Price"].min())
print("Average Price :", round(df["Price"].mean(), 2))
print("Median Price  :", df["Price"].median())