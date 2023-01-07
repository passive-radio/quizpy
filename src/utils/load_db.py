from object import Question, QuestionDataFrame
import pandas as pd

def _alphabet_to_id(alphabet: str) -> int:
    alphabet = alphabet.lower()
    return ord(alphabet) - 96

def load_db(filepath: str) -> QuestionDataFrame:
    import csv
    
    questions = []
    question_df = pd.DataFrame()
    arr_question = [["id", "question", "answer", "type", "choices", "Question"]]

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
                question.id = i - 1
                if question.type == "4択":
                    question.choices = [row[3], row[4], row[5], row[6]]
                    question.answer = ord(row[2].lower()) - 96
                arr_question.append([question.id, question.question, question.answer, question.type, question.choices, question])
        question_df = QuestionDataFrame(pd.DataFrame(arr_question[1:], columns=arr_question[0]))
    return question_df

if __name__ == "__main__":
    questions = load_db("../data/qa.csv")
    print(questions)