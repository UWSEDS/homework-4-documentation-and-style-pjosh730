"""check datatset"""
import pandas as pd
import numpy as np

Dt = pd.read_csv("https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD")

def test_dataframe(frame):
    """check dataset if it has:
    same type for each column;
    there is NaN in each column;
    dataframe has at least one row
    """
#check if the values in each column are right
    for j in range(frame.shape[1]):
        type1 = type(frame.iloc[0, j])
        num = 1
        for i in range(len(frame)):
            if type(frame.iloc[i, j]) != type1:
                num += 1
        if num != 1:
            print('Not correct value in column '+str(frame.columns[j]))
        else:
            print('Value is right in column '+str(frame.columns[j]))

    #check if there is NaN in each column
    for j in range(frame.shape[1]):
        if np.sum(frame.isna()*1)[j] != 0:
            print('There is NaN in column '+ str(frame.columns[j]))
        else:
            print('No NaN in column '+ str(frame.columns[j]))

    # check if the dataframe has at least one row
    if frame.shape[0] >= 1:
        print('The dataframe has at least one row.')
    else:
        print('The dataframe does not have even ONE ROW!')

test_dataframe(Dt)
