import os

def generateJson(file_path):
    # Geneerate JSON file from simple text
    json_file_path = file_path.replace(".txt", ".json")
    with open(file_path, 'r') as txtfile:
        with open(json_file_path, 'w') as json_file:
            json_file.write("{\n")
            for i, line in enumerate(txtfile):
                if i == 0: continue # Skip header
                rating, question_id, question_title, *_ = line.split("\t")
                json_file.write(f'{{"question_id": "{question_id}", "question_title": "{question_title}", "rating": "{rating}"}},\n')

if __name__ == "__main__":
    current_file_path = os.path.realpath(__file__)
    print(current_file_path)
    generateJson("../static/questionRating.txt")