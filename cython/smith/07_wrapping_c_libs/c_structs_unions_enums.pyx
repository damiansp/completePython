cdef extern from 'header_name':
    struct struct_name:
        struct_members

    union union_name:
        union_members

    enum enum_name:
        enum members


# for typedef-ed versions
cdef extern from 'header_name':
    ctypedef struct strcut_alias:
        struct_members

    # etc


