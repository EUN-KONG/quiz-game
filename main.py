# 롤 챔피언 퀴즈 게임
# main.py
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question    # 문제
        self.choices = choices      # 보기 리스트
        self.answer = answer        # 정답

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

# 퀴즈 데이터 5개
game = QuizGame()

game.add_quiz(Quiz(
    "정글러가 갱킹을 안 오는 이유는?",
    ["바쁘다", "못 봤다", "캠핑 중이다", "위의 모든 것"],
    4
))
game.add_quiz(Quiz(
    "티모를 보면 적이 제일 먼저 하는 행동은?",
    ["싸운다", "도망간다", "버섯 밟는다", "친구 신청한다"],
    3
))
game.add_quiz(Quiz(
    "야스오가 게임마다 지는 진짜 이유는?",
    ["바람이 없어서", "팀원 탓", "인터넷이 느려서", "철학적 고민 중이라서"],
    2

))
game.add_quiz(Quiz(
    "다음 중 암살자 챔피언은?",
    ["1. 소나", "2. 질리언", "3. 샤코", "4. 소라카"]
    "3"
))
game.add_quiz(Quiz(
    "럭스가 스킬을 쓸 때 항상 외치는 것은?",
    ["어둠이여!", "빛이여!", "제발 맞아라!", "궁 빗나가지 마라!"],
    2
))