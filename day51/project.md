# Air Quality Index (AQI) Prediction Project

## Overview
This project builds a machine learning model to predict Air Quality Index (AQI) values based on various air pollutant measurements using a neural network implemented with TensorFlow/Keras.

## Project Purpose
The model analyzes city air quality data and predicts AQI values, which can be used to understand air pollution patterns and estimate air quality for given pollutant concentrations.

## Data Source
- **File**: `city_day.csv`
- **Format**: CSV dataset containing air quality measurements for different cities
- **Data Cleaning**: Missing values are removed before processing

## Technologies & Libraries Used
- **pandas**: Data loading and manipulation
- **plotly.express**: Interactive visualizations
- **tensorflow/keras**: Neural network model building and training
- **matplotlib**: Loss visualization
- **scikit-learn**: Data splitting and feature scaling

## Project Flow

### 1. Data Loading & Exploration
- Loads data from `city_day.csv`
- Displays first few rows with `data.head()`
- Checks for missing values with `data.isnull().sum()`
- Removes rows with missing values

### 2. Data Preprocessing
- Converts 'Date' column to datetime format
- Identifies feature columns for model input

### 3. Data Visualization
Three interactive visualizations are created:

#### a) **AQI Trend Over Time**
- Line plot showing AQI values over time
- Separated by city for comparison
- Helps identify temporal patterns

#### b) **AQI Distribution by City**
- Box plot comparing AQI distributions across different cities
- Cities ordered by total descending values
- Shows spread and outliers in each city

#### c) **Scatter Plot Matrix**
- Displays relationships between selected pollutants and AQI
- Features included: PM2.5, NO2, CO, O3, AQI
- Identifies correlations between variables

### 4. Model Development

#### Features (Input Variables)
The model uses 12 air quality features:
- PM2.5, PM10
- NO, NO2, NOx
- NH3, CO, SO2
- O3, Benzene, Toluene, Xylene

#### Target Variable
- **AQI** (Air Quality Index)

#### Data Splitting
- Training Set: 80% of data
- Test Set: 20% of data
- Random state: 42 (for reproducibility)

#### Feature Scaling
- Uses `StandardScaler` to normalize features
- Applied to both training and test sets

### 5. Neural Network Architecture
```
Input Layer: 12 features
    ↓
Dense Layer 1: 64 neurons, ReLU activation
    ↓
Dense Layer 2: 32 neurons, ReLU activation
    ↓
Output Layer: 1 neuron (AQI prediction)
```

#### Model Configuration
- **Optimizer**: Adam
- **Loss Function**: Mean Squared Error (MSE)
- **Training Parameters**:
  - Epochs: 150
  - Batch Size: 32
  - Validation Split: 20%

### 6. Model Training & Evaluation
- Trains the model on scaled training data
- Validates on 20% of training data during training
- Plots training and validation loss curves to monitor learning
- Evaluates on test set with MSE metric
- Saves the trained model as `model.h5`

### 7. Prediction Example
Makes a sample prediction with user-input air quality measurements:
- PM2.5: 81 µg/m³
- PM10: 124 µg/m³
- NO: 1.44 ppb
- NO2: 20 ppb
- NOx: 12 ppb
- NH3: 10 µg/m³
- CO: 0.1 ppm
- SO2: 15 µg/m³
- O3: 127 ppb
- Benzene: 0.20 µg/m³
- Toluene: 6 µg/m³
- Xylene: 0.06 ppb

**Output**: Predicted AQI value for the given pollutant concentrations

## Key Insights
- The model learns the relationship between multiple air pollutants and overall air quality
- Visualization helps identify which cities and time periods have worse air quality
- The neural network can generalize and predict AQI for new, unseen pollutant combinations

## Files Generated
- `model.h5`: Trained neural network model (saved for future use)

## Potential Improvements
- Hyperparameter tuning for better accuracy
- Cross-validation for more robust evaluation
- Feature engineering to extract more meaningful signals
- Handling of temporal dependencies (time series models like LSTM)
- Ensemble methods for improved predictions
- Regular model retraining with new data
