"""This is a very basic patttern search # beginner level  probably I'll try to improve this code or upload a better one"""
from math import exp, log, sqrt
import re

#import the necessary modules
# Count the number of times a pattern appears in a string
string = input("Enter the sentence to search:")
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("Output #38: {0:d}".format(count))
