'''
This module uses the Viterbi algorithm to allow for fuzzy matching used to match
typos to the best match in a set of candidates by selecting the candidate with
the least distance from the input (or None if distance > max_dist threshold). 
'''
import numpy as np

'''
Class for determining the edit distance between pairs of strings, that is, the 
number of edits (insertions, deletions, or substitutions) needed to convert one
string to the other.

This can be used for fuzzy matching (e.g., of a string and a set of candidates,
as well as for text alignment (e.g. in DNA sequence alignment)
'''
class EditDistance():
    # Default costs are "Levenstein distance" -- insertions and deletion are
    # penalized as 1; substitutions are 2, equivalent to an insertion and a
    # deleiton
    def __init__(self, word1, word2, sub_cost=2, add_cost=1, del_cost=1):
        self.word1 = [c for c in '#' + word1]
        self.word2 = [c for c in '#' + word2]
        self.n1 = len(self.word1)
        self.n2 = len(self.word2)
        self.costs = {'sub': sub_cost,
                      'del': del_cost,
                      'add': add_cost}
        self.steps = {'dia': np.array([-1, -1]),
                      'non': np.array([-1, -1]),
                      'sub': np.array([-1, -1]),
                      'add': np.array([ 0, -1]), 
                      'del': np.array([-1,  0])}
        self._create_matrices()
        self.get_cost()

    def set_words(self, *words):
        self.word1 = [c for c in '#' + words[0]]
        self.word2 = [c for c in '#' + words[1]]
        self.n1 = len(self.word1)
        self.n2 = len(self.word2)
        self._create_matrices()
        self.cost = self.get_cost()

    def get_cost(self):
        try:
            return self.cost
        except AttributeError:
            self.cost = self.matrix[self.n1 - 1, self.n2 - 1]
            return self.cost

    def print_matrix(self):
        if self.matrix is None:
            self.matrix = self._create_matrix()
        print(self.matrix)

    def align(self):
        out1 = ''
        out2 = ''
        self.actions = self._get_action_seq()
        for a in self.actions:
            if a in ['fin', 'sub', 'non']:
                out1 += self.word1.pop(0)
                out2 += self.word2.pop(0)
            elif a == 'add':
                out1 += '-'
                out2 += self.word2.pop(0)
            else:
                out1 += self.word1.pop(0)
                out2 += '-'
        self.alignment = (out1[1:], out2[1:]) # omit initial '#'
        print('%s\n%s' % (out1[1:], out2[1:]))

    def print_seq(self):
        print(self.actions[1:])

    def _create_matrices(self):
        self.matrix = self._init_matrix()
        self.action_matrix = np.array(['unk'] * self.n1 * self.n2)\
                               .reshape([self.n1, self.n2])
        self.action_matrix[0, :] = ['fin'] + ['add'] * (self.n2 - 1)
        self.action_matrix[:, 0] = ['fin'] + ['del'] * (self.n1 - 1)
        for i in range(1, self.n1):
            for j in range(1, self.n2):
                (self.matrix[i, j],
                 self.action_matrix[i, j]) = self._get_cell_value(i, j)

    def _init_matrix(self):
        matrix = np.zeros([self.n1, self.n2])
        matrix[:, 0] = range(self.n1)
        matrix[0, :] = range(self.n2)
        return matrix

    def _get_cell_value(self, i, j):
        prev_cells = self._get_prev_cells(i, j)
        min_prev = prev_cells['dia']
        optimal_action = 'dia'
        for cell in ['add', 'del']:
            if prev_cells[cell] < min_prev:
                min_prev = prev_cells[cell]
                optimal_action = cell
        diag_action = 'non' if self.word1[i] == self.word2[j] else 'sub'
        diag_cost = 0 if diag_action == 'non' else self.costs['sub']
        values = {'dia': prev_cells['dia'] + diag_cost,
                  'del':  prev_cells['del']  + self.costs['del'],
                  'add':  prev_cells['add']  + self.costs['add']}
        min_value = values['dia']
        for cell in ['add', 'del']:
            val = values[cell]
            if val < min_value:
                min_value = val
        if optimal_action == 'dia':
            optimal_action = diag_action
        return min_value, optimal_action

    def _get_prev_cells(self, i, j):
        cells = {}
        for step, action in self.steps.items():
            prev_loc = np.array([i, j]) + action
            cells[step] = self.matrix[prev_loc[0], prev_loc[1]]
        return cells

    def _get_action_seq(self):
        i, j = self.n1 - 1, self.n2 - 1
        action = self.action_matrix[i, j]
        action_seq = [action]
        while action != 'fin':
            i += self.steps[action][0]
            j += self.steps[action][1]
            action = self.action_matrix[i, j]
            action_seq.append(action)
        return action_seq[::-1]


def match_fuzzy(found, candidates, max_dist=np.inf, verbose=False, **kwargs):
    '''
    Find the best match for a string <found> given a list of potential 
    candidates, or return <found> as is if all distances > <max_dist>
    
    Args:
    found (str): the string to match on (e.g., containing a typo)
    candidates (list<str>): list of strings to potentially match on
    max_dist (real): the maximum edit distance allowable to match on
    kwargs: additional params to pass EditDistance.__init__() (costs)
    '''
    best_cost = np.inf
    best_match = []
    if verbose:
        print(found)
    for candidate in candidates:
        ed = EditDistance(found.lower(), candidate.lower(), **kwargs)
        cost = ed.get_cost()
        if verbose:
            print(f'  -> {candidate}: {cost}')
        if cost == best_cost:
            best_match.append(candidate)
        if cost < best_cost:
            best_cost = cost
            best_match = [candidate]            
    if best_cost > max_dist:
        print('info', f'No match found within max_dist: {max_dist}')
        return found
    return best_match
