import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('datasets/dataset_train.csv')

df_Ravenclaw = df[df['Hogwarts House'] == "Ravenclaw"].select_dtypes(['number'])
df_Slytherin = df[df['Hogwarts House'] == "Slytherin"].select_dtypes(['number'])
df_Gryffindor = df[df['Hogwarts House'] == "Gryffindor"].select_dtypes(['number'])
df_Hufflepuff = df[df['Hogwarts House'] == "Hufflepuff"].select_dtypes(['number'])

fig, axs = plt.subplots(ncols=3, nrows=int((len(df_Ravenclaw.columns) - 1) / 3 + 1), figsize=(20, 10))
fig.tight_layout(pad=2)
j = 0
for i in range(1, len(df_Ravenclaw.columns)):
	print((i - 1) % 3, int((i - 1) / 3))
	sns.barplot(x=["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"], y=[df_Ravenclaw.sum(axis=0)[i], df_Slytherin.sum(axis=0)[i], df_Gryffindor.sum(axis=0)[i], df_Hufflepuff.sum(axis=0)[i]], ax=axs[int((i - 1) / 3), (i - 1) % 3]).set(title=df_Ravenclaw.columns[i])

plt.show()
