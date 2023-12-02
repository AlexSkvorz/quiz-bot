from dataclasses import dataclass


@dataclass
class UserAnswer:
    quiz_id: int
    completed: int
    score: int
    correct_answer: bool
