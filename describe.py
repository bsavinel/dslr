import pandas as pd
import numpy as np


def mean(data):
    return sum(data) / data.shape[0]


def std(data, _mean):
    return np.sqrt(sum([(x - _mean)**2 for x in data]) / data.shape[0])


def q1(data):
    fi = (data.shape[0] + 3) / 4 - 1
    ii = int(fi)
    return data[ii] + (data[ii+1] - data[ii]) * (fi - ii)


def median(data):
    fi = (data.shape[0] + 1) / 2 - 1
    ii = int(fi)
    return data[ii] + (data[ii+1] - data[ii]) * (fi - ii)


def q3(data):
    fi = (3 * data.shape[0] + 1) / 4 - 1
    ii = int(fi)
    return data[ii] + (data[ii+1] - data[ii]) * (fi - ii)


def describe(data):
    tab = []
    for i in range(data.shape[0]):
        nonzero_data = np.sort(data[i][~np.isnan(data[i])])
        _count = nonzero_data.shape[0]
        _mean = mean(nonzero_data)
        _std = std(nonzero_data, _mean)
        _min = min(nonzero_data)
        _q1 = q1(nonzero_data)
        _median = median(nonzero_data)
        _q3 = q3(nonzero_data)
        _max = max(nonzero_data)
        tab.append([_count, _mean, _std, _min, _q1, _median, _q3, _max])

    return np.array(tab).transpose()
    


data = pd.read_csv('datasets/dataset_train.csv')

data = data.drop(columns=['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])

# print(data.describe())

dataframe = pd.DataFrame(data=describe(data.to_numpy().transpose()), index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], columns=data.columns)
print(dataframe)