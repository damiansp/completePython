class Homework:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, val):
        if not (0 <= val <= 100):
            raise ValueError('Grade must be between 0-100')
        self._grade = val


galileo = Homework()
galileo.grade = 95


class Exam:
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(val):
        if not (0 <= val <= 100):
            raise ValueError('Grade must be between 0-100')

    # bad. requires...
    #@property
    #def writing_grade
    # + setter
    #@property
    # def math_grad + setter... not generalizable or reusable


class Grade:
    def __get__(self, instance, instance_type):
        pass

    def __set__(self, instance, value):
        pass


class Exam:
    # Class attibutes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


exam = Exam()
exam.writing_grade = 40 # interpreted as:
                        # Exam.__dict__['writing_grade'].__set__(exam, 40)
print(exam.writing_grade) # Retrieval:
                          # Exam.__dict__['writing_grade'].__get__(exam, Exam)


    
