# In order to understand how the code works, it is a good idea to check the
# final section of the file that starts with
#   if __name__ == '__main__'
#
# Your task is essentially to replace all the parts marked as TODO or as
# instructed through comments in the functions, as well as the filenames
# and labels in the main part of the code which can be found at the end of
# this file.
#
# The raise command is used to help you out in finding where you still need to
# write your own code. When you successfully modified the code in that part,
# remove the `raise` command.
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def sample_nodes(g, p):
    """
    Obtains a sampled network via Bernoulli node sampling.
    For each node in g, sample it with probability p, and add edge (i, j) only if both nodes i and j have been sampled.

    Parameters
    ----------------
    g: a networkx graph object
    p: sampling probability for each node
    """

    # Initialize empty network
    g_new = nx.empty_graph()

    ###TIP: #TODO: Write code for sampling. Iterate over nodes, and add to g_new with probability p
    ###TIP: #TODO add edges if both nodes in an edge have been observed.

    # YOUR CODE HERE
    return g_new


def sample_edges(g, p):
    """
    Obtains a sampled network via Bernoulli edge sampling.
    For each edge in g, sample it with probability p

    Parameters
    ----------------
    g: a networkx graph object
    p: sampling probability for each edge
    """

    # Initialize empty network
    g_new = nx.empty_graph()

    # TODO: Write code for sampling. Iterate over edges, and add to g_new with probability p
    # YOUR CODE HERE
    return g_new

def sample_stars(g, p):
    """
    Obtains a sampled network via star sampling.
    We sample nodes with probability p, and observe all neighbors. Returns a g_new network obtained via star sampling, and also a list of the nodes that were directly sampled from g, not only sampled via observing a sampled neighbor.
    Parameters
    ----------------
    g: a networkx graph object
    p: sampling probability for each edge
    """

    # Initialize empty network
    g_new = nx.empty_graph()
    nodes = []
    # TODO: Write code for sampling. Iterate over edges, and add to g_new with probability p
    # YOUR CODE HERE
    return g_new, nodes


def count_twostars(g, nodes=None):
    """
    Counts the number of two stars in a graph

    Parameters
    ------------------
    g: a networkx graph object
    nodes: if nodes is not None, a list of sampled nodes under the star-sampling scheme.

    """
    n_two_stars = 0
    # TODO: Replace this. The line "if not nodes" is True when nodes=None, this is for node and edge sampling
    if not nodes:
        two_stars = []
    else:
    # TODO: Replace this. If nodes is a list of sampled nodes, count the two-stars centered on these sampled nodes.
        two_stars = []

    # YOUR CODE HERE
    return n_two_stars


def count_triangles(g):
    """
    Counts the number of triangles in a graph

    Parameters
    ------------------
    g: a networkx graph object
    """
    triangles = []
    n_triangles = 0
    ### TIP: #TODO: count the number of triangles in a graph.
    # YOUR CODE HERE
    return n_triangles


def transitivity(n_triangles, n_twostars):
    """
    Returns the plug-in estimator for global transitivity given the number of triangles and number of triples connected by two edges

    Parameters
    ---------------------
    triples: int
    triangles: int
    """
    transitivity = 0.
    ###TIP: #TODO: Write the plug-in estimator for transitivity given the estimators for 2-stars and triangles
    # YOUR CODE HERE
    return transitivity


def horvitz_thompson(obs_values, pi):
    """
    Returns the Horvitz-Thompson Estimator

    Parameters
    --------------------
    obs_values: int or float, observed values from a sampled network
    pi: float, observation probability
    """
    ht = 0.
    ###TIP: #TODO Write the HT estimato.
    # YOUR CODE HERE
    return ht


def ht_node_probabilities(p):
    """
    Given the probability of sampling a node, returns the probabilities of sampling two-stars and triangles

    Parameters
    ---------------------
    p: float
    """
    pi_twostars = 0
    pi_triangles = 0
    ###TIP: #TODO write the probabilites of sampling twostars and triangles under node sampling
    # YOUR CODE HERE
    return pi_twostars, pi_triangles


def ht_edge_probabilities(p):
    """
    Given the probability of sampling an edge, returns the probabilities of sampling two-stars and triangles

    Parameters
    ---------------------
    p: float
    """
    pi_twostars = 0
    pi_triangles = 0
    ###TIP: #TODO write the probabilites of sampling twostars and triangles under edge sampling
    # YOUR CODE HERE
    return pi_twostars, pi_triangles


def ht_star_probabilities(p):
    """
    Given the probability of sampling a star, returns the probabilities of sampling two-stars and triangles

    Parameters
    ---------------------
    p: float
    """
    pi_twostars = 0
    pi_triangles = 0
    ###TIP: #TODO write the probabilites of sampling twostars and triangles under star-sampling
    # YOUR CODE HERE
    return pi_twostars, pi_triangles


def ht_estimators(g, p, n_samp, sampling_type, empirical=False):
    """
    Function for obtaining n_samp samples from a network g and returning the HT estimates, given a sampling type and sampling probabilty p.
    Returns three lists of n_samp, where each list contains HT estimates for transitivity and
    number of two-stars, where the sampling.

    Parameters
    ------------------------
    g: a networkx network
    p: float, sampling probability
    n_samp: int, number of samples to obtain
    sampling_type: str, either 'nodes', 'edges' or 'stars'
    empirical: bool, if True, then do not use HT estimators
    """
    transitivity_estimates = []
    triangles_estimates = []

    for i in range(n_samp):

        if sampling_type == 'nodes':
            g_new = sample_nodes(g, p)
            nodes = None
            pi_twostars, pi_triangles = ht_node_probabilities(p)

        elif sampling_type == 'edges':
            g_new = sample_edges(g, p)
            nodes = None
            pi_twostars, pi_triangles = ht_edge_probabilities(p)

        elif sampling_type == 'stars':
            g_new, nodes = sample_stars(g, p)
            pi_twostars, pi_triangles = ht_star_probabilities(p)
        else:
            raise ValueError("Invalid sampling_type, must be either 'nodes', 'edges' or 'stars'")
        ### TIP: #TODO: Count the statistics, build the HT estimators, plug-in for transitivity and save sampled value
        ### TIP: #TODO: if empirical = True, simply do not use HT estimators
        # YOUR CODE HERE

    return transitivity_estimates, triangles_estimates


def plot_histograms(n_samp, sampling_type, p_empirical=.5):
    """
    Plot exercise histograms for a number of samples n_samp and a sampling_type (nodes, edges or stars).
    """

    fig = plt.figure(figsize=(8, 5))
    probabilities = [ .3, .5]

    estimator_name_triangles = r'$\hat{\tau}^' + sampling_type[0] + r'_{\bigtriangleup}$'
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_title('Estimators for triangles sampling {}, '.format(sampling_type) + estimator_name_triangles)
    ax1.set_xlabel(estimator_name_triangles)

    estimator_name_transit = r'$\hat{\tau}^' + sampling_type[0] + r'_C$'
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_title('Estimators for transitivity sampling {}, '.format(sampling_type) + estimator_name_transit)
    ax2.set_xlabel(estimator_name_transit)

    #Plot HT estimates for different probabilities
    for p in probabilities:
        transit_est, triangles_est = ht_estimators(g, p, n_samp, sampling_type)
        ax1.hist(triangles_est, 30, alpha=.5, density=True, label='p = {}'.format(p))
        ax2.hist(transit_est, 30, alpha=.5, density=True, label='p = {}'.format(p))

    #Obtain empirical estimates
    transit_est, triangles_est = ht_estimators(g, p_empirical, n_samp, sampling_type, empirical=True)
    ax1.hist(triangles_est, 30, alpha=.5, density=True, label='p_empirical = {}'.format(p_empirical))
    ax2.hist(transit_est, 30, alpha=.5, density=True, label='p_empirical = {}'.format(p_empirical))

    # Plot real values
    ax1.axvline(n_triangles, color='r') # n_triangles as obtained for the full network
    ax2.axvline(transit, color='r') # transit as obtained for the full network

    ax1.legend(loc=0)
    ax2.legend(loc=0)
    fig.tight_layout()
    fig.savefig('ht_estimator_sampling_{}.pdf'.format(sampling_type))

#  ===================== MAIN CODE BELOW =======================

if __name__ == '__main__':

    # Generate network
    g = nx.relaxed_caveman_graph(200, 10, .1)
    # e)
    # Empirical estimators for sampling nodes
# Empirical estimators for sampling nodes
    probabilites = [.1, .3, .5, 1]
    print(' --------- Sampling nodes ---------')
    print('p  |  triangles | two-stars | transitivity | ')
    for p in probabilites:
        if p == 1:
            g_new = g
        else:
            g_new = sample_nodes(g, p)

        n_triangles = count_triangles(g_new)
        n_twostars = count_twostars(g_new)
        transit = transitivity(n_triangles, n_twostars)
        print('%2.2f  |  %7d  |  %7d  |  %4.4f  |' % (p, n_triangles, n_twostars, transit))
    print('....................................')
    print(' --------- Sampling edges ----------')
    print('p  |  triangles | two-stars | transitivity | ')
    for p in probabilites:
        if p == 1:
            g_new = g
        else:
            g_new = sample_edges(g, p)
        n_triangles = count_triangles(g_new)
        n_twostars = count_twostars(g_new)
        transit = transitivity(n_triangles, n_twostars)
        print('%2.2f  |  %7d  |  %7d  |  %4.4f  |' % (p, n_triangles, n_twostars, transit))

    print('....................................')
    print(' --------- Star sampling ----------')
    print('p  |  triangles | two-stars | transitivity | ')
    for p in probabilites:
        if p == 1:
            g_new = g
            nodes = None
        else:
            g_new, nodes = sample_stars(g, p)
        n_triangles = count_triangles(g_new)
        n_twostars = count_twostars(g_new, nodes)
        transit = transitivity(n_triangles, n_twostars)
        print('%2.2f  |  %7d  |  %7d  |  %4.4f  |' % (p, n_triangles, n_twostars, transit))

    # f)# Histograms for node sampling
    n_samp = 100
    plot_histograms(n_samp, 'nodes')

    # Histograms for edge sampling
    n_samp = 100
    plot_histograms(n_samp, 'edges')

    # Histograms for star sampling
    n_samp = 100
    plot_histograms(n_samp, 'stars', p_empirical=.5)

