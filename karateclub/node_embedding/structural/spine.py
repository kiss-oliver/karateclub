import numpy as np
import networkx as nx
import random
from collections import Counter
from karateclub.estimator import Estimator

class spine(Estimator):
    r"""An implementation of `"SPINE" <https://arxiv.org/pdf/1802.03984.pdf>`_
    from the paper "SPINE: Structural Identity Preserved Inductive Network Embedding".

    Args:
        random_walk_number (int): Number of truncated random walks. Default is XXXXX.
        random_walk_length (int): Length of truncated random walks. Default is XXXXXX.
        beta (float): Probability of walking to a neighbor rather than jumping back to origin in RPR generation. Default is XXXXXX.
        k (int): Length of structural feature vector. Default is XXXXXXXXX.
    """
    def __init__(self, random_walk_number, random_walk_length, beta, k):
        self.random_walk_number = random_walk_number
        self.random_walk_length = random_walk_length
        self.beta = beta
        self.k = k

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
        counts = {}
        for node in graph.nodes():
            counts[node] = Counter()
        for truncated_random_walk in self._generate_truncated_random_walks(graph):
            counts[truncated_random_walk[0]].update(truncated_random_walk)
        
        rpr_matrix = []
        rpr_target_nodes = []
        for node in graph.nodes():
            k_most_common = counts[node].most_common(self.k)
            discrepancy = int(len(k_most_common)<self.k)*(self.k-len(k_most_common)) 
            k_most_common_node_id = [x[0] for x in k_most_common] + [node for _ in range(discrepancy)]
            k_most_common_node_frequency = [x[1] for x in k_most_common] + [0 for _ in range(discrepancy)]
            k_most_common_node_frequency = [x/sum(k_most_common_node_frequency) for x in k_most_common_node_frequency]
            rpr_matrix.append(k_most_common_node_frequency)
            rpr_target_nodes.append(k_most_common_node_id)
            
        return rpr_matrix, rpr_target_nodes

    def _get_degrees(self,graph):
        """
        """
        degree_view = graph.degree()
        degrees = [degree for node, degree in degree_view]
        vertices_with_degree_n = {degree:{"vertices":[]} for degree in list(set(degrees))}
        for node, degree in degree_view:
            vertices_with_degree_n[degree]["vertices"].append(node)
        sorted_degrees = list(set(degrees))
        sorted_degrees.sort()
        different_degrees = len(sorted_degrees)
        for i in range(different_degrees):
            if i>0:
                vertices_with_degree_n[sorted_degrees[i]]["previous"] = sorted_degrees[i-1]
            if i<different_degrees-1:
                vertices_with_degree_n[sorted_degrees[i]]["next"] = sorted_degrees[i+1]
        return vertices_with_degree_n, degrees
            

    def fit(self, graph):
        r"""
        Fitting a SPINE model.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be embedded.
        """
        rpr_matrix, rpr_target_nodes = self._get_rooted_page_rank_matrix(graph)
        vertices_with_degree_n, degrees = self._get_degrees(graph)

    def get_embedding(self):
        r"""Getting the node embedding.

        Return types:
            * **embedding** *(Numpy array)* - The embedding of nodes.
        """
        embedding = None
        return embedding
