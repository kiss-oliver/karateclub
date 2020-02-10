import numpy as np
import networkx as nx
from karateclub.estimator import Estimator

class spine(Estimator):
    r"""An implementation of `"SPINE" <https://arxiv.org/pdf/1802.03984.pdf>`_
    from the paper "SPINE: Structural Identity Preserved Inductive Network Embedding".

    Args:
        random_walk_number (int): Number of truncated random walks. Default is XXXXX.
        random_walk_length (int): Length of truncated random walks. Default is XXXXXX.
        beta (float): Probability of walking to a neighbor rather than jumping back to origin in RPR generation. Default is XXXXXX.
    """
    def __init__(self, random_walk_number, random_walk_length, beta):
        self.random_walk_number = random_walk_number
        self.random_walk_length = random_walk_length
        self.beta = beta
        pass


    def _get_rooted_page_rank_matrix(self, graph):
        r"""Generating a rooted page rank matrix

        Arg types:
            * **graph** *(NetworkX graph)* - The graph for which the rooted page rank matrix is generated.    

        Return types:
            * **rpr_matrix** *(Numpy array)* - The rooted page rank matrix.    
        """
        rpr_matrix = None
        return rpr_matrix


    def fit(self, graph):
        r"""
        Fitting a SPINE model.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be embedded.
        """
        self._get_rooted_page_rank_matrix(graph)
        pass

    def get_embedding(self):
        r"""Getting the node embedding.

        Return types:
            * **embedding** *(Numpy array)* - The embedding of nodes.
        """
        embedding = None
        return embedding
