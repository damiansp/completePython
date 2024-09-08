import logic


def main():
    mat = logic.start_game()
    print_mat(mat)
    while True:
        x = input('Press the command:')
        x = x.lower()
        if x not in 'wsad':
            break
        mat, flag = {
            'w': logic.move_up,
            's': logic.move_down,
            'a': logic.move_left,
            'd': logic.move_right
        }[x](mat)
        status = logic.get_current_state(mat)
        if status == 'CONTINUE':
            logic.add_new_2(mat)
        else:
            break
        print_mat(mat)


def print_mat(mat):
    for row in mat:
        for val in row:
            print(f'{val:4d}', end=' ')
        print()
        
        
    
if __name__ == '__main__':
    main()
