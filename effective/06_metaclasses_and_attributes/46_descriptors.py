from weakref import WeakKeyDictionary


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


# Implementation
class Grade:
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0-100')
        self._value = value


class Exam:
    # Class attibutes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print('Writing:', first_exam.writing_grade)
print('Science:', first_exam.science_grade)

exam2 = Exam()
exam2.writing_grade = 75
print('And now... still 82?\n', first_exam.writing_grade) # Nope, 75



# Partially Fixed Implementation
class Grade:
    def __init__(self):
        self._values = {}

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0-100')
        self._values[instance] = value


class Exam:
    # Class attibutes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print('Writing:', first_exam.writing_grade)
print('Science:', first_exam.science_grade)

exam2 = Exam()
exam2.writing_grade = 75
print('And now... still 82?\n', first_exam.writing_grade) # Yay!

# ..but leaks memory :(


# Fully Fixed Implementation
class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0-100')
        self._values[instance] = value


class Exam:
    # Class attibutes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print('Writing:', first_exam.writing_grade)
print('Science:', first_exam.science_grade)

exam2 = Exam()
exam2.writing_grade = 75
print('And now... still 82?\n', first_exam.writing_grade) # Yay!
