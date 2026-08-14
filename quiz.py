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