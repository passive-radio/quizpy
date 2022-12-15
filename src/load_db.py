from object import Question, QuestionBox

def _alphabet_to_id(alphabet: str) -> int:
    alphabet = alphabet.lower()
    return ord(alphabet) - 96

def load_db(filepath: str) -> QuestionBox:
    import csv
    
    questions = []
    reader = None
    with open(filepath, encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i < 1:
                pass
            else: 
                question = Question()
                question.question = row[0]
                question.type = row[1]
                question.answer = row[2]
                if question.type == "4択":
                    question.choices = [row[3], row[4], row[5], row[6]]
                    question.answer = ord(row[2].lower()) - 96
                questions.append([question])
    return QuestionBox(questions)


if __name__ == "__main__":
    questions = load_db("../data/qa.csv")
    print(questions)