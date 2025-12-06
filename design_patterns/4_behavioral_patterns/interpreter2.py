from abc import ABC, abstractmethod


def main():
    context = DatabaseContext()
    query = SelectExpression('users', EqualCondition('age', 30))
    res = query.interpret


class Expression(ABC):
    @abstractmethod
    def interpret(self, ctx):
        pass


class SelectExpression(Expression):
    def __init__(self, table, condition):
        self.table = table
        self.condition = condition

    def interpret(self, context):
        data = context.get_table(self.table)
        return [row for row in data if self.condition.interpret(row)]


class EqualsCondition(Expression):
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def interpret(self, row):
        return row[self.column] == self.value
    



if __name__ == '__main__':
    main()
