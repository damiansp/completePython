def cast_to_list(a):
    cdef list cast_list = <list>a
    print(type(a))
    print(type(cast_list))
    cast_list.append(a)


def safe_cast_to_list(a):
    cdef list cast_list = <list?>a
    print(type(a))
    print(type(cast_list))
    cast_list.append(a)


