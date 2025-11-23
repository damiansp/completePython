from abc import ABC, abstractmethod


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


class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, name, val):
        pass
