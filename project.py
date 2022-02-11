import pandas as pd
import numpy as np

df=pd.read_csv(r"C:/Users/kanis/OneDrive/Mithun-One drive/OneDrive/Desktop/abc/qwe.csv")
x=df["Coffee"].tolist()
y=df["sleep"].tolist()


data_correletaion=np.corrcoef(x,y)
print(data_correletaion)
