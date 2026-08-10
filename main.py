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

    def run(self):
        print("=== 롤 챔피언 퀴즈 게임 ===\n")
        score = 0  # 점수를 저장하는 변수, 처음엔 0점
        
        # enumerate: 문제 번호(i)와 문제(quiz)를 동시에 가져옴
        for i, quiz in enumerate(self.quizzes):
            print(f"Q{i+1}. {quiz.question}")  # Q1, Q2... 형식으로 문제 출력
            
            # 보기 목록 출력 (1번부터 시작하려고 j+1 사용)
            for j, choice in enumerate(quiz.choices):
                print(f"  {j+1}. {choice}")
            
            # 사용자에게 정답 번호 입력받기
            answer = input("\n정답 번호를 입력하세요: ")
            
            # 입력값과 정답 비교 (input은 문자열이라 str()로 변환해서 비교)
            if answer == str(quiz.answer):
                print("✅ 정답입니다!\n")
                score += 1  # 정답이면 점수 1 증가
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번이에요.\n")
        
        # 모든 문제가 끝나면 최종 점수 출력
        print(f"=== 최종 점수: {score}/{len(self.quizzes)} ===")

if __name__ == "__main__":
    game = QuizGame()

    # 퀴즈 데이터 추가
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
        ["소나", "질리언", "샤코", "소라카"],
        3
    ))
    game.add_quiz(Quiz(
        "럭스가 스킬을 쓸 때 항상 외치는 것은?",
        ["어둠이여!", "빛이여!", "제발 맞아라!", "궁 빗나가지 마라!"],
        2
    ))

    game.run() # 게임 실행