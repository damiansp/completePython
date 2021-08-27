# The rules of else with for, while, and try
# for: else runs if and when for completes, (but not if aborted with break)
# while: else runs if and when while loop exits bc condition became falsy (but
#        not if aborted with break)
# try: else runs if no exception, return, break, or continue causes control to
#      jump out of main try block
for item in my_list:
    if item.flavor == 'banana':
        break
else:
    raise ValueError('No banana flavor found!')


try:
    dangerous_call()
    after_call()
except OSError:
    log('OSError...')

# Better--keep ONLY potentially error-generating statements in try blocks:
try:
    dangerous_call()
except OSError:
    log('OSError...')
else:
    after_call()

