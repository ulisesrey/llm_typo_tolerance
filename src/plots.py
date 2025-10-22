import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv("data/llm_scores.csv")

# Assuming 'df' is the DataFrame read from "data/llm_scores.csv"
# df = pd.read_csv("data/llm_scores.csv") 

# Use the raw DataFrame 'df' for the plot
# By default, 'sns.lineplot' calculates the mean of 'score' for each ('typo_method', 'iteration') 
# and plots the 95% confidence interval (CI) as the shaded area.
sns.lineplot(
    x="iteration", 
    y="score", 
    hue="typo_method", 
    data=df, 
    errorbar=("ci", 95) # Explicitly set to 95% Confidence Interval (the default)
)
iterations = df["iteration"].unique()
for iter_num in iterations:
    plt.axvline(
        x=iter_num, 
        color='gray',      # Color of the line
        linestyle='--',     # Dotted line style
        linewidth=1,       # Thickness of the line
        zorder=0,
        alpha=0.5           # Ensure the line is behind the data and bands
    )

plt.title("LLM Score Robustness Over Iterations (with 95% CI)")
plt.xlabel("Iteration (number of typos added)")
plt.ylabel("Mean Score (% of correct answers)")
plt.show()