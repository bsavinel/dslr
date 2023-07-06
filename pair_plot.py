import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/dataset_train.csv')
df = df.drop(columns=['First Name', 'Last Name', 'Birthday', 'Best Hand', 'Index'])

sns.pairplot(df, hue='Hogwarts House')
plt.show()