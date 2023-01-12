from dataclasses import dataclass
import pandas as pd

@dataclass
class Question:
    question: str = ""
    id: int = 0
    answer: str = ""
    choices: list = None
    type: str = ""
    
@dataclass
class QuestionBox:
    content: list[Question]
    
@dataclass
class QuestionDataFrame:
    """
    columns = ["id", "question", "answer", "type", "choices"]
    keys:
    id: user defined index of each questions. you have to give index when load_db loads data.
    question: question sentences of each question class.
    answer: answer of each questio class
    type: Question type of each question instances
    choices: choices of question, by default None.
    """
    content: pd.DataFrame()
    # origin_content: pd.DataFrame()