# 롤 챔피언 퀴즈 게임
# main.py
class Quiz:
    def __init__(self, question, answer, choices):
        self.question = question    # 문제
        self.answer = answer        # 정답
        self.choices = choices      # 보기 리스트
    
    def check_answer(self, user_answer):
        return self.answer == user_answer  # 정답 확인

class QuizGame:
    def __init__(self):
        self.score = 0          # 점수
        self.quizzes = []       # 퀴즈 목록
    
    def add_quiz(self, quiz):
        self.quizzes.append(quiz)   # 퀴즈 추가
    
    def run(self):
        print("=== 롤 챔피언 퀴즈 게임 ===")
        for quiz in self.quizzes:
            print(quiz.question)    # 문제 출력