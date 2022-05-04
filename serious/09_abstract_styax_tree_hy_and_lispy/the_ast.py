import ast


print(ast.parse)
print(ast.parse('x = 42'))
print(ast.dump(ast.parse('x = 42')))


print(compile(ast.parse('x = 42'), '<input>', 'exec'))
eval(compile(ast.parse('x = 42'), '<input>', 'exec'))
print(x)


hello = ast.Str(s='Hello, World!', lineno=1, col_offset=1)
print_name = ast.Name(id='print', ctx=ast.Load(), lineno=1, col_offset=1)
print_call = ast.Call(
    func=print_name,
    ctx=ast.Load(),
    args=[hello],
    keywords=[],
    lineno=1,
    col_offset=1)
module = ast.Module(
    body=[ast.Expr(print_call, lineno=1, col_offset=1)],
    lineno=1,
    col_offset=1,
    type_ignores=[])
code = compile(module, '', 'exec')
eval(code)


