from abc import ABC, abstractmethod


def main():
    ctx = Context()
    # 5 + (10 - 3)
    expression = AddExpression(
        NumberExpression(5),
        SubtractExpression(NumberExpression(10), NumberExpression(3)))
    res = expression.interpret(ctx)
    print(res)

    ctx.set_variable('x', 5)
    ctx.set_variable('y', 3)
    # x + 2y
    expr = AddExpression(
        VariableExpression('x'),
        MultiplyExpression(VariableExpression('y'), NumberExpression(2)))
    res = expr.interpret(ctx)
    print(res)
    

class Expression(ABC):
    @abstractmethod
    def interpret(self, ctx):
        pass


class NumberExpression(Expression):
    def __init__(self, n):
        self.n = n

    def interpret(self, ctx):
        return self.n


class AddExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, ctx):
        return self.left.interpret(ctx) + self.right.interpret(ctx)


class SubtractExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, ctx):
        return self.left.interpret(ctx) - self.right.interpret(ctx)


class MultiplyExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, ctx):
        return self.left.interpret(ctx) * self.right.interpret(ctx)


class VariableExpression(Expression):
    def __init__(self, name):
        self.name = name

    def interpret(self, ctx):
        return ctx.get_variable(self.name)


class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, name, val):
        self.variables[name] = val

    def get_variable(self, name):
        return self.variables.get(name, 0)


if __name__ == '__main__':
    main()
