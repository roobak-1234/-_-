# -*- coding: utf-8 -*-
"""sales prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CSjyks0SKm-yXU5ufOy4T0JBZvkKIMrh
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('/content/Advertising.csv')

df.head()

df

df.shape

df.describe()

sns.pairplot(df,hue="TV")

df['TV'].plot.hist(bins=10)

df['Radio'].plot.hist(bins=10,color="red")

df['Newspaper'].plot.hist(bins=10,color='black')

sns.heatmap(df.corr(),annot = True)
plt.show()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(df[['TV']],df[['Sales']], test_size=0.3,random_state=0)

print(X_train)

print(y_train)

from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(X_train,y_train)

res = LR.predict(X_test)
print(res)

LR.coef_

LR.intercept_

0.04581434*69.2+7.31081017

plt.plot(res)

plt.scatter(X_test,y_test)
plt.plot(X_test, 7.31081017+0.04581434*X_test, 'r')
plt.show()