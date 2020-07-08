import re
import fileinput
from datetime import datetime, timedelta

z = input("Please enter the full name of your file: ")
s = input("Please enter the number of seconds, positive or negative, that you would like to add to the times: ")


def add_seconds(x, fmt="%H:%M:%S,%f", seconds=int(s)):
    return (datetime.strptime(x, fmt) +
            timedelta(seconds=seconds)).strftime(fmt)


pattern = r"(\b(?:\d\d:){2}\d\d,\d\d\b)"

with fileinput.FileInput(z, inplace=True) as f:
    for line in f:
        replacement = lambda x: add_seconds(x.group(0))[:11]
        print(re.sub(pattern, replacement, line), end="")
