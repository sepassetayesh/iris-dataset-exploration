import pandas as pd

#  Data Loading
column_names = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Class']
data = pd.read_csv("../data/iris.data", names=column_names)

# Class-wise Subsetting
setosa_data = data[data['Class'] == 'Iris-setosa']
versicolor_data = data[data['Class'] == 'Iris-versicolor']
virginica_data = data[data['Class'] == 'Iris-virginica']


# STEP1
# Univariate Summary Statistics

# Number of missing values
missing_values_sepal_width_setosa = setosa_data['Sepal width'].isnull().sum()
missing_values_sepal_width_versicolor = versicolor_data['Sepal width'].isnull().sum()
missing_values_sepal_width_virginica = virginica_data['Sepal width'].isnull().sum()

# Minimum
min_sepal_width_setosa = setosa_data['Sepal width'].min()
min_sepal_width_versicolor = versicolor_data['Sepal width'].min()
min_sepal_width_virginica = virginica_data['Sepal width'].min()

# First quartile (Q1)
q1_sepal_width_setosa = setosa_data['Sepal width'].quantile(0.25)
q1_sepal_width_versicolor = versicolor_data['Sepal width'].quantile(0.25)
q1_sepal_width_virginica = virginica_data['Sepal width'].quantile(0.25)

# Median
median_sepal_width_setosa = setosa_data['Sepal width'].median()
median_sepal_width_versicolor = versicolor_data['Sepal width'].median()
median_sepal_width_virginica = virginica_data['Sepal width'].median()

# Second quartile (Q2) = Median
"""q2_sepal_width_setosa = setosa_data['Sepal width'].quantile(0.5)
q2_sepal_width_versicolor = versicolor_data['Sepal width'].quantile(0.5)
q2_sepal_width_virginica = virginica_data['Sepal width'].quantile(0.5) """

# Third quartile (Q3)
q3_sepal_width_setosa = setosa_data['Sepal width'].quantile(0.75)
q3_sepal_width_versicolor = versicolor_data['Sepal width'].quantile(0.75)
q3_sepal_width_virginica = virginica_data['Sepal width'].quantile(0.75)

# 95th percentile
p95_sepal_width_setosa = setosa_data['Sepal width'].quantile(0.95)
p95_sepal_width_versicolor = versicolor_data['Sepal width'].quantile(0.95)
p95_sepal_width_virginica = virginica_data['Sepal width'].quantile(0.95)

# Maximum
max_sepal_width_setosa = setosa_data['Sepal width'].max()
max_sepal_width_versicolor = versicolor_data['Sepal width'].max()
max_sepal_width_virginica = virginica_data['Sepal width'].max()

# Mean
mean_sepal_width_setosa = setosa_data['Sepal width'].mean()
mean_sepal_width_versicolor = versicolor_data['Sepal width'].mean()
mean_sepal_width_virginica = virginica_data['Sepal width'].mean()

# Range
range_sepal_width_setosa = max_sepal_width_setosa - min_sepal_width_setosa 
range_sepal_width_versicolor = max_sepal_width_versicolor - min_sepal_width_versicolor
range_sepal_width_virginica = max_sepal_width_virginica - min_sepal_width_virginica

# Interquartile range (IQR)
iqr_sepal_width_setosa = q3_sepal_width_setosa - q1_sepal_width_setosa 
iqr_sepal_width_versicolor = q3_sepal_width_versicolor - q1_sepal_width_versicolor
iqr_sepal_width_virginica = q3_sepal_width_virginica - q1_sepal_width_virginica

# Sample standard deviation
std_sepal_width_setosa = setosa_data['Sepal width'].std(ddof=1)
std_sepal_width_versicolor = versicolor_data['Sepal width'].std(ddof=1)
std_sepal_width_virginica = virginica_data['Sepal width'].std(ddof=1)

# Population standard deviation
std_pop_sepal_width_setosa = setosa_data['Sepal width'].std(ddof=0)
std_pop_sepal_width_versicolor = versicolor_data['Sepal width'].std(ddof=0)
std_pop_sepal_width_virginica = virginica_data['Sepal width'].std(ddof=0)

# Median absolute deviation (MAD)
mad_sepal_width_setosa =  (setosa_data['Sepal width'] - median_sepal_width_setosa).abs().median()
mad_sepal_width_versicolor = (versicolor_data['Sepal width'] - median_sepal_width_versicolor).abs().median()
mad_sepal_width_virginica = (virginica_data['Sepal width'] - median_sepal_width_virginica).abs().median()

# Calculate statistics for each species
stats = {
    'label': ['setosa', 'versicolor', 'virginica'],
    'missing_values': [
        missing_values_sepal_width_setosa,
        missing_values_sepal_width_versicolor,
        missing_values_sepal_width_virginica
    ],
    'min': [
        min_sepal_width_setosa,
        min_sepal_width_versicolor,
        min_sepal_width_virginica
    ],
    'q1': [
        q1_sepal_width_setosa,
        q1_sepal_width_versicolor,
        q1_sepal_width_virginica
    ],
    'median': [
        median_sepal_width_setosa,
        median_sepal_width_versicolor,
        median_sepal_width_virginica
    ],
    'q3': [
        q3_sepal_width_setosa,
        q3_sepal_width_versicolor,
        q3_sepal_width_virginica
    ],
    'p95': [
        p95_sepal_width_setosa,
        p95_sepal_width_versicolor,
        p95_sepal_width_virginica
    ],
    'max': [
        max_sepal_width_setosa,
        max_sepal_width_versicolor,
        max_sepal_width_virginica
    ],    
    'mean': [
        mean_sepal_width_setosa,
        mean_sepal_width_versicolor,
        mean_sepal_width_virginica
    ],
    'range': [
        range_sepal_width_setosa,
        range_sepal_width_versicolor,
        range_sepal_width_virginica
    ],
    'iqr': [
        iqr_sepal_width_setosa,
        iqr_sepal_width_versicolor,
        iqr_sepal_width_virginica
    ], 
    'std': [
        std_sepal_width_setosa,
        std_sepal_width_versicolor,
        std_sepal_width_virginica
    ], 
    'std_pop': [
        std_pop_sepal_width_setosa,
        std_pop_sepal_width_versicolor,
        std_pop_sepal_width_virginica
    ],
    'mad': [
        mad_sepal_width_setosa,
        mad_sepal_width_versicolor,
        mad_sepal_width_virginica
    ],  
}

# Create a DataFrame and Save the results to 'statistics.csv'
stats_df = pd.DataFrame(stats) 
stats_df = stats_df.round(3)
stats_df.to_csv('../dist/statistics.csv', index=False, header=False)
print("Statistics saved to 'dist/statistics.csv'")