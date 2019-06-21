def has_5_or_fewer_chars(string):
    return len(string) <= 5


wrapped_function = root.register(has_5_or_fewer_chars)
vcmd = (wrapped_function, '%P') # '%P: Proposed value'
five_char_input = ttk.Entry(root, validate='key', validatecommand=vcmd)


# Alternative
class FiveCharEntry(ttk.Entry):
    '''An Entry that truncates to 5 chars on exit.'''
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(validate='focusout',
                    validatecommand=(self.register(self._validate), '%P'),
                    invalidcommand=(slef.register(self._on_invalid),))

    def _validate(self, proposed_value):
        return len(proposed_value) <= 5

    def _on_invalid(self):
        self.delete(5, tk.END)
