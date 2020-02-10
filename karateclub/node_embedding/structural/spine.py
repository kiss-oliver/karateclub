import numpy as np
import networkx as nx
from karateclub.estimator import Estimator

class spine(Estimator):
    r"""An implementation of `"SPINE" <https://arxiv.org/pdf/1802.03984.pdf>`_
    from the paper "SPINE: Structural Identity Preserved Inductive Network Embedding".

    Args:
        sample_number (int): Number of evaluation points. Default is 200.
        step_size (float): Grid point step size. Default is 0.1.
        heat_coefficient (float): Heat kernel coefficient. Default is 1.0.
        approximation (int): Chebyshev polynomial order. Default is 100.
        mechanism (str): Wavelet calculation method 'exact' or 'approximate'. Default is 'approximate'.
        switch (int): Vertex cardinality when the wavelet calculation method switches to approximation. Default is 1000.
    """
    def __init__(self):

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
