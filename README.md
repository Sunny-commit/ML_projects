# Machine Learning Projects

A comprehensive collection of machine learning projects and implementations covering supervised learning, unsupervised learning, deep learning, and data analysis.

## Overview

This repository contains diverse machine learning projects with complete datasets, Jupyter notebooks, and implementations of various algorithms and techniques. Projects range from basic classification to advanced deep learning models.

## Featured Projects

### **Supervised Learning**
- **Linear Regression**: Fuel consumption prediction, head-brain dataset analysis
- **Logistic Regression**: Binary classification problems, disease prediction
- **Decision Trees**: Drug recommendation system, classification models
- **Support Vector Machines (SVM)**: Classification tasks with kernel methods
- **K-Nearest Neighbors (KNN)**: Instance-based learning applications
- **Ensemble Methods**: Random forests, gradient boosting

### **Unsupervised Learning**
- **K-Means Clustering**: Customer segmentation, pattern discovery
- **Hierarchical Clustering**: Dendrograms, hierarchical analysis
- **DBSCAN**: Density-based clustering, outlier detection
- **Dimensionality Reduction**: PCA, feature extraction

### **Deep Learning**
- **Neural Networks**: Multi-layer perceptrons with TensorFlow
- **Convolutional Neural Networks**: Image classification, computer vision
- **Recurrent Neural Networks**: Sequence prediction, time series
- **Text Classification**: NLP with neural networks

### **Recommender Systems**
- **Collaborative Filtering**: Movie recommendations
- **Content-Based Filtering**: Item similarity matching

### **Data Analysis**
- **Exploratory Data Analysis (EDA)**: Visualization, statistics
- **Feature Engineering**: Feature scaling, transformation
- **Data Wrangling**: Cleaning, preprocessing

## Datasets Included

| Dataset | Size | Type | Projects |
|---------|------|------|----------|
| Iris Dataset | 4.5KB | CSV | Classification, KNN, SVM |
| Titanic Dataset | 60KB | CSV | Classification, Prediction |
| Boston Housing | 35KB | CSV | Regression, Linear Models |
| MNIST/Fashion MNIST | Large | Image | CNN, Deep Learning |
| Movie Data | 40MB | CSV | Recommendations, Analysis |
| Weather Data (AUS) | 14MB | CSV | Time Series, Forecasting |
| Credit Card | 400KB | CSV | Clustering, Anomaly Detection |

## Project Structure

```
ML_projects/
├── Datasets/                          # CSV and data files
│   ├── IRIS.csv
│   ├── Titanic.csv
│   ├── BostonHousing.csv
│   └── ... (multiple datasets)
├── Notebooks/                         # Jupyter notebooks
│   ├── Linear_Regression_2.ipynb
│   ├── K_Means.ipynb
│   ├── SVM.ipynb
│   ├── IRIS_DATASET.ipynb
│   └── ... (50+ notebooks)
├── Programs/                          # Python scripts
│   ├── functions.py
│   ├── utilities.py
│   └── ... (implementation files)
├── Certificates/                      # Achievement certificates
└── README.md
```

## Technology Stack

### Core Libraries
- **NumPy**: Numerical computing and arrays
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **Scikit-learn**: Machine learning algorithms

### Deep Learning
- **TensorFlow**: Neural networks and deep learning
- **Keras**: High-level API for neural networks
- **PyTorch**: Alternative deep learning framework

### Specialized Libraries
- **XGBoost**: Gradient boosting
- **NLTK**: Natural language processing
- **OpenCV**: Computer vision tasks

## Installation

### Prerequisites
- Python 3.7+
- Jupyter Notebook or JupyterLab
- pip package manager

### Setup

1. Clone the repository
```bash
git clone https://github.com/Sunny-commit/ML_projects.git
cd ML_projects
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
pip install tensorflow keras xgboost nltk
```

4. Launch Jupyter
```bash
jupyter notebook
```

## Quick Start

### Running a Notebook
```bash
# Navigate to the repository
cd ML_projects

# Open Jupyter
jupyter notebook

# Select any notebook to view and run cells
# Example: IRIS_DATASET.ipynb
```

### Example: Iris Classification
```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv('IRIS.csv')
X = df.drop('Species', axis=1)
y = df['Species']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2%}")
```

## Key Projects

### 1. **Titanic Survival Prediction**
- **Type**: Binary Classification
- **Features**: 11 passenger attributes
- **Algorithms**: Logistic Regression, SVM, Random Forest
- **Notebook**: `Titanic.csv` + `Logistic_regression.ipynb`

### 2. **Iris Flower Classification**
- **Type**: Multi-class Classification
- **Features**: Sepal/Petal dimensions
- **Algorithms**: KNN, SVM, Decision Trees
- **Notebook**: `IRIS_DATASET.ipynb`

### 3. **K-Means Customer Segmentation**
- **Type**: Unsupervised Clustering
- **Dataset**: Mall customer data
- **Applications**: Market segmentation, targeting
- **Notebook**: `K_Means.ipynb`

### 4. **Movie Recommendations**
- **Type**: Collaborative Filtering
- **Methods**: Matrix factorization, similarity
- **Notebook**: `Collaborative-Filtering-movies.ipynb`

### 5. **Deep Learning Models**
- **CNN**: Image classification
- **RNN**: Sequence prediction
- **LSTM**: Time series forecasting
- **Notebooks**: Multiple deep learning implementations

## Data Analysis Pipeline

```
1. Load Data
   ↓
2. Exploratory Data Analysis (EDA)
   ├── Statistical summary
   ├── Data visualization
   └── Correlation analysis
   ↓
3. Data Preprocessing
   ├── Handle missing values
   ├── Outlier detection
   ├── Feature scaling/normalization
   └── Encoding categorical variables
   ↓
4. Feature Engineering
   ├── Feature selection
   ├── Feature creation
   └── Dimensionality reduction
   ↓
5. Model Selection & Training
   ├── Algorithm choice
   ├── Hyperparameter tuning
   └── Cross-validation
   ↓
6. Model Evaluation & Validation
   ├── Performance metrics
   ├── Confusion matrix
   └── ROC/AUC curves
   ↓
7. Results & Insights
```

## Algorithms Covered

### Classification Algorithms
- Logistic Regression
- Support Vector Machines (SVM)
- K-Nearest Neighbors (KNN)
- Decision Trees
- Random Forests
- Naive Bayes
- Neural Networks

### Regression Algorithms
- Linear Regression
- Polynomial Regression
- Ridge & Lasso Regression
- Support Vector Regression

### Clustering Algorithms
- K-Means
- Hierarchical Clustering
- DBSCAN
- Gaussian Mixture Models

### Deep Learning
- Feedforward Neural Networks
- Convolutional Neural Networks (CNN)
- Recurrent Neural Networks (RNN)
- LSTM & GRU

### Ensemble Methods
- Random Forests
- Gradient Boosting
- XGBoost
- AdaBoost

## Performance Metrics

### Classification Metrics
- Accuracy, Precision, Recall, F1-Score
- ROC Curve, AUC Score
- Confusion Matrix
- Matthews Correlation Coefficient

### Regression Metrics
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R² Score

### Clustering Metrics
- Silhouette Score
- Davies-Bouldin Index
- Calinski-Harabasz Index

## Visualizations

- Histograms, Box plots, Scatter plots
- Heatmaps and Correlation matrices
- Confusion matrices
- ROC Curves and AUC plots
- Feature importance charts
- Cluster visualizations

## Best Practices Implemented

- ✅ Data validation and quality checks
- ✅ Train-test split methodology
- ✅ Cross-validation techniques
- ✅ Hyperparameter tuning
- ✅ Model evaluation and comparison
- ✅ Reproducible results with random seeds
- ✅ Documentation and comments
- ✅ Version control

## Common Use Cases

- **Prediction**: Regression and classification
- **Grouping**: Clustering and segmentation
- **Recommendations**: Collaborative filtering
- **Anomaly Detection**: Outlier identification
- **Ranking**: Feature importance analysis
- **Forecasting**: Time series prediction

## Notebooks Count

- **Total Notebooks**: 50+
- **Regression Projects**: 15+
- **Classification Projects**: 20+
- **Clustering Projects**: 10+
- **Deep Learning**: 8+
- **Analysis & Visualization**: 12+

## Certifications Included

- Machine Learning (edX)
- Java Data Structures (Codio)
- Specialized course certificates

## Contributing

1. Fork this repository
2. Create a feature branch
3. Add new projects or improvements
4. Submit a pull request

## Tips for Learning

### Beginners
1. Start with IRIS dataset
2. Learn about data preprocessing
3. Try basic algorithms (KNN, Decision Trees)
4. Understand evaluation metrics

### Intermediate
1. Explore ensemble methods
2. Try multiple datasets
3. Hyperparameter tuning
4. Cross-validation techniques

### Advanced
1. Deep learning models
2. Custom architectures
3. Time series forecasting
4. Production deployment

## Resources

- [Scikit-learn Documentation](https://scikit-learn.org)
- [TensorFlow/Keras Docs](https://tensorflow.org)
- [Pandas Documentation](https://pandas.pydata.org)
- [Matplotlib Tutorials](https://matplotlib.org)

## Author

Pateti Chandu (Sunny-commit)

## License

MIT License - Open source and free to use

## Support

For questions or issues, please open a GitHub issue.

## Roadmap

- [ ] Add more deep learning projects
- [ ] Implement production pipelines
- [ ] Add model explanability (SHAP, LIME)
- [ ] Time series forecasting models
- [ ] NLP project expansion
- [ ] Computer vision projects
