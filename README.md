# iris-dataset-exploration
### A Complete Reference Implementation 
**Course**: Machine Learning / Data Mining / Data Analysis 

**Topic**: Getting to Know Your Data – Exploratory Data Analysis on the Classic Iris Dataset  

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Dataset](https://img.shields.io/badge/Dataset-Iris%20(UCI)-brightgreen)](https://archive.ics.uci.edu/dataset/53/iris)

## Overview
This repository contains a **complete, clean, and well-documented solution** to the classic “Getting to Know Your Data” assignment using the famous **Iris dataset** (Fisher, 1936).

It is designed as a **reference implementation** that demonstrates best practices in:
- Univariate and multivariate statistical analysis  
- Correlation analysis (Pearson)  
- Comprehensive data visualization (2D & 3D)  
- Probability density estimation  
- Clean, reproducible Python code structure  

Perfect for students learning EDA, instructors looking for a high-quality sample solution, or professionals showcasing data analysis skills in their portfolio.

## What This Project Covers
| Section                      | Implemented Tasks                                                                                  |
|-----------------------------|----------------------------------------------------------------------------------------------------|
| 1. Univariate Statistics   | Full summary statistics (min, Q1, median, Q3, 95th percentile, mean, IQR, std, MAD, etc.) per species for **sepal width** |
| 2. Correlation Analysis     | Pearson correlation matrix + identification of strongest/weakest feature pairs                    |
| 3. Visualization            | • Class distribution bar plot<br>• Histograms (1D + 3D)<br>• Box plots (per class & bivariate)<br>• Quantile plots<br>• 6 pairwise scatter plots (color-coded by species)<br>• Interactive 3D scatter plot<br>• KDE-based PDF estimation per species |

All numerical results are rounded to 3 decimal places.

## Repository Structure
```text
iris-dataset-exploration/
├── src/
│   ├── step1.py                   # Univariate Statistics code
│   ├── step2.py                   # Correlation Analysis code
│   ├── step3.py                   # Visualization code 
│   └── run.py                     # Main executable – runs everything with one command
├── data/
│   └── iris.data                  
├── dist/
│   ├── statistics.csv             # Univariate stats per species (sepal width)
│   ├── correlations.csv           # 4×4 Pearson correlation matrix (no headers/index)
│   └── plots/                     # All figures automatically saved here
├── requirements.txt               # Minimal dependencies
└── README.md                      # You're reading it!
```
Running `python src/run.py` will:
- Compute all statistics and correlations
- Generate and save all required plots
- Export `statistics.csv` and `correlations.csv`

## Key Insights Discovered
- **Petal length** alone almost perfectly separates *Iris setosa* from the other two species  
- **Petal length + petal width** or **petal length + sepal length** are far superior to other features for classification  
- The dataset is perfectly balanced (50 samples × 3 classes)

## Requirements
```bash
pip install -r requirements.txt
```
Libraries used: pandas, numpy, matplotlib, seaborn

## How to Run
```bash
Bashgit clone https://github.com/sepassetayesh/iris-dataset-exploration.git
cd iris-exploratory-data-analysis
pip install -r requirements.txt
python src/run.py
```
All outputs will appear in the dist/ folder.

## Author
**Sepas Setayesh**  
Machine Learning Instructor & Practitioner

Feel free to use it as a learning resource, template for your own assignments, or portfolio piece.

⭐ If you find this helpful, please give it a star – it helps others discover quality educational code! 
Feedback and contributions are always welcome!

“The greatest value of the Iris dataset is not that it is hard, but that it beautifully illustrates how simple exploratory analysis can reveal almost perfect class separability.”