import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#  Data Loading
column_names = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Class']
data = pd.read_csv("../data/iris.data", names=column_names)

# Class-wise Subsetting
setosa_data = data[data['Class'] == 'Iris-setosa']
versicolor_data = data[data['Class'] == 'Iris-versicolor']
virginica_data = data[data['Class'] == 'Iris-virginica']


# STEP3
# Visualization

# Distribution of Labels
# Count the occurrences of each species
species_counts = data['Class'].value_counts()
# Create the BAR PLOT
species_counts.plot(kind='bar', color=['blue', 'orange', 'green'])
plt.title('Distribution of Iris Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.savefig("../dist/plots/1-BarPlot.png", format='png', dpi=300, bbox_inches='tight')


# Histogram

# Create a figure with two subplots
plt.figure(figsize=(12, 5))
# Histogram for Sepal width
plt.subplot(1, 2, 1)
plt.hist(data['Sepal width'], bins=8, color='orange', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width')
plt.ylabel('Frequency')
# Histogram for Petal length
plt.subplot(1, 2, 2)
plt.hist(data['Petal length'], bins=8, color='blue', edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
# Show the plot
plt.tight_layout()
plt.savefig("../dist/plots/2-Histogram.png", format='png', dpi=300, bbox_inches='tight')


# 3D Histogram

# Define bins for Petal length and Sepal width
petal_length_bins = np.linspace(data['Petal length'].min(), data['Petal length'].max(), 10)
sepal_width_bins = np.linspace(data['Sepal width'].min(), data['Sepal width'].max(), 10)
# Create a 2D histogram
hist, xedges, yedges = np.histogram2d(data['Petal length'], data['Sepal width'], bins=[petal_length_bins, sepal_width_bins])
# Create the 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
# Create meshgrid for plotting
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0
# Plot bars with heights based on the histogram counts
dx = dy = 0.5  # Width of each bin
dz = hist.ravel()
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', color='teal', edgecolor='black')
# Labeling the axes
ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Width')
plt.title("3D Histogram")
plt.savefig("../dist/plots/2-3DHistogram.png", format='png', dpi=300, bbox_inches='tight')


# Box Plot

plt.figure(figsize=(12, 6))
# Box plot for Sepal width
plt.subplot(1, 2, 1)
sns.boxplot(x='Class', y='Sepal width', data=data, hue='Class', palette='Set2', dodge=False)
plt.legend([],[], frameon=False)
plt.title('Distribution of Sepal Width by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Width')
# Box plot for Petal length
plt.subplot(1, 2, 2)
sns.boxplot(x='Class', y='Petal length', data=data, hue='Class', palette='Set2', dodge=False)
plt.legend([],[], frameon=False)
plt.title('Distribution of Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length')
# Show the plots
plt.tight_layout()
plt.savefig("../dist/plots/3-BoxPlot.png", format='png', dpi=300, bbox_inches='tight')


# Two-dimensional Box Plot

plt.figure(figsize=(18, 6))
# Create a 2D boxplot using 'Petal length' on the x-axis and 'Sepal width' on the y-axis
sns.boxplot(x=data['Petal length'], y=data['Sepal width'])
plt.title('Distribution of Sepal Width vs Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Sepal Width')
plt.savefig("../dist/plots/3-2DBoxPlot.png", format='png', dpi=300, bbox_inches='tight')


# Quantile Plot

def quantile_plot(feature, label):
    quantiles = np.linspace(0, 1, 100)
    feature_values = data[feature].sort_values().values
    quantile_values = np.quantile(feature_values, quantiles)
    plt.plot(quantiles, quantile_values, label=label)
# Generate quantile plot for 'Petal length'
plt.figure(figsize=(10, 6))
quantile_plot('Petal length', 'Petal Length')
plt.title('Quantile Plot for Petal Length')
plt.xlabel('Quantile')
plt.ylabel('Petal Length')
plt.grid(True)
plt.legend()
plt.savefig("../dist/plots/4-QuantilePlotPL.png", format='png', dpi=300, bbox_inches='tight')
# Generate quantile plot for 'Sepal width'
plt.figure(figsize=(10, 6))
quantile_plot('Sepal width', 'Sepal Width')
plt.title('Quantile Plot for Sepal Width')
plt.xlabel('Quantile')
plt.ylabel('Sepal Width')
plt.grid(True)
plt.legend()
plt.savefig("../dist/plots/4-QuantilePlotSW.png", format='png', dpi=300, bbox_inches='tight')


# Scatter Plot

# Create a figure with subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
# Define the feature pairs and plot them
feature_pairs = [
    ('Sepal length', 'Sepal width'),
    ('Sepal length', 'Petal length'),
    ('Sepal length', 'Petal width'),
    ('Sepal width', 'Petal length'),
    ('Sepal width', 'Petal width'),
    ('Petal length', 'Petal width')
]
species_colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'blue', 'Iris-virginica': 'green'}
# Iterate through the feature pairs and axes to plot each scatter plot
for i, (feat1, feat2) in enumerate(feature_pairs):
    ax = axes[i // 3, i % 3]  # Determine the subplot location
    for species, color in species_colors.items():
        species_data = data[data['Class'] == species]
        ax.scatter(species_data[feat1], species_data[feat2], label=species, color=color, alpha=0.7)
    
    ax.set_xlabel(feat1)
    ax.set_ylabel(feat2)
    ax.set_title(f'{feat1} vs {feat2}')
    ax.legend()
plt.savefig("../dist/plots/5-ScatterPlot.png", format='png', dpi=300, bbox_inches='tight')


# 3D Scatter Plot

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Plot data points for each species in different colors
for species, group in data.groupby('Class'):
    ax.scatter(group['Sepal length'], group['Sepal width'], group['Petal length'], label=species)
# Label the axes
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')
ax.legend()
plt.savefig("../dist/plots/5-3DScatterPlot.png", format='png', dpi=300, bbox_inches='tight')


# probability density function (PDF)

# Set up the plot
plt.figure(figsize=(10, 6))
# Plot the KDE for each species
species = data['Class'].unique()
for species_name in species:
    sns.kdeplot(data=data[data['Class'] == species_name]['Petal length'], 
                label=species_name, fill=True, common_norm=False)

# Set title and labels
plt.title('Probability Density Function of Petal Length by Species')
plt.xlabel('Petal Length')
plt.ylabel('Density')
plt.legend(title='Species')
plt.savefig("../dist/plots/6-PDF.png", format='png', dpi=300, bbox_inches='tight')


print("All plots saved to 'dist/plots/'")