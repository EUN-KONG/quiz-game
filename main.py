class Quiz:
    """퀴즈 정보를 저장하는 클래스"""
    def __init__(self, question, choices, answer):
        self.question = question    # 문제
        self.choices = choices      # 보기 리스트 (4개)
        self.answer = answer        # 정답 (1~4 숫자)

    def check_answer(self, user_answer):
        """사용자 답이 정답인지 확인"""
        return self.answer == user_answer  # 정답 확인    

class QuizGame:
    """퀴즈 게임을 관리하는 클래스"""
    def __init__(self):
        self.score = 0          # 누적 점수
        self.quizzes = []       # 퀴즈 목록 (Quiz 객체들)
    
    def add_quiz(self, quiz):
        """퀴즈 목록에 새로운 퀴즈 추가"""
        self.quizzes.append(quiz)   # 퀴즈를 리스트에 추가

    def show_quiz_list(self):
        """등록된 퀴즈 목록 출력"""
        print("\n=== 퀴즈 목록 ===")
        
        # 퀴즈가 없으면 메시지 출력
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
        else:
            # 모든 퀴즈의 문제만 출력 (번호와 함께)
            for i, quiz in enumerate(self.quizzes):
                print(f"Q{i+1}. {quiz.question}")
        print()

    def show_menu(self):
        """메인 메뉴 표시 및 사용자 선택 처리"""
        while True:  # 계속 메뉴를 보여주기 위해 무한 루프
            print("\n" + "="*40)
            print("        🎯 나만의 퀴즈 게임 🎯")
            print("="*40)
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("="*40)

            choice = input("선택: ")

            # 사용자 선택에 따라 다른 기능 실행
            if choice == "1":
                self.run()  # 게임 시작
            elif choice == "2":
                self.add_new_quiz()  # 새 퀴즈 추가
            elif choice == "3":
                self.show_quiz_list()  # 퀴즈 목록 보기
            elif choice == "4":
                self.show_score()  # 점수 확인
            elif choice == "5":
                print("\n게임을 종료합니다! 👋")
                break  # 무한 루프 탈출
            else:
                print("❌ 1, 2, 3, 4, 5 중에 입력해주세요!")

    def add_new_quiz(self):
        """사용자가 직접 새로운 퀴즈를 추가하는 기능"""
        print("\n=== 새 퀴즈 추가 ===")
        
        # 1단계: 문제 입력받기
        question = input("문제를 입력하세요: ")
        
        # 2단계: 선택지 4개 입력받기
        choices = []
        for i in range(4):
            choice = input(f"선택지 {i+1}을 입력하세요: ")
            choices.append(choice)
        
        # 3단계: 정답 번호 입력받기 (1~4 범위 확인)
        while True:
            try:
                answer = int(input("정답 번호(1~4)를 입력하세요: "))
                # 1~4 범위 확인
                if 1 <= answer <= 4:
                    break
                else:
                    print("❌ 1~4 사이의 숫자를 입력하세요!")
            except ValueError:
                # 숫자가 아닌 값이 입력되었을 때
                print("❌ 숫자를 입력하세요!")
        
        # 4단계: 입력받은 정보로 Quiz 객체 생성 후 추가
        self.add_quiz(Quiz(question, choices, answer))
        print("✅ 퀴즈가 추가되었습니다!\n")

    def show_score(self):
        """현재까지의 누적 점수 표시"""
        print("\n=== 점수 확인 ===")
        print(f"현재 점수: {self.score}점")
        print()

    def run(self):
        """게임 실행 - 모든 퀴즈를 풀고 점수 계산"""
        # 퀴즈가 없으면 게임 시작 불가
        if not self.quizzes:
            print("\n❌ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요!\n")
            return

        # 게임 시작 메시지
        print("\n" + "="*40)
        print("    🎮 롤 챔피언 퀴즈 게임 시작!")
        print("="*40 + "\n")
        
        score = 0  # 이번 게임의 점수 (0부터 시작)
        
        # 모든 퀴즈를 순서대로 출제
        # enumerate: 인덱스(i)와 퀴즈(quiz)를 동시에 가져옴
        for i, quiz in enumerate(self.quizzes):
            # 문제 출력 (Q1, Q2, ... 형식)
            print(f"Q{i+1}. {quiz.question}")
            
            # 보기 목록 출력 (1번부터 시작하려고 j+1 사용)
            for j, choice in enumerate(quiz.choices):
                print(f"  {j+1}. {choice}")
            
            # 사용자에게 정답 번호 입력받기
            answer = input("\n정답 번호를 입력하세요: ")
            
            # 입력값과 정답 비교
            # input()은 문자열이므로 str()로 변환해서 비교
            if answer == str(quiz.answer):
                print("✅ 정답입니다!\n")
                score += 1  # 정답이면 점수 1 증가
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번이에요.\n")
        
        # 모든 문제가 끝나면 최종 점수 출력
        self.score += score  # 누적 점수에 이번 게임 점수 더하기
        print("="*40)
        print(f"🏆 최종 점수: {score}/{len(self.quizzes)}")
        print("="*40 + "\n")

# 프로그램 시작 지점
if __name__ == "__main__":
    # QuizGame 객체 생성
    game = QuizGame()

    # 기본 퀴즈 데이터 추가
    game.add_quiz(Quiz(
        "정글러가 갱킹을 안 오는 이유는?",
        ["바쁘다", "못 봤다", "캠핑 중이다", "위의 모든 것"],
        4  # 정답: 4번
    ))
    game.add_quiz(Quiz(
        "티모를 보면 적이 제일 먼저 하는 행동은?",
        ["싸운다", "도망간다", "버섯 밟는다", "친구 신청한다"],
        3  # 정답: 3번
    ))
    game.add_quiz(Quiz(
        "야스오가 게임마다 지는 진짜 이유는?",
        ["바람이 없어서", "팀원 탓", "인터넷이 느려서", "철학적 고민 중이라서"],
        2  # 정답: 2번
    ))
    game.add_quiz(Quiz(
        "다음 중 암살자 챔피언은?",
        ["소나", "질리언", "샤코", "소라카"],
        3  # 정답: 3번
    ))
    game.add_quiz(Quiz(
        "럭스가 스킬을 쓸 때 항상 외치는 것은?",
        ["어둠이여!", "빛이여!", "제발 맞아라!", "궁 빗나가지 마라!"],
        2  # 정답: 2번
    ))

    # 메뉴 실행 (게임 시작)
    game.show_menu()