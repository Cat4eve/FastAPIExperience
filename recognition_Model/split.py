from PIL import Image  
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = []
Y = []

for file in os.listdir('./train'):
    img = Image.open('./train/'+file)
    img = img.resize((300, 300))
    ndarray = np.array(img)
    X.append(ndarray)
    Y.append(file[:-4])
    for _ in range(3):
        img = img.rotate(90)
        ndarray = np.array(img)
        X.append(ndarray)
        Y.append(file[:-4])
    

X = np.array(X)
Y = np.array(Y)


X_train, X_val, Y_train, Y_val = train_test_split(X,Y,test_size=0.2)
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_val = scaler.fit_transform(X_val)

for i in range(len(X_train)):
    im = Image.fromarray(np.uint8(X_train[i])).convert('RGB')
    im.save(f'./training/{Y_train[i]}.JPG')
for i in range(len(X_val)):
    im = Image.fromarray(np.uint8(X_val[i])).convert('RGB')
    im.save(f'./testing/{Y_val[i]}.JPG')

