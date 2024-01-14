import pandas as pd
import numpy as np

def generate_data(name):
    nr_lt = len(name)
    data = np.random.randint(5, 35, size=nr_lt)
    df = pd.DataFrame(data, columns=['random_numbers'])
    return df
