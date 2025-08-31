import numpy as np
arr=np.array([10,20,30,40,50,60,70,110,250])

def outlier_detecction(arr):
    sorted(arr)
    q1,q3=np.percentile(arr,[25,75])
    IQR=q3-q1
    lr=q1-1.5*IQR
    ur=q3+1.5*IQR
    return lr,ur

lr,ur=outlier_detecction(arr)
print(lr,ur)

out_lier=[]
for i in arr:
    if i<lr or i>ur:
        out_lier.append(i)

print(out_lier)
