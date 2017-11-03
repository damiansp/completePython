def accept_command(command, db):
    if action == 'a':
        add_dvd(db)
    elif action =='e':
        edit_dvd(db)
    elif action == 'l':
        list_dvds(db)
    elif action == 'r':
        remove_dvd(db)
    elif action == 'i':
        import_(db)
    elif action == 'x':
        export(db)
    elif action == 'q':
        quit(db)

# ...equivalent to...
def accept_command(command, db):
    commands = dict(a=add_dvd,
                    e=edit_dvd,
                    l=list_dvds,
                    r=remove_dvd,
                    i=import_,
                    x=export,
                    q=quit)
    commands[command](db)



        
