import pandas as pd
import numpy as np
import random

# 1. Load the original transaction file
original_data = pd.read_csv("original_transactions.csv")

# 2. Define the DP synthetic data function
def dp_synthetic_binary(df, epsilon=1.0):
    """
    Apply Differential Privacy using randomized response to binary transaction data.
    df: pandas DataFrame with binary columns (0/1)
    epsilon: privacy budget
    """
    # probability of keeping the real value
    p = np.exp(epsilon) / (np.exp(epsilon) + 1)
    
    synthetic_df = df.copy()
    for col in df.columns:
        if col == "ID":
            continue
        for i in range(len(df)):
            if random.random() > p:
                # Flip the bit (0 becomes 1, 1 becomes 0)
                synthetic_df.at[i, col] = 1 - df.at[i, col]
    
    return synthetic_df

# 3. Generate the synthetic DP dataset
synthetic_data = dp_synthetic_binary(original_data, epsilon=0.8)

# 4. Save or view the result
synthetic_data.to_csv("synthetic_transactions.csv", index=False)
