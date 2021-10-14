from typing import Any
import numpy as np
import pandas as pd


def reachable(g, x: str, z: set[str]) -> set[str]:
    '''
    Get all nodes reachable from node X in graph g, given obervations z
    Args:
      g (matrix-like): adjacency representation of the graph
      x (str): name of node in graph
      z (set[str]): set of observed nodes
    '''
    # Insert all ancestors of Z into A




if __name__ == '__main__':
    # Test
    # W ->\
    #      Y ->\
    # Z ->/     X
    #  \------>/
    G = pd.DataFrame([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0]],
                     columns=list('WXYZ'),
                     index=list('WXYZ'))
