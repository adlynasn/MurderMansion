import re

#simple method - linear search
books = [
    "The man walked the dog", 
    "The lady walked the dog", 
    "Dogs are cool", 
    "Cats are interesting creatures",
    "Cats and Dogs was an interesting movie", 
    "The man has a brown dog",
    "the manner dogma",
    "Time man",
    "Great Gatsby",
    "Fine on the outside",
    "Winter Dream"
]

words = ["fine", "great", "summer", "winter", "day" ,"night" ,"time" ]
results = [x for x in books if all(re.search("\\b{}\\b".format(w), x) for w in words)]
print(results)


#hashing