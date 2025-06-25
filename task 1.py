# india_population_visualization.py

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- BAR CHART ---

# Age group labels and corresponding population values (in millions)
age_groups = ['0–20 Years', '21–64 Years', '65+ Years']
population_millions = [512, 807, 98]
colors = ['gold', 'dodgerblue', 'hotpink']

# Create Bar Chart
plt.figure(figsize=(10, 6))
bars = plt.bar(age_groups, population_millions, color=colors, edgecolor='black')

# Add labels on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 10, f'{yval} Mn',
             ha='center', va='bottom', fontsize=12)

plt.title("India's Population Distribution by Age Group (2022)", fontsize=14)
plt.ylabel("Population (in millions)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("bar_chart.png", dpi=300)
plt.show()

# --- HISTOGRAM ---

# Simulate individual age data
np.random.seed(42)
ages = np.concatenate([
    np.random.randint(0, 21, 500),    # 0–20 years
    np.random.randint(21, 65, 700),   # 21–64 years
    np.random.randint(65, 100, 150)   # 65+ years
])

# Save age data to Excel for reference
df = pd.DataFrame(ages, columns=["Age"])
df.to_excel("india_age_distribution_sample.xlsx", index=False)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram of Simulated Indian Age Distribution", fontsize=14)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Number of People", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("histogram_from_python.png", dpi=300)
plt.show()
