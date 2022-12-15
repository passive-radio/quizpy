from dataclasses import dataclass

@dataclass
class Question:
    question: str = ""
    answer: str = ""
    choices: list = ""
    type: str = ""
    
@dataclass
class QuestionBox:
    content: list[Question]