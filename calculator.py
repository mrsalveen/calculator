import string
import re

def addition(input: string):
    if input == '':
        return 0
    if len(re.split(',|\n', input)) == 1:
        return int(input)
    arr = [eval(i) for i in re.split(',|\n', input)]
    if all(arr) < 0:
        return Exception

    return sum(arr)
