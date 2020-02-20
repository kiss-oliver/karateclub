import numpy as np
import networkx as nx
import random
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

    def _generate_single_truncated_random_walk(self, graph, source_node):
        r"""Generates a single truncated random walk given a graph and a source node.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph for which the rooted page rank matrix is generated.  
            * **source_node** *(int)* - The index of the source node.  

        Return types:
            * **truncated_random_walk** *(list)* - A list of node indices in the random walk.    
        """
        truncated_random_walk = [source_node]        
        for previous_node_index in range(self.random_walk_length-1):
            if random.random()>=self.beta:
                truncated_random_walk.append(source_node)
            else:
                truncated_random_walk.append(random.choice(list(graph[truncated_random_walk[previous_node_index]].keys())))
        return truncated_random_walk

    def _generate_truncated_random_walks(self, graph):
        r"""Generator for truncated random walks on a graph.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph for which the rooted page rank matrix is generated.  
        """
        print(graph)
        for _ in range(self.random_walk_number):
            for node_i in graph.nodes():
                truncated_random_walk = self._generate_single_truncated_random_walk(graph, node_i)
                yield truncated_random_walk


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
        pass

    def get_embedding(self):
        r"""Getting the node embedding.

        Return types:
            * **embedding** *(Numpy array)* - The embedding of nodes.
        """
        embedding = None
        return embedding
