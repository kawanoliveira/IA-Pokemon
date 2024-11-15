import pandas as pd
import os
import classes

relative_path = os.path.join(os.path.dirname(__file__),"atk.csv")


for i in range(166):
    linha_desejada = pd.read_csv(relative_path, sep=';', skiprows=lambda x: x != i, nrows=1, header=None)
    ataque = classes.Attack(*linha_desejada.values[0])
    print(ataque)
