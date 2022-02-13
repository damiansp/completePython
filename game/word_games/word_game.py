import json
import sys

import numpy as np


NOT_TRIED   = GREY   = '\033[47m'
RIGHT       = GREEN  = '\033[42m'
WRONG_SPOT  = ORANGE = '\033[43m'
NOT_IN_WORD = RED    = '\033[41m'
RESET       = BLACK  = '\033[40m'
DATA = './data'


def main():
    print('Word game time!')
    choice = input('Enter to begin or 1 to change settings: ')
    if choice == 1:
        wordlen, turns = choose_settings()
    else:
        wordlen = 5
        turns = 6
    game = WordGame(wordlen, turns)
    display_color_coding()
    game.play_game()


def choose_settings():
    turns = input('Maximum number of attempts: ')
    wordlen = 5 # maybe add more later...
    return wodlen, turns


def display_color_coding():
    print('#=====================#')
    print('|    Color Coding:    |')
    print_color('|      Not Tried      |', NOT_TRIED)
    print_color('|       Correct       |', RIGHT)
    print_color('| In word, wrong spot |', WRONG_SPOT)
    print_color('|    Not in word      |', NOT_IN_WORD)
    print('#=====================#')
    
    
def print_color(txt, color, **kwargs):
    print(color + txt + RESET, **kwargs)
    
    
class WordGame:
    def __init__(self, wordlen=5, turns=6):
        self.wordlen = wordlen
        self.turns = turns
        self.letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        with open(f'{DATA}/wordlist_{wordlen}letter.json', 'r') as f:
            self.vocab = json.load(f)
        self.stats = self._load_stats()

    def _load_stats(self):
        try:
            with open(f'{DATA}/stats.json', 'r') as f:
                stats = json.load(f)
        except FileNotFoundError:
            stats = {f'{self.wordlen}_letter': {}}
        return stats

    def play_game(self):
        turns = self.turns
        self.status = {letter: NOT_TRIED for letter in self.letters}
        self.answer = self._get_random_word()
        while turns:
            turns = self._play_turn(turns)
        self._end()

    def _get_random_word(self):
        word = np.random.choice(self.vocab, 1)[0]
        if len(word) != self.wordlen:
            print('Bad word in vocab:', word)
            self._ger_random_word()
        return word

    def _play_turn(self, turns):
        word = input(f'\nEnter a {self.wordlen}-letter word: ')
        if not self._is_valid(word):
            return self._play_turn(turns)
        letters = list(word.upper())
        self._update_game_status(letters)
        self._display(letters)
        if word.lower() == self.answer.lower():
            n_turns = self.turns - turns + 1
            s = 's' if n_turns > 1 else ''
            print(f'You got it in {n_turns} turn{s}!')
            self.stats[f'{self.wordlen}_letter'][str(n_turns)] = (
                self.stats[f'{self.wordlen}_letter'].get(str(n_turns), 0) + 1)
            self._end()
        turns -= 1
        return turns

    def _is_valid(self, word):
        if len(word) != self.wordlen:
            print(f'Word is not {self.wordlen} letters.')
            return False
        if len(word) != len(set(word)):
            print('Each letter may only occur once')
            return False
        if word.upper() not in self.vocab:
            print('Word not recognized')
            return False
        return True

    def _update_game_status(self, letters):
        for i, letter in enumerate(letters):
            if letter in self.answer:
                if letter == self.answer[i]:
                    self.status[letter] = RIGHT
                else:
                    self.status[letter] = WRONG_SPOT
            else:
                self.status[letter] = NOT_IN_WORD

    def _display(self, letters):
        for i, letter in enumerate(letters):
            end = '\n' if i == self.wordlen - 1 else ''
            self._display_letter(letter, end=end)
        print()
        self._display_status()

    def _display_letter(self, letter, **kwargs):
        print_color(f' {letter} ', self.status[letter], **kwargs)
        
    def _display_status(self):
        for i, letter in enumerate(self.status.keys()):
            end = '\n' if (i + 1) % 10 == 0 else ''
            self._display_letter(letter, end=end)
        print()

    def _end(self):
        print('The answer was:', self.answer)
        self._show_stats()
        play_again = input('Play again? (y/n): ')
        if play_again.lower() == 'y':
            self.play_game()
        elif play_again.lower() == 'n':
            self._save_stats()
            sys.exit()
        else:
            print('Command not understood.')
            self._end()

    def _show_stats(self):
        stats = self.stats[f'{self.wordlen}_letter']
        print('Turns | Freq')        
        for turns in sorted([int(k) for k in stats.keys()]):
            print(f'{turns:<6d}| {stats[str(turns)]}')
        print()

    def _save_stats(self):
        with open(f'{DATA}/stats.json', 'w') as f:
            json.dump(self.stats, f)


if __name__ == '__main__':
    main()

    
