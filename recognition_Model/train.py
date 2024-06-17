import numpy as np
import argparse
import os
from PIL import Image

# I know that regression is wrong algorithm but I don't have a time to implement a proper one, hence, used this.
# Correct one would be DL Dense network which would have softmax outputs for probabilistic claculations of front 9 digits and back
# 99 digits and sum them them up, maybe using Keras
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

def train(train, epoches=1000, learning_rate=0.001):

    global model
    
    X_train = []
    Y_train = []
    for file in os.listdir('./train'):
        img = Image.open('./train/'+file)
        ndarray = np.array(img)
        X_train.append(ndarray)
        Y_train.append(file[:-4] if not file[:-4].endswith(")") else file[:-7])

    model = LogisticRegression(max_iter=epoches)
    model.fit(X_train, Y_train)


if __name__ == '__main__':
    parser = argparse.ArgumentParser() 
    parser.add_argument('-p','--path', type=str)
    args = vars(parser.parse_args())
    path = args['path']
    f = open(path, "r")
    lines = f.readlines()
    train_path = ""
    validation_path = ""
    epoches = 1000
    lr = 0.001
    for line in lines:
        if line.startswith("train"):
            train_path = line.split(":")[1]
        if line.startswith("validation"):
            validation_path = line.split(":")[1]
        if line.startswith("lr"):
            lr = line.split(":")[1]
        if line.startswith("epoches"):
            epoches = line.split(":")[1]

    train(train=train_path,epoches=epoches)


    

