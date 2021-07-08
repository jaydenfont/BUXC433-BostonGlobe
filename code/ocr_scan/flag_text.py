import json

def get_complaint_dict(file):
    # read json file of complaint words
    
    with open(file) as json_file:
        complaint_words = json.load(json_file)
    return complaint_words


def find_categories(complaint_words, complaint):
    complaint = complaint.lower()

    # find which categories the complaint falls under
    categories = []
    for category in complaint_words:
        for word in complaint_words[category]:
            if word in complaint and category not in categories: 
                categories.append(category)

    return categories


if __name__ == "__main__":
    file = 'complaint_words.json'
    complaint_words = get_complaint_dict(file)
    complaint = 'I was Assalted By Agular From D-2 We had Words with each outher and he entered my room and Started hiting me and Kicking me and them outher officer came and Some one sprad me with mace and one of the officer that cuffed me and took me to new man also Asslated me to on the way their'
    categories = find_categories(complaint_words, complaint)
    print(categories)
