import sys

sys.path.append('../')
from ..object import QuestionDataFrame

class World():
    def __init__(self) -> None:
        pass
    
    def add_question_df(self, question_df:QuestionDataFrame):
        self.question_df = question_df