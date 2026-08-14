import json
import os

class Quiz:
    """퀴즈 정보를 저장하는 클래스"""
    def __init__(self, question, choices, answer):
        self.question = question    # 문제
        self.choices = choices      # 보기 리스트 (4개)
        self.answer = answer        # 정답 (1~4 숫자)

    def check_answer(self, user_answer):
        """사용자 답이 정답인지 확인"""
        return self.answer == user_answer  # 정답 확인    

    # Quiz 객체를 딕셔너리로 변환 (JSON 저장용)
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    # 딕셔너리에서 Quiz 객체로 변환 (JSON 로드용)
    @staticmethod
    def from_dict(data):
        return Quiz(data["question"], data["choices"], data["answer"])

class QuizGame:
    """퀴즈 게임을 관리하는 클래스"""
    def __init__(self):
        self.score = 0          # 누적 점수
        self.quizzes = []       # 퀴즈 목록 (Quiz 객체들)
        self.state_file = "state.json"  # 저장 파일명
        self.load_state()        # 프로그램 시작 시 저장된 데이터 불러오기
        
    def add_quiz(self, quiz):
        """퀴즈 목록에 새로운 퀴즈 추가"""
        self.quizzes.append(quiz)   # 퀴즈를 리스트에 추가
        self.save_state()  # 퀴즈 추가 후 즉시 저장

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
        
    def get_valid_menu_choice(self):
        """메뉴 선택 입력 (1~5 범위 검증)"""
        while True:
            try:
                # 입력받기
                choice = input("선택: ").strip()
                
                # 빈 입력 확인
                if not choice:
                    print("❌ 선택을 입력해주세요!")
                    continue
                
                # 숫자 변환
                choice_num = int(choice)
                
                # 범위 확인 (1~5)
                if 1 <= choice_num <= 5:
                    return choice_num
                else:
                    print("❌ 1, 2, 3, 4, 5 중에 입력해주세요!")
                    
            except ValueError:
                # 숫자가 아닌 값 입력
                print("❌ 숫자를 입력하세요!")

    def show_menu(self):
        """메인 메뉴 표시 및 사용자 선택 처리"""
        while True:  # 계속 메뉴를 보여주기 위해 무한 루프
            try:
                print("\n" + "="*40)
                print("        🎯 나만의 퀴즈 게임 🎯")
                print("="*40)
                print("1. 퀴즈 풀기")
                print("2. 퀴즈 추가")
                print("3. 퀴즈 목록")
                print("4. 점수 확인")
                print("5. 종료")
                print("="*40)
                
                # 메뉴 선택 (검증된 입력)
                choice = self.get_valid_menu_choice()

                # 사용자 선택에 따라 다른 기능 실행
                if choice == 1:
                    self.run()# 게임 시작
                elif choice == 2:
                    self.add_new_quiz()  # 새 퀴즈 추가
                elif choice == 3:
                    self.show_quiz_list()  # 퀴즈 목록 보기
                elif choice == 4:
                    self.show_score()  # 점수 확인
                elif choice == 5:
                    print("\n게임을 종료합니다! 👋")
                    self.save_state()  # 종료 전 데이터 저장
                    break  # 무한 루프 탈출
                
            except KeyboardInterrupt:
                # Ctrl+C 입력 처리
                print("\n\n⚠️  프로그램이 중단되었습니다.")
                self.save_state()
                print("✅ 데이터가 저장되었습니다.")
                break
            except EOFError:
                # 입력 스트림 종료 처리
                print("\n\n⚠️  입력 스트림이 종료되었습니다.")
                self.save_state()
                print("✅ 데이터가 저장되었습니다.")
                break
    
    def get_valid_answer_input(self):
        """정답 입력 (1~4 범위 검증)"""
        while True:
            try:
                # 입력받기
                answer = input("\n정답 번호를 입력하세요: ").strip()
                
                # 빈 입력 확인
                if not answer:
                    print("❌ 정답을 입력해주세요!")
                    continue
                
                # 숫자 변환
                answer_num = int(answer)
                
                # 범위 확인 (1~4)
                if 1 <= answer_num <= 4:
                    return answer_num
                else:
                    print("❌ 1~4 사이의 숫자를 입력하세요!")
                    
            except ValueError:
                # 숫자가 아닌 값 입력
                print("❌ 숫자를 입력하세요!")

    def add_new_quiz(self):
        """사용자가 직접 새로운 퀴즈를 추가하는 기능"""
        try:
            print("\n=== 새 퀴즈 추가 ===")
            
            # 1단계: 문제 입력받기
            question = input("문제를 입력하세요: ").strip()
            
            # 빈 입력 확인
            if not question:
                print("❌ 문제를 입력해주세요!")
                return
            
            # 2단계: 선택지 4개 입력받기
            choices = []
            for i in range(4):
                while True:
                    choice = input(f"선택지 {i+1}을 입력하세요: ").strip()
                    
                    # 빈 입력 확인
                    if not choice:
                        print("❌ 선택지를 입력해주세요!")
                        continue
                    
                    choices.append(choice)
                    break
            
            # 3단계: 정답 번호 입력받기 (1~4 범위 확인)
            while True:
                try:
                    answer = input("정답 번호(1~4)를 입력하세요: ").strip()
                    
                    # 빈 입력 확인
                    if not answer:
                        print("❌ 정답 번호를 입력해주세요!")
                        continue
                    
                    # 숫자 변환
                    answer_num = int(answer)

                    # 1~4 범위 확인
                    if 1 <= answer_num <= 4:
                        break
                    else:
                        print("❌ 1~4 사이의 숫자를 입력하세요!")
                except ValueError:
                    # 숫자가 아닌 값이 입력되었을 때
                    print("❌ 숫자를 입력하세요!")
            
            # 4단계: 입력받은 정보로 Quiz 객체 생성 후 추가
            self.add_quiz(Quiz(question, choices, answer_num))
            print("✅ 퀴즈가 추가되었습니다!\n")

        except KeyboardInterrupt:
            # Ctrl+C 입력 처리
            print("\n\n⚠️  퀴즈 추가가 중단되었습니다.")
            self.save_state()
            print("✅ 데이터가 저장되었습니다.")
        except EOFError:
            # 입력 스트림 종료 처리
            print("\n\n⚠️  입력 스트림이 종료되었습니다.")
            self.save_state()
            print("✅ 데이터가 저장되었습니다.")

    def show_score(self):
        """현재까지의 누적 점수 표시"""
        print("\n=== 점수 확인 ===")
        print(f"현재 점수: {self.score}점")
        print()

    def run(self): 
        """게임 실행 - 모든 퀴즈를 풀고 점수 계산""" 
        try: 
            # 퀴즈가 없으면 게임 시작 불가 
            if not self.quizzes: 
                print("\n❌ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요!\n") 
                return 
            
            # 게임 시작 메시지 
            print("\n" + "="*40) 
            print(" 🎮 롤 챔피언 퀴즈 게임 시작!") 
            print("="*40 + "\n") 
            
            score = 0 # 이번 게임의 점수 (0부터 시작) 
            
            # 모든 퀴즈를 순서대로 출제 
            # enumerate: 인덱스(i)와 퀴즈(quiz)를 동시에 가져옴 
            for i, quiz in enumerate(self.quizzes): 
                # 문제 출력 (Q1, Q2, ... 형식) 
                print(f"Q{i+1}. {quiz.question}") 
                
                # 보기 목록 출력 (1번부터 시작하려고 j+1 사용) 
                for j, choice in enumerate(quiz.choices): 
                    print(f" {j+1}. {choice}") 
                    
                # 사용자에게 정답 번호 입력받기 (검증된 입력) 
                answer = self.get_valid_answer_input() 
                
                # 입력값과 정답 비교 
                if answer == quiz.answer: 
                    print("✅ 정답입니다!\n") 
                    score += 1 # 정답이면 점수 1 증가 
                else: 
                    print(f"❌ 오답입니다! 정답은 {quiz.answer}번이에요.\n") 
                    
            # 모든 문제가 끝나면 최종 점수 출력 
            self.score += score # 누적 점수에 이번 게임 점수 더하기 
            self.save_state() # 게임 종료 후 점수 저장 
            print("="*40) 
            print(f"🏆 최종 점수: {score}/{len(self.quizzes)}") 
            print("="*40 + "\n") 
            
        except KeyboardInterrupt: 
            # Ctrl+C 입력 처리 
            print("\n\n⚠️ 게임이 중단되었습니다.") 
            self.save_state() 
            print("✅ 데이터가 저장되었습니다.") 
        except EOFError: 
            # 입력 스트림 종료 처리 
            print("\n\n⚠️ 입력 스트림이 종료되었습니다.") 
            self.save_state() 
            print("✅ 데이터가 저장되었습니다.")
            
    # ✨ JSON 파일에 데이터 저장
    def save_state(self):
        """현재 상태(퀴즈, 점수)를 state.json에 저장"""
        state = {
            "score": self.score,
            "quizzes": [quiz.to_dict() for quiz in self.quizzes]
        }
        
        try:
            with open(self.state_file, "w", encoding="utf-8") as f:
                json.dump(state, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"❌ 저장 실패: {e}")

    # ✨ JSON 파일에서 데이터 불러오기
    def load_state(self):
        """state.json에서 저장된 상태를 불러오기"""
        try:
            # 파일이 존재하는지 확인
            if os.path.exists(self.state_file):
                with open(self.state_file, "r", encoding="utf-8") as f:
                    state = json.load(f)
                
                # 저장된 점수와 퀴즈 복원
                self.score = state.get("score", 0)
                self.quizzes = [Quiz.from_dict(q) for q in state.get("quizzes", [])]
                print("✅ 이전 데이터가 로드되었습니다.")
            else:
                print("📝 새로운 게임을 시작합니다.")
            
        except json.JSONDecodeError:
            # JSON 파일이 손상된 경우
            print("⚠️  저장된 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
            self.score = 0
            self.quizzes = []
            self.initialize_default_quizzes()
            
        except Exception as e:
            # 기타 예외 처리
            print(f"⚠️  데이터 로드 실패: {e}. 기본 데이터로 복구합니다.")
            self.score = 0
            self.quizzes = []
            self.initialize_default_quizzes()
            
        def initialize_default_quizzes(self):
            """기본 퀴즈 5개를 초기화하는 메서드 (파일 손상 시 복구용)"""
        
            self.quizzes = [
                Quiz(
                    "정글러가 갱킹을 안 오는 이유는?",
                    ["바쁘다", "못 봤다", "캠핑 중이다", "위의 모든 것"],
                    4
                ),
                Quiz(
                    "티모를 보면 적이 제일 먼저 하는 행동은?",
                    ["싸운다", "도망간다", "버섯 밟는다", "친구 신청한다"],
                    3
                ),
                Quiz(
                    "야스오가 게임마다 지는 진짜 이유는?",
                    ["바람이 없어서", "팀원 탓", "인터넷이 느려서", "철학적 고민 중이라서"],
                    2
                ),
                Quiz(
                    "다음 중 암살자 챔피언은?",
                    ["소나", "질리언", "샤코", "소라카"],
                    3
                ),
                Quiz(
                    "럭스가 스킬을 쓸 때 항상 외치는 것은?",
                    ["빛이여!", "어둠이여!", "제발 맞아라!", "궁 빗나가지 마라!"],
                    1
                )
            ]
            print("✅ 기본 퀴즈 5개가 로드되었습니다.")


if __name__ == "__main__":
    game = QuizGame()
    game.show_menu()