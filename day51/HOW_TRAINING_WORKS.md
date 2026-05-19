# How Model Training Works in AQI Prediction Project

## Training Code
```python
history = model.fit(X_train_scaled, y_train, epochs=150, batch_size=32, validation_split=0.2)
```

---

## 📖 Understanding the Parameters

### 1. **X_train_scaled** (Input Data)
- 80% of the original dataset (after train-test split)
- 12 pollutant columns (PM2.5, PM10, NO2, etc.)
- Already normalized using StandardScaler

### 2. **y_train** (Target Data)
- AQI values corresponding to X_train_scaled
- What the model learns to predict

### 3. **epochs=150**
- One **epoch** = one complete pass through all training data
- Model sees all training data 150 times
- With each epoch, the model improves

**Visual:**
```
Epoch 1:   Model predicts AQI → Calculates error → Updates weights
Epoch 2:   Model predicts AQI → Calculates error → Updates weights
Epoch 3:   Model predicts AQI → Calculates error → Updates weights
...
Epoch 150: Model predicts AQI → Calculates error → Updates weights
```

### 4. **batch_size=32**
- Splits training data into groups of 32 samples
- Updates weights after every 32 samples (not after each sample)

**Example with 1000 training samples:**
```
Batch 1: Samples 1-32    → Update weights
Batch 2: Samples 33-64   → Update weights
Batch 3: Samples 65-96   → Update weights
...
Batch 32: Samples 993-1000 → Update weights
(One epoch complete, start Epoch 2)
```

### 5. **validation_split=0.2**
- Uses 20% of training data to validate during training
- 80% for actual training, 20% for validation
- Helps detect overfitting in real-time

---

## 🔄 What Happens During Training (Step-by-Step)

### Step 1: Random Weight Initialization
```
Neural Network Created with Random Weights:
Input Layer → Hidden Layer 1 (64 neurons) → Hidden Layer 2 (32 neurons) → Output Layer
       ↓                  ↓                          ↓                        ↓
  12 inputs      Random weights ~0.01        Random weights         Random weights
```

### Step 2: Forward Pass (Prediction)
```python
# Simplified calculation for one sample:
sample = [PM2.5=81, PM10=124, NO=1.44, ..., Xylene=0.06]

# Through Hidden Layer 1 (64 neurons)
hidden1_output = ReLU(W1 @ sample + b1)  # 64 values

# Through Hidden Layer 2 (32 neurons)
hidden2_output = ReLU(W2 @ hidden1_output + b2)  # 32 values

# Through Output Layer (1 neuron)
predicted_AQI = W3 @ hidden2_output + b3  # 1 value (e.g., 98.5)
```

### Step 3: Calculate Loss (Error)
```python
# For one sample:
actual_AQI = 100
predicted_AQI = 98.5

error = (actual_AQI - predicted_AQI)² = (100 - 98.5)² = 2.25

# For all 32 samples in batch (MSE Loss):
batch_loss = average_of_all_errors = (error1 + error2 + ... + error32) / 32
```

### Step 4: Backward Pass (Calculate Gradients)
```
Using Backpropagation Algorithm:

Error at Output
     ↓
Gradient for Output Layer weights (dW3/dloss)
     ↓
Gradient for Hidden Layer 2 weights (dW2/dloss)
     ↓
Gradient for Hidden Layer 1 weights (dW1/dloss)
```

**What is a gradient?**
- Shows which direction to adjust weights
- If gradient = +0.05 → increase weight
- If gradient = -0.05 → decrease weight

### Step 5: Update Weights (Adam Optimizer)
```python
# Before update
W1_old = [0.012, -0.015, 0.008, ...]

# Adam calculates how much to change
learning_rate = 0.001 (typically)
new_weight = old_weight - learning_rate × gradient

# After update
W1_new = [0.011, -0.014, 0.007, ...]  # Slightly adjusted
```

### Step 6: Repeat for All Batches
```
Epoch 1:
  Batch 1 (32 samples) → Loss = 45.2 → Update weights
  Batch 2 (32 samples) → Loss = 44.8 → Update weights
  Batch 3 (32 samples) → Loss = 43.5 → Update weights
  ...
  (All batches complete = 1 Epoch)

Epoch 2: (All batches again with better weights)
Epoch 3: (All batches again with even better weights)
...
Epoch 150: (Final training with best weights)
```

---

## 📊 Training Process Visualization

```
Epoch 1    Loss = 80.2  │ Validation Loss = 78.5
Epoch 2    Loss = 72.1  │ Validation Loss = 70.3
Epoch 3    Loss = 61.5  │ Validation Loss = 60.2
Epoch 4    Loss = 52.3  │ Validation Loss = 51.8
...
Epoch 50   Loss = 15.2  │ Validation Loss = 15.8
Epoch 100  Loss = 8.5   │ Validation Loss = 9.2
Epoch 150  Loss = 6.2   │ Validation Loss = 7.1

↓ (Lower loss = Better predictions)
```

---

## 🎯 Example: Training One Batch

**Input Data (Batch of 2 samples):**
```
Sample 1: [81, 124, 1.44, ..., 0.06] → Actual AQI = 100
Sample 2: [75, 110, 1.20, ..., 0.05] → Actual AQI = 85
```

**Forward Pass:**
```
Sample 1:
  → Hidden Layer 1: 64 neurons compute features
  → Hidden Layer 2: 32 neurons simplify features
  → Output: Predicts 98.5

Sample 2:
  → Hidden Layer 1: 64 neurons compute features
  → Hidden Layer 2: 32 neurons simplify features
  → Output: Predicts 84.2
```

**Calculate Loss:**
```
Sample 1 Error: (100 - 98.5)² = 2.25
Sample 2 Error: (85 - 84.2)² = 0.64
Batch Loss: (2.25 + 0.64) / 2 = 1.445
```

**Backward Pass:**
- Calculate gradient for each weight
- Shows how much each weight contributed to the error

**Update Weights:**
```
For every weight in the network:
  new_weight = old_weight - learning_rate × gradient
```

**Result:**
- Model slightly improves
- Next batch will have better predictions

---

## 🔍 How Loss Decreases Over Time

```
Epoch 1:  Loss = 80 │ ████████░░░░░░ (80% error)
Epoch 10: Loss = 45 │ ███░░░░░░░░░░░ (45% error)
Epoch 50: Loss = 15 │ █░░░░░░░░░░░░░ (15% error)
Epoch 100: Loss = 8 │ ░░░░░░░░░░░░░░ (8% error)
Epoch 150: Loss = 6 │ ░░░░░░░░░░░░░░ (6% error)

Lower loss = Better predictions!
```

---

## 📈 Training vs Validation Loss

```python
history = model.fit(X_train_scaled, y_train, epochs=150, batch_size=32, validation_split=0.2)

# history.history contains:
# - 'loss': Training loss for each epoch
# - 'val_loss': Validation loss for each epoch
```

**Ideal Case:**
```
Both losses decrease and are close:
Epoch 1:   loss=80,  val_loss=82
Epoch 50:  loss=15,  val_loss=15.5
Epoch 150: loss=6,   val_loss=6.5
✅ Good fit!
```

**Overfitting (Bad):**
```
Training loss decreases but validation loss increases:
Epoch 1:   loss=80,  val_loss=82
Epoch 50:  loss=8,   val_loss=20    ⚠️ Gap increasing!
Epoch 150: loss=2,   val_loss=35    ❌ Model memorized, not learning!
```

**Underfitting (Bad):**
```
Both losses stay high:
Epoch 1:   loss=80,  val_loss=82
Epoch 50:  loss=70,  val_loss=72    ⚠️ Not improving much
Epoch 150: loss=65,  val_loss=67    ❌ Model too simple
```

---

## ⚙️ Behind the Scenes: Mathematical Details

### Forward Pass Formula:
```
z1 = W1·X + b1              (Linear combination)
a1 = ReLU(z1)               (Activation)
z2 = W2·a1 + b2             (Linear combination)
a2 = ReLU(z2)               (Activation)
z3 = W3·a2 + b3             (Final linear)
y_pred = z3                 (Output prediction)
```

### Loss Calculation:
```
L = (1/m) * Σ(y_true - y_pred)²

Where m = batch size (32)
```

### Gradient Descent with Adam:
```
m_t = β1 * m_{t-1} + (1 - β1) * g_t        (First moment)
v_t = β2 * v_{t-1} + (1 - β2) * g_t²      (Second moment)
θ_t = θ_{t-1} - α * m_t / (√v_t + ε)      (Parameter update)

Where:
- g_t = gradient
- β1 ≈ 0.9, β2 ≈ 0.999 (Adam constants)
- α = learning rate
```

---

## 🎬 Complete Training Flow

```
START
  ↓
Initialize weights randomly
  ↓
FOR epoch = 1 TO 150:
  │
  ├─ FOR each batch of 32 samples:
  │   ├─ Forward Pass: X_batch → prediction
  │   ├─ Calculate Loss: (y_true - y_pred)²
  │   ├─ Backward Pass: Calculate gradients
  │   ├─ Update Weights: Using Adam optimizer
  │
  ├─ Calculate Training Loss (all training data)
  ├─ Calculate Validation Loss (20% validation data)
  ├─ Display: Epoch 1/150, loss=80.2, val_loss=78.5
  │
END FOR
  ↓
Save model.h5 with final weights
  ↓
END
```

---

## 💡 Why 150 Epochs?

- **Too few epochs (e.g., 10):** Model hasn't learned enough, poor predictions
- **Too many epochs (e.g., 1000):** Overfitting, wastes time, might memorize noise
- **150 epochs:** Sweet spot for this dataset
  - Enough time to learn patterns
  - Not so much that it overfits
  - Loss stabilizes around epoch 100-150

---

## 🧠 Key Concepts

| Concept | Meaning |
|---------|---------|
| **Epoch** | One complete pass through training data |
| **Batch** | Small group of samples (32) |
| **Forward Pass** | Data flows through network to get prediction |
| **Loss** | Measure of prediction error |
| **Backward Pass** | Calculate how to adjust weights |
| **Gradient** | Direction and magnitude to update weights |
| **Adam** | Algorithm that adjusts learning rate automatically |
| **Validation** | Test on separate 20% to check for overfitting |

---

## 📝 After Training

```python
# Model is now trained with 150 epochs of learning
# Weights have been adjusted to minimize AQI prediction error

# What's stored in model:
- W1 (64 neurons weights): Best values found
- b1 (64 neurons biases): Best values found
- W2 (32 neurons weights): Best values found
- b2 (32 neurons biases): Best values found
- W3 (output weights): Best values found
- b3 (output bias): Best values found

# These weights are frozen and used for predictions
```

---

## Conclusion

**Training Summary:**
1. Initialize random weights
2. Show model 32 samples at a time
3. Model makes prediction
4. Calculate how wrong it was
5. Adjust weights to be more correct
6. Repeat for 150 epochs (complete passes through data)
7. Model gradually learns to predict AQI accurately
8. Final weights are saved for future predictions

**Result:** A trained neural network that can predict AQI based on pollutant levels!
