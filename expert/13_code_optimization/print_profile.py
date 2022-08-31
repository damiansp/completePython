import cProfile
import pstats

from my_app import main


print('Profiling...')
cProfile.run('main()', 'my_app.stats')
stats = pstats.Stats('my_app.stats')
print('total calls:', stats.total_calls)
stats.sort_stats('time').print_stats(4)

print()
print('medium callees:')
stats.print_callees('medium')

print()
print('light callees:')
stats.print_callees('light')
