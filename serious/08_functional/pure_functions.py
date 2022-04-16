def remove_last_item(mylist):
    mylist.pop(-1) # modifies mylist (not functional)


def butlast(mylist):
    return mylist[:-1] # returns a copy (functional approved)


a = [1, 2, 3, 4, 5]
remove_last_item(a)
print(a)  # [1, 2, 3, 4]
b = butlast(a)
print(a)  # [1, 2, 3, 4]

