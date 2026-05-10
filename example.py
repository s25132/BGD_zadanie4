#Python example:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("transaction_report.csv")

country_summary = (
    df.groupby("country")["amount"]
      .sum()
      .sort_values(ascending=False)
)

print(country_summary.head(10))

# Create visualization
plt.figure(figsize=(8, 5))

country_summary.head(10).plot(kind="bar")

plt.xlabel("Country")
plt.ylabel("Total Transaction Amount")
plt.title("Top Countries by Transaction Value")

plt.tight_layout()
plt.show()