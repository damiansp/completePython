from cProfile import Profile

from my_app import main


profiler = Profile()
profiler.runcall(main)
profiler.print_stats()
