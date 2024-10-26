import numpy as np

def calculate(calcList):
    if len(calcList) < 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.full((3, 3), [calcList[0:3],calcList[3:6],calcList[6:9]])
    calculations = {
      "mean": [list(np.mean(matrix, axis = 0)), list(np.mean(matrix, axis = 1)), float(np.mean(matrix))],
      "variance": [list(np.var(matrix, axis = 0)), list(np.var(matrix, axis=1)), float(np.var(matrix))],
      "standard deviation": [list(np.std(matrix, axis = 0)), list(np.std(matrix, axis = 1)), float(np.std(matrix))],
      "max": [list(np.max(matrix, axis = 0)), list(np.max(matrix, axis = 1)), int(np.max(matrix))],
      "min":[list(np.min(matrix, axis = 0)), list(np.min(matrix, axis = 1)), int(np.min(matrix))],
      "sum":[list(np.sum(matrix, axis = 0)), list(np.sum(matrix, axis = 1)), int(np.sum(matrix))],
    }
    return calculations