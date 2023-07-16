import pandas as pd
from pandasgui import show

file = pd.read_csv('dicttocsv.csv')
gui = show(file)