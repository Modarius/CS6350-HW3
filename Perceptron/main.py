import os
import pandas as pd
import numpy as np

def importData(filename, column_labels=None, index_col=None, header=None):
    # index_col is a number indicating which column, if any, is the index into the data
    # header is the line of the data if any that where column labels are indicated
    terms = pd.read_csv(filename, sep=',', names=column_labels, index_col=index_col, header=header) # read in the csv file into a DataFrame object , index_col=index_col
    # if needed any processing can be done here
    return terms

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__)) # https://stackoverflow.com/a/5137509
    X_train = importData(dir_path + '/bank-note/train.csv', ['variance', 'skewnes', 'curtosis', 'entropy', 'label'])
    X_test = importData(dir_path + '/bank-note/test.csv', ['variance', 'skewnes', 'curtosis', 'entropy', 'label'])
    return

if __name__ == "__main__":
    main()