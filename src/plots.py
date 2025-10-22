import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv("data/llm_scores.csv")

df.head()

# df groupby typo_method and iteration and calculate mean score
mean_score = df.groupby(["typo_method", "iteration"])["score"].mean()

mean_score = mean_score.reset_index()

sns.lineplot(x="iteration", y="score", hue="typo_method", data=mean_score)
plt.show()