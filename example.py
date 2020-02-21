from model import MLP
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np 
import pandas as pd

def loadData():
    feature_name = ["f_" + str(i) for i in range(162)]
    df_feature = pd.read_table("./data/input_path_data.txt", delimiter="\t", names=feature_name)
    df_label = pd.read_table("./data/input_label.txt", names=['label'])
    df_label = pd.get_dummies(df_label['label'], prefix = 'label')
    return df_feature, df_label

def main():
    # load data
    df_feature, df_label = loadData()
    X_train, X_test, Y_train, Y_test = train_test_split(df_feature, df_label, test_size=0.2, random_state=1)
    Y_train, Y_test = Y_train.to_numpy(), Y_test.to_numpy()
    print("Train:", X_train.shape, Y_train.shape)
    print("Text:", X_test.shape, Y_test.shape)  
    
    #processing data
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform (X_test)
    
    #train model
    clf = MLP(n_hidden=10, n_deep=3, l1_norm=0, drop=0.1, verbose=1, max_epoch=10)
    clf.fit(X_train, Y_train, X_test, Y_test)

if __name__ == '__main__':
    main()
