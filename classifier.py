# -*- coding: utf-8 -*-

import csv

""" Handle Data: Load the data from CSV file and split it into training and test datasets. """


def load_csv(filename):
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [x for x in dataset[i]]
    return dataset


if __name__ == '__main__':
    filename = "./input.csv";
    ds = load_csv(filename)
    print('Loaded data file {0} with {1} rows').format(filename, len(ds))