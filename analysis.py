import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("=== Complete Data ===")
print(df)

print("\n=== Total Sales ===")
print(df["sales"].sum())

print("\n=== Category wise Sales ===")
print(df.groupby("category")["sales"].sum())

print("\n=== Product wise Sales ===")
print(df.groupby("product")["sales"].sum())

print("\n=== City wise Sales ===")
print(df.groupby("city")["sales"].sum())

df.groupby("product")["sales"].sum().plot(kind="bar")
plt.title("Product wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
