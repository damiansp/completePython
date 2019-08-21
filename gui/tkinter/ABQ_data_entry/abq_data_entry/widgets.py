class ValidatedMixin:
    '''Adds validation functionality to an input widget'''
    def __init__(self, *args, error_var=None, **kwargs):
        self.error = error_var or tk.StringVar()
        super().__init__(*args, **kwargs)
        vcmd = self.register(self._validate)
        invcmd = self.register(self._invalid)
        self.config(validate='all',
                    validatecommand=(vcmd, '%P', '%s', '%S', '%V', '%i', '%d'),
                    invalidcommand=(invcmd, '%P', '%s', '%S', '%V', '%i', '%d'))

    def trigger_focusout_validation(self):
        valid = self._validate('', '', '', 'focusout', '', '')
        if valid:
            return valid
        self._focusout_invalid(event='focusout')

    def _toggle_error(self, on=False):
        self.config(foreground=('red' if on else 'black'))

    def _validate(self, proposed, current, char, event, index, action):
        self._toggle_error(False)
        self.error.set('')
        valid = True
        if event == 'focusout':
            valid = self._focusout_validate(event=event)
        elif event == 'key':
            valid = self._key_validate(proposed=proposed,
                                       current=current,
                                       char=char,
                                       event=event,
                                       index=index,
                                       action=action)
        return valid

    def _focusout_validate(self, **kwargs):
        return True

    def _key_validate(self, **kwargs):
        return True

    def _invalid(self, proposed, current, char, event, index, action):
        if event == 'focusout':
            self._focusout_invalid(event=event)
        elif event == 'key':
            self._key_invalid(proposed=proposed,
                              current=current,
                              char=char,
                              event=event,
                              index=index,
                              action=action)

    def _focusout_invalid(self, **kwargs):
        self._toggle_error(True)

    def _key_invalid(self, **kwargs):
        pass


# Validation Codes
# %S: For in/del, the text being inserted/deleted (key events only)
# %i: The index (0-based) of the text being inserted/deleted, or -1 on non-key
#     events (passed as STRING)
# %V: The event that triggered validation (focusin, focusout, key, forced;
#     indicating that the text variable was changed)
# %d: Action being attempted: 0: delete, 1: insert, -1: other (as STRING)
class DateEntry(ttk.Entry):  # DateInput ??
    '''An Entry for ISO-style dataes (YYYY-MM-DD)'''
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(
            validate='all',
            validatecommand=(
                # _validate receives insertion (%S), index of insertion (%i),
                # type of event (%V) and action performed (%d)
                self.register(self._validate), '%S', '%i', '%V', '%d'),
            # _on_invalid gets type of event
            invalidcommand=(self.register(self._on_invalid), '%V'))
        self.error = tk.StringVar()

    def _toggle_error(self, error=''):
        self.error.set(error)
        if error:
            self.config(foreground='red')
        else:
            self.config(foreground='black')

    def _validate(self, char, index, event, action):
        # reset error state
        self._toggle_error()
        valid = True
        if event == 'key':
            if action == '0': # Delete: should always validate
                valid = True
            elif index in '01235689':
                valid = char.isdigit()
            elif index in '47':
                valid = char == '-'
            else:
                valid = False
        elif event == 'focusout':
            try:
                datetime.strptime(self.get(), '%Y-%m-%d')
            except ValueError:
                valid = False
        return valid

    def _on_invalid(self, event):
        if event != 'key':
            self._toggle_error('Not a valid date')

    def _key_validate(self, action, index, char, **kwargs):
        valid = True
        if action == '0':
            valid = True
        if index in '01235689':
            valid = char.isdigit()
        elif index in '47':
            valid = char == '-'
        else:
            valid = False
        return valid
                                
    def _focusout_validate(self, event):
        valid = True
        if not self.get():
            self.error.set('A value is required')
            valid = False
        try:
            datetime.strptime(self.get(), '%Y-%m-%d')
        except ValueError:
            self.error.set('Invalid date')
            valid = False
        return valid
