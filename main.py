# 롤 챔피언 퀴즈 게임
# main.py
class Quiz:
    def __init__(self, question, answer, choices):
        self.question = question    # 문제
        self.answer = answer        # 정답
        self.choices = choices      # 보기 리스트
    
    def check_answer(self, user_answer):
        return self.answer == user_answer  # 정답 확인
