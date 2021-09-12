import pandas as pd
# openpyxl is required by pandas. Make sure you installed it
# in your environment
# import openpyxl
from lxml import etree
import numpy as np

tree = etree.parse("matrix.xml")

indexes = []
root = tree.getroot()
matrix = root[0]
matrix_values = {}
for entry in matrix:
    indexes.append(entry.get('base'))
    matrix_values[entry.get('base')] = []
    for e in entry:
        matrix_values[entry.get('base')].append(e.text)


indexes.sort()

zeros = np.zeros((len(indexes), len(indexes)))

my_df = pd.DataFrame(zeros, columns=indexes, index=indexes)

for row, columns in matrix_values.items():
    for column in columns:
        my_df.at[row, column] = 1

my_df.to_excel("matrix.xlsx", sheet_name="Matrix")

