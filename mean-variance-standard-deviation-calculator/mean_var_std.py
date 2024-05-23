import numpy as np

def calculate(list):
    testArray = list
    if len(testArray) < 9:
        raise ValueError("List must contain nine numbers.")

    meanList = [testArray.mean(axis=0).tolist(), testArray.mean(axis=1).tolist(), np.mean(testArray.flatten())]
    varList = [testArray.var(axis=0).tolist(), testArray.var(axis=1).tolist(), np.var(testArray.flatten())]
    stdList = [testArray.std(axis=0).tolist(), testArray.std(axis=1).tolist(), np.std(testArray.flatten())]
    minList = [testArray.min(axis=0).tolist(), testArray.min(axis=1).tolist(), np.min(testArray.flatten())]
    maxList = [testArray.max(axis=0).tolist(), testArray.max(axis=1).tolist(), np.max(testArray.flatten())]
    sumList = [testArray.sum(axis=0).tolist(), testArray.sum(axis=1).tolist(), np.sum(testArray.flatten())]
    calculations = {
        'mean' : meanList,
        'variance' : varList,
        'standard deviation' : stdList,
        'max' : maxList,
        'min' : minList,
        'sum' : sumList
    }
    return calculations