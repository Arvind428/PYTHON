# Air Quality Index (AQI) Prediction Project - Simple Explanation

## 🎯 What is this project?
This project **predicts air pollution levels** using a Machine Learning model. It looks at different types of pollution (like PM2.5, NO2, CO, etc.) and predicts an AQI score.

**Think of it like:** Weather forecasting, but for air quality!

---

## 📊 What data does it use?
The project uses `city_day.csv` containing daily pollution measurements:
- 12 types of pollutants (PM2.5, PM10, NO2, CO, O3, etc.)
- Date of measurement
- City location
- **AQI value** (the thing we want to predict)

---

## 🔄 How it works (Simple Steps)

### Step 1: Load & Clean Data
```python
data = pd.read_csv("city_day.csv")
data.dropna(axis=0, inplace=True)
```
**What it does:** Reads the CSV file and removes any broken/missing data

---

### Step 2: Visualize the Data
```python
fig1 = px.line(data, x='Date', y='AQI', color='City')  # Line chart
fig2 = px.box(data, x='City', y='AQI')                # Box chart
fig3 = px.scatter_matrix(data)                        # Scatter chart
```
**What it does:** Shows charts to understand pollution patterns across cities and time

---

### Step 3: Prepare Data for Training
```python
X = data[['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']]
y = data['AQI']
```
**What it does:**
- `X` = Input (all pollutants)
- `y` = Output (AQI we want to predict)

---

### Step 4: Split Data
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```
**What it does:**
- 80% used for **training** the model
- 20% used for **testing** the model

---

### Step 5: Normalize Numbers
```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
```
**What it does:** Converts all numbers to similar scale (between -1 and 1) so the model learns better

---

### Step 6: Build Neural Network
```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])
```
**What it does:** Creates a simple brain-like model with:
- Input layer: Takes 12 pollutants
- Hidden layer 1: 64 neurons (learns patterns)
- Hidden layer 2: 32 neurons (simplifies patterns)
- Output layer: 1 neuron (gives AQI prediction)

---

### Step 7: Train the Model
```python
model.fit(X_train_scaled, y_train, epochs=150, batch_size=32)
```
**What it does:** Shows the model 150 times what pollution looks like and what AQI it produces (learns the pattern)

---

### Step 8: Check Performance
```python
loss = model.evaluate(X_test_scaled, y_test)
print("Mean Squared Error:", loss)
```
**What it does:** Tests the model on new data it hasn't seen before to check if it's accurate

---

### Step 9: Save the Model
```python
model.save('model.h5')
```
**What it does:** Saves the trained model so you can use it later without retraining

---

### Step 10: Make a Prediction
```python
user_input = pd.DataFrame({
    'PM2.5': [81], 'PM10': [124], 'NO': [1.44], ...
})
user_pred = model.predict(user_input_scaled)
print(f"Predicted AQI: {user_pred[0][0]}")
```
**What it does:** Takes new pollution data and predicts the AQI value

---

## 📚 Technologies Used
| Tool | What it does |
|------|-------------|
| **Pandas** | Reads & manages the CSV data |
| **Matplotlib/Plotly** | Shows charts & graphs |
| **Scikit-learn** | Splits data & normalizes numbers |
| **TensorFlow** | Creates & trains the neural network |

---

## ⚙️ How to Run It

1. **Install libraries:**
   ```bash
   pip install pandas plotly tensorflow scikit-learn matplotlib
   ```

2. **Make sure `city_day.csv` is in the same folder**

3. **Run the script:**
   ```bash
   python project.py
   ```

4. **You will see:**
   - Charts showing pollution trends
   - Model training progress
   - Final AQI prediction

---

## 🎬 Quick Summary
```
Data → Visualize → Split → Normalize → Train Model → Test Model → Save → Predict AQI
```

---

## 💡 Real-World Uses
- 🌍 **Air Quality Alerts** - Warn people when pollution will be high
- 🏙️ **City Planning** - Help governments reduce pollution
- 🏥 **Health Protection** - Alert vulnerable people (kids, elderly)
- 📊 **Research** - Understand which pollutants affect AQI most

---

## ✅ In One Sentence
**This project learns the pattern between pollution types and AQI score, then predicts future AQI based on pollution levels.**
