python3 -m cProfile my_app.py

# or, to generate vis tools:
python3 -m cProfile -o my_app.cprof my_app.py
pyprof2calltree -k -i my_app.cprof
