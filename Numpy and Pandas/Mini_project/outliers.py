import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")
arr = df.select_dtypes(include=[np.number]).to_numpy() 

def outlier_detection(arr):
    outliers = {}
    for col in range(arr.shape[1]):  
        data = arr[:, col]           
        q1, q3 = np.percentile(data, [25, 75])
        IQR = q3 - q1
        lr = q1 - 1.5 * IQR
        ur = q3 + 1.5 * IQR
        
        # find outliers in this column
        col_outliers = data[(data < lr) | (data > ur)]
        outliers[f"Column {col}"] = col_outliers
    
    return outliers

outliers = outlier_detection(arr)
print(outliers)
