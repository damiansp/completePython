import ast  # abstract syntax tree


hello_world = 'def hello_world(): print("Hello, World!")'
tree = ast.parse(hello_world)
print(tree)
print(ast.dump(tree))
