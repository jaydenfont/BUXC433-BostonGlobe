import json
import pandas as pd
from dotenv import load_dotenv
import os

def get_complaint_dict(file):
    # read json file of complaint words
    
    with open(file) as json_file:
        complaint_words = json.load(json_file)
    return complaint_words


def find_categories(complaint, complaint_words):
    complaint = complaint.lower()

    # find which categories the complaint falls under
    categories = []
    for category in complaint_words:
        for word in complaint_words[category]:
            if word in complaint and category not in categories: 
                categories.append(category)
    if len(categories) == 0:
        categories.append("None")
    return categories


if __name__ == "__main__":
    file = 'complaint_words.json'
    load_dotenv()
    data = pd.read_csv(os.getenv("FULLSPREADSHEETPATH"))
    complaint_words = get_complaint_dict(file)
    data['misconduct_classifiers'] = data.complaint.apply(find_categories, args=(complaint_words,))
    data.to_csv("data_with_flags.csv")
