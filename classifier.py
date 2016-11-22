# -*- coding: utf-8 -*-
import csv
import random
import math

""" Handle Data: Load the data from CSV file and split it into training and test datasets. """


def load_csv(filename):
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [x for x in dataset[i]]
    return dataset


def split_data_set(ds, split_ratio):
    train_size = int(len(ds) * split_ratio)
    train_set = []
    copy = list(ds)
    while len(train_set) < train_size:
        index = random.randrange(len(copy))
        train_set.append(copy.pop(index))
    return [train_set, copy]


""" Summarize Data: """

" Separate Data By Class "


def separate_by_class(data_set):
    separated = {}
    for i in range(len(data_set)):
        vector = data_set[i]
        if vector[0] not in separated:
            separated[vector[0]] = []
        separated[vector[0]].append(vector)
    return separated


" Calculate Mean "


def mean(numbers):
    return sum(numbers) / float(len(numbers))


" Calculate Standard Deviation "


def sd(numbers):
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)


""" Summarize Dataset """


def summarize(data_set):
    summaries = [(mean(attribute), sd(attribute)) for attribute in zip(*data_set)]
    del summaries[-1]
    return summaries

    # Make a Prediction: Use the summaries of the dataset to generate a single prediction.
    # Make Predictions: Generate predictions given a test dataset and a summarized training dataset.
    # Evaluate Accuracy: Evaluate the accuracy of predictions made for a test dataset as the percentage correct out of all predictions made.
    # Tie it Together: Use all of the code elements to present a complete and standalone implementation of the Naive Bayes algorithm.


if __name__ == '__main__':
    filename = "./input.csv";
    ds = load_csv(filename)
    print('Loaded data file {0} with {1} rows').format(filename, len(ds))

    splitRatio = 0.67
    train, test = split_data_set(ds, splitRatio)
    print('Split {0} rows into train with : \n{1} and test with :\n{2}').format(len(ds), train, test)

    separated = separate_by_class(ds)
    print('Separated instances: {0}').format(separated)