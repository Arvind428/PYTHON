import pandas as pd
import plotly.express as px
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("city_day.csv")
data.head()
# Checking for missing values
data.isnull().sum()
# data.dropna(axis=0, inplace=True)
# - Loads the CSV data using pandas
# - Inspects the first few rows
# - Checks for missing values
# - Removes rows with any null/missing data to ensure data quality


data['Date'] = pd.to_datetime(data['Date'])
# Converts the 'Date' column from string format to datetime format for proper
# chronological handling


# AQI Trend Over Time
fig1 = px.line(data, x='Date', y='AQI', color='City', title='AQI Trend Over Time')
fig1.show()
#  Creates an interactive line chart showing how AQI changes over time
# - Different colors represent different cities
# - Helps identify patterns, trends, and seasonal variations

# AQI Distribution by City
fig2 = px.box(data, x='City', y='AQI', title='AQI Distribution by City')
fig2.update_layout(xaxis={'categoryorder':'total descending'})
fig2.show()
# - Creates a box plot comparing AQI values across cities
# - Shows median, quartiles, and outliers for each city
# - Cities are sorted by average AQI (highest to lowest)

# Scatter Plot Matrix for selected features
selected_features = ['PM2.5', 'NO2', 'CO', 'O3', 'AQI']
fig3 = px.scatter_matrix(data[selected_features], title='Scatter Plot Matrix')
fig3.show()

# - Creates pairwise scatter plots to show relationships between pollutants and AQI
# - Helps identify which pollutants are most correlated with AQI

feature_columns = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']
# Splitting the dataset into features (X) and target (y)
X = data[feature_columns]
y = data['AQI']

# - **X** = Input features (all pollutant measurements)
# - **y** = Target variable (AQI value to predict)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizing the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# - Normalizes features to have mean=0 and std=1
# - Important for neural networks to converge faster and perform better
# - Uses the training data statistics to scale test data

# Defining and compiling the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

# **Model Structure:**
# - **Input Layer:** 12 neurons (one for each pollutant feature)
# - **Hidden Layer 1:** 64 neurons with ReLU activation
#   - ReLU: Introduces non-linearity to learn complex patterns
# - **Hidden Layer 2:** 32 neurons with ReLU activation
#   - Reduces dimensions and extracts higher-level features
# - **Output Layer:** 1 neuron
#   - Outputs the predicted AQI value
model.compile(optimizer='adam', loss='mean_squared_error')

# Training the model
history = model.fit(X_train_scaled, y_train, epochs=150, batch_size=32, validation_split=0.2)

# ```python
# history = model.fit(X_train_scaled, y_train, epochs=150, batch_size=32, validation_split=0.2)
# ```
# - **epochs=150:** Model trains for 150 iterations through the data
# - **batch_size=32:** Updates weights after every 32 samples
# - **validation_split=0.2:** Uses 20% of training data to validate during training
# - **Stores history:** Tracks loss metrics for visualization

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# - Plots training loss and validation loss over epochs
# - Shows if model is overfitting or underfitting
# - Helps verify model convergence

# Evaluate the model
loss = model.evaluate(X_test_scaled, y_test)
print("Mean Squared Error on Test Data:", loss)

# - Tests model on unseen data (test set)
# - Outputs MSE to show prediction accuracy on new data


model.save('model.h5')
user_input = pd.DataFrame({
    'PM2.5': [81],
    'PM10': [124],
    'NO': [1.44],
    'NO2': [20],
    'NOx': [12],
    'NH3': [10],
    'CO': [0.1],
    'SO2': [15],
    'O3': [127],
    'Benzene': [0.20],
    'Toluene': [6],
    'Xylene': [0.06]
})

user_input_scaled = scaler.transform(user_input)

user_pred = model.predict(user_input_scaled)

print(f"Predicted AQI: {user_pred[0][0]}")

# | Concept | Purpose |
# |---------|---------|
# | **Pandas** | Data loading, cleaning, and manipulation |
# | **Plotly** | Interactive data visualizations |
# | **Matplotlib** | Static plot visualization |
# | **Scikit-learn** | Train-test split and feature scaling |
# | **TensorFlow/Keras** | Building and training neural networks |
# | **Neural Networks** | Learning non-linear relationships between pollutants and AQI |
# | **Regression** | Predicting continuous AQI values |
