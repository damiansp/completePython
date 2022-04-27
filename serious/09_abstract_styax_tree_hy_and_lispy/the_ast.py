import ast


print(ast.parse)
print(ast.parse('x = 42'))
print(ast.dump(ast.parse('x = 42')))
