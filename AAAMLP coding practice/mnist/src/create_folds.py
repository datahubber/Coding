import numpy as np
import pandas as pd
from sklearn import model_selection

if __name__ == "__main__":
    df = pd.read_csv("../input/mnist_train.csv")
    df = df.dropna().reset_index(drop=True)
    df["kfold"] = -1

    df = df.sample(frac=1).reset_index(drop=True)

    kf = model_selection.KFold(n_splits=5, shuffle=True, random_state=42)

    for fold, (trn_, val_) in enumerate(kf.split(X=df)):
        print(len(trn_), len(val_))
        df.loc[val_, 'kfold'] = fold

    df.to_csv("../input/mnist_train_folds.csv", index=False)