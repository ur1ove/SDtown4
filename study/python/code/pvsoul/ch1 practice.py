# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 01:01:04 2019

@author: pc
"""

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
%matplotlib inline
movie = pd.read_csv('data/movie.csv')
movie.head()
"""

"""
import csv
filename = 'movie.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movie = pd.read_csv('movie.csv')    

movie.dtypes

# print(movie.dtypes)

movie.get_dtype_counts()

print(movie.get_dtype_counts())




