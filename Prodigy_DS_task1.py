import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample dataset
data = {
    'Gender': np.random.choice(['Male', 'Female', 'Other'], size=100),
    'Age': np.random.normal(loc=30, scale=10, size=100).astype(int)
}
df = pd.DataFrame(data)

# Prepare gender counts
gender_counts = df['Gender'].value_counts()

# Create one figure with two subplots
plt.figure(figsize=(12, 4))

# Bar chart for Gender
plt.subplot(1, 2, 1)
plt.bar(gender_counts.index, gender_counts.values, color='teal')
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')

# Histogram for Age
plt.subplot(1, 2, 2)
plt.hist(df['Age'], bins=10, color='orange', edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Number of People')

# Final layout adjustment
plt.tight_layout()
plt.show()
