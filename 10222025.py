try: # will try to do this, but if it fails...
    pass
except: # it will move to this
    pass

try:
    print("I'm trying") # will print this line, but other languages will not unroll this line
    1/0
except:
    print("divide by 0")

x=5
try:
    x=8
    1/0
except:
    print("divide by 0")
print(x)
#x = 8

x=5
try:
    1/0
    x=8
except:
    print("divide by 0")
print(x)
#x = 5

x=5
try:
    raise Exception("asdf")  # an error notification to the user
    x=8
except ZeroDivisionError:
    print("divide by 0")
except:
    print:("generic error")
print(x)

raise Exception("something went wrong") # Can pick more specific types of errors

import time

def log(msg):
    with open("log.txt", "a") as file: #have to create this text file
        file.write(f"{time.time()} {message}\n") #time.time() number of seconds past since 1-Jan-1970 (Epoch Time)
i=0
while 1:
    time.sleep(1)
    log("message to user") #instead of print, you can log this in the text file for future reference

# I believe he just said that this would create texxt files in codespace, i am still not clear if i need to create the text file first.

#serialization with pickle

import pickle
# serialize (save) data
data = {"name": "Alice", "Scores": [85, 92, 78]}
with open("data.pkl", 'wb') as file: #write in binary, this also created the file for us
    pickle.dump(data, file)

#deserialize (load) data
with open("data.pkl", 'rb') as file: #read in binary
    loaded_data = pickle.load(file)

#swtitch files between python and other languages
import json # you shouldnt write your own json, you should have the PC write it
data = {"name": "Alice", "Scores": [85, 92, 78]}
with open("data.json", 'wb') as file: 
    picklejson.dump(data, file)


with open("data.pkljson", 'rb') as file: 
    loaded_data = json.load(file)
print(loaded_data)


import sqlite3 # structured querry language

conn = sqlite3.connect("users.db") # may or may not create the .db file (daatabase)

cursor.execute("INSERT INTO users (name,age) VALUES (?, ?)"", ("Alice", 25)) # Create table if not exists

#gets really fancy from here dont need to use this in this class. 
