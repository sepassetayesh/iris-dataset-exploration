import pandas as pd

#  Data Loading
column_names = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Class']
data = pd.read_csv("../data/iris.data", names=column_names)

# Class-wise Subsetting
setosa_data = data[data['Class'] == 'Iris-setosa']
versicolor_data = data[data['Class'] == 'Iris-versicolor']
virginica_data = data[data['Class'] == 'Iris-virginica']


# STEP2
# Correlation Analysis

# Select only the numerical columns for correlation analysis
data_numeric = data[['Sepal length', 'Sepal width', 'Petal length', 'Petal width']]
# Compute the correlation matrix using Pearson's method
correlation_matrix = data_numeric.corr(method='pearson')
# Save the correlation matrix to a CSV file without headers or indices
correlation_matrix.to_csv("../dist/correlations.csv", header=False, index=False)
print("Correlations saved to 'dist/correlations.csv'")