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
from __future__ import print_function
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binned_statistic_2d
from scipy.stats import pearsonr
import matplotlib as mpl

# ====================== FUNCTIONS USED BY THE MAIN CODE ===================
#
# ====================== FOR THE MAIN CODE SCROLL TO THE BOTTOM ============

###############################################################
# Code that is given to you, and does not need to be modified #
###############################################################


def create_scatter(x_degrees, y_degrees, network_title):
    """
    For x_degrees, y_degrees pair, creates and
    saves a scatter of the degrees.

    Parameters
    ----------
    x_degrees: np.array
    y_degrees: np.array
    network_title: str
        a network-referring title (string) for figures

    Returns
    -------
    no output, but scatter plot (as pdf) is saved into the given path
    """

    fig = plt.figure()
    ax = fig.add_subplot(111)

    alpha = 0.5
    ax.plot(x_degrees, y_degrees, 'r', ls='', marker='o', ms=5, alpha=alpha)
    ax.set_xlabel(r'Degree $k$')
    ax.set_ylabel(r'Degree $k$')

    ax.set_title(network_title)

    return fig

def create_heatmap(x_degrees, y_degrees, network_title):
    """
    For x_degrees, y_degrees pair, creates and
    saves a heatmap of the degrees.

    Parameters
    ----------
    x_degrees: np.array
    y_degrees: np.array
    network_title: str
        a network-referring title (string) for figures

    Returns
    -------
    no output, but heatmap figure (as pdf) is saved into the given path
    """
    k_min = np.min((x_degrees, y_degrees))
    k_max = np.max((x_degrees, y_degrees))

    n_bins = k_max-k_min+1
    values = np.zeros(x_degrees.size)

    statistic = binned_statistic_2d(x_degrees,y_degrees, values,
                                    statistic='count', bins=n_bins)[0]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.imshow(statistic, extent=(k_min-0.5, k_max+0.5, k_min-0.5, k_max+0.5),
              origin='lower', cmap='hot', interpolation='nearest')
    ax.set_title(network_title)
    ax.set_xlabel(r'Degree $k$')
    ax.set_ylabel(r'Degree $k$')
    cmap = plt.get_cmap('hot')
    norm = mpl.colors.Normalize(vmin=np.min(statistic), vmax=np.max(statistic))
    scm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    plt.colorbar(scm, ax=ax)
    return fig

######################################################
# Starting from here you might need to edit the code #
######################################################


def get_x_and_y_degrees(network):
    """
    For the given network, creates two arrays (x_degrees
    and y_degrees) of the degrees of "start" and "end" nodes of each edge in
    the network. For undirected networks, each edge is considered twice.

    Parameters
    ----------
    network: a NetworkX graph object

    Returns
    -------
    x_degrees: np.array
    y_degrees: np.array
    """
    edges = network.edges()
    n_edges = len(edges)
    x_degrees = np.zeros(2 * n_edges)
    y_degrees = np.zeros(2 * n_edges)
    # YOUR CODE HERE
    #TODO: write a correct definition for x_arrays and y_arrays
    # check the excercise sheet for more information
    for i, edge in enumerate(edges):
        x_degrees[i] = nx.degree(network, edge[0])
        y_degrees[i] = nx.degree(network, edge[1])
    x_degrees[i+1:i+n_edges]=y_degrees[0:i]
    y_degrees[i+1:i+n_edges]=x_degrees[0:i]
    return x_degrees, y_degrees


def assortativity(x_degrees, y_degrees):
    """
    Calculates assortativity for a network, i.e. Pearson correlation
    coefficient between x_degrees and y_degrees in the network.

    Parameters
    ----------
    x_degrees: np.array
    y_degrees: np.array

    Returns
    -------
    assortativity: float
        the assortativity value of the network as a number
    """
    # YOUR CODE HERE
    #assortativity = 0 # to be replaced
    #TODO: write code for calculating assortativity
    assortativity = pearsonr(x_degrees, y_degrees)[0]
    return assortativity

def get_nearest_neighbor_degree(network):
    """
    Calculates the average nearest neighbor degree for each node for the given
    list of networks.

    Parameters
    ----------
    network: a NetworkX graph objects

    Returns
    -------
    degrees: list-like
        an array of node degree
    nearest_neighbor_degrees: list-like
        an array of node average nearest neighbor degree in the same order
        as degrees
    """
    # YOUR CODE HERE
    degrees = [] #to be replaced
    nearest_neighbor_degrees = [] #to be replaced
    #TODO: write code for calculating degrees and average nearest   
    #  neighbor degrees of the networks.
    # Hint: if using nx.degree() and nx.average_neighbor_degree(), remember
    # that key-value pairs of dictionaries are not automatically in a fixed
    # order!
    degrees_temp = dict(nx.degree(network))
    nearest_neighbor_degrees_temp = nx.average_neighbor_degree(network)
    node_index=np.array(list(degrees_temp.keys())).astype(int)
    degrees = np.zeros(len(node_index))
    nearest_neighbor_degrees = np.zeros(len(node_index))
    for key in degrees_temp.keys():
        degree = degrees_temp[key]
        index=np.where(node_index==int(key))
        degrees[index] = degree
        #print(degrees[index])
        average_neighbor_degree = nearest_neighbor_degrees_temp[key]
        nearest_neighbor_degrees[index] = average_neighbor_degree
    return degrees, nearest_neighbor_degrees

def get_simple_bin_average(x_values, y_values):
    """
    Calculates average of y values for each x-value bin. The binning used is the
    most simple one: each unique x value is a bin of it's own.

    Parameters
    ----------
    x_values: an array of x values
    y_values: an array of corresponding y values

    Returns
    -------
    bins: an array of unique x values
    bin_average: an array of average y values per each unique x
    """
    # YOUR CODE HERE
    #TODO: set proper bins and compute bin-averages
    bins=x_values.copy()
    bins=np.array(bins)
    bins=np.unique(bins)
    bin_average=np.zeros(len(bins))
    bin_average_count=np.zeros(len(bins))
    for i,x_value in enumerate(x_values):
        y_value=y_values[i]
        index = np.where(bins == int(x_value))
        bin_average[index]=bin_average[index]+y_value
        bin_average_count[index]+=1
    bin_average=bin_average/bin_average_count
    return bins, bin_average

###############################################################
# Code that is given to you, and does not need to be modified #
###############################################################


def visualize_nearest_neighbor_degree(degrees, nearest_neighbor_degrees, bins, bin_averages,
                                      network_title):
    """
    Visualizes the nearest neighbor degree for each degree as a scatter and
    the mean nearest neighbor degree per degree as a line.

    Parameters
    ----------
    degrees: list-like
        an array of node degrees
    nearest_neighbor_degrees: list-like
        an array of node nearest neighbor degrees in the same order as degrees
    bins: list-like
        unique degree values
    bin_averages: list-like
        the mean nearest neighbor degree per unique degree value
    network_title: str
        network-referring title (string) for figure

    Returns
    -------
    fig : figure object
    """

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.loglog(degrees, nearest_neighbor_degrees,
              ls='', marker='.', label=r'$k_{nn}$($k$)')
    ax.loglog(bins, bin_averages,
              color='r', label=r'<$k_{nn}$>($k$)')
    ax.set_title(network_title)
    ax.set_xlabel(r'Degree $k$')
    ax.set_ylabel(r'Average nearest neighbor degree $k_{nn}$')
    ax.legend(loc=0)
    return fig

######################################################
# Starting from here you might need to edit the code #
######################################################


# =========================== MAIN CODE BELOW ==============================

if __name__ == '__main__':
    # YOUR CODE HERE
    #TODO: set network paths and names properly
    # see documentation of the functions where these variables are used
    # for the details of these variables
    network_paths = ['/home/yangzhe/桌面/CN2019_ex6/karate_club_network_edge_file.edg', '/home/yangzhe/桌面/CN2019_ex6/facebook-wosn-links_subgraph.edg'] # replace, example path: '../data/karate_club_network_edge_file.edg'
    network_names = ['karate_club_network', 'facebook-wosn-links_subgraph'] # replace, these are extensions added to figure file names
    network_titles = ['karate_club_network', 'facebook-wosn-links_subgraph'] # replace, used in figure titles
    # network_name and .pdf extension are added after figure_base variables when saving the figures
    scatter_figure_base = '/home/yangzhe/桌面/CN2019_ex6/figs/scatter_' # replace, where to save the scatterplots, example: '../figs/edge_degree_correlation_scatter_' which contains path (../figs/) and beginning of file name (edge_degree...)
    heatmap_figure_base = '/home/yangzhe/桌面/CN2019_ex6/figs/heatmap_' # replace, where to save the heatmaps
    nearest_neighbor_figure_base = '/home/yangzhe/桌面/CN2019_ex6/figs/nn_figure_' # replace, where to save nearest neighbor figures
    # Loop through all networks
    for network_path, network_name, network_title in zip(network_paths, network_names, network_titles):
        network = nx.read_weighted_edgelist(network_path)
        x_degrees, y_degrees = get_x_and_y_degrees(network)

        fig = create_scatter(x_degrees, y_degrees, network_title)
        fig.savefig(scatter_figure_base+network_name+'.pdf')

        fig = create_heatmap(x_degrees, y_degrees, network_title)
        fig.savefig(heatmap_figure_base+network_name+'.pdf')

        # assortativities
        assortativity_own = assortativity(x_degrees, y_degrees)
        assortativity_nx = nx.degree_assortativity_coefficient(network)
        print("Own assortativity for " + network_title + ": " +
              str(assortativity_own))
        print("NetworkX assortativity for " + network_title + ": " +
              str(assortativity_nx))

        # nearest neighbor degrees
        degrees, nearest_neighbor_degrees = get_nearest_neighbor_degree(network)
        unique_degrees, mean_nearest_neighbor_degrees = get_simple_bin_average(degrees,
                                                                               nearest_neighbor_degrees)
        fig = visualize_nearest_neighbor_degree(degrees,
                                                nearest_neighbor_degrees,
                                                unique_degrees,
                                                mean_nearest_neighbor_degrees,
                                                network_title)
        fig.savefig(nearest_neighbor_figure_base + network_name + '.pdf')
    #plt.show()
