python3 -m cProfile palindrome1.py # output res to stdout
#python3 -m cProfile -o palindrome1_prof.pstat palindrome1.py # save to file

# if saving to file:
#python3 -m pstats palindrome1_prof.pstat  # opens pstat browser
# > help
# > stats [5] # same as output above
# > sort [colname]
# > quit

#pip3 install snakeviz
#snakeviz palindrome.pstat
