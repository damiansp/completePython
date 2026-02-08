import re


comment = re.compile(r'/\*(.*?)\*/')
t1 = '/* this is a comment */'
t2 = '''/* this is a
        multiline comment */'''
print(comment.findall(t1))  # [' this is a comment ']
print(comment.findall(t2))  # [] !
ml_comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(ml_comment.findall(t2))  # [' this is a\n        multiline comment ']

