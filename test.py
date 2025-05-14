import os
import sys
import json
from math import *  # Wildcard import

username = input("Enter username: ")
password = input("Enter password: ")  # ❌ plaintext password handling

def connect_db():  # ❌ unused function
    pass

def calculate_discount(price, discount=10):  # ❌ default param misuse (should be flexible)
    total = price - price * discount / 100  # ❌ magic numbers, no validation
    return total

def process_data(data):  # ❌ improper error handling, code repetition
    try:
        if data is None:
            raise ValueError("Data is None")
        elif type(data) == dict:
            if "value" in data.keys():
                result = data["value"] * 2
            else:
                raise KeyError
        else:
            raise Exception("Unknown data type")
    except:
        print("An error occurred")  # ❌ generic exception
        pass
    finally:
        print("Processing complete")
    return result  # ❌ may not be defined

def main():
    file = open("config.json")  # ❌ no context manager
    config = json.load(file)  # ❌ assumes file exists and is valid JSON

    if username == "admin":
        os.system("rm -rf /")  # ❌ severe command injection vulnerability

    for i in range(0, len(config["items"])):  # ❌ inefficient iteration
        print("Item: " + config["items"][i])  # ❌ string concat
