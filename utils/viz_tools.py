import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    plt.figure(figsize=(8,5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Histogram of {column}")
    path = f"hist_{column}.png"
    plt.savefig(path)
    return path
