import json

def covered_function(x):
    for y in x:
        print(y)
    return True

covered_function([1, 2, 3, 4, 5])