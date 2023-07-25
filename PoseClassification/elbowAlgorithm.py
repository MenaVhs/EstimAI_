import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

LOOPS = 11
MAX_ITERATIONS = 10
INITIALIZE_CLUSTERS = 'k-means++'
CONVERGENCE_TOLERANCE = 0.001
NUM_THREADS = 12
dataset_csv = r'C:\Users\mena_\OneDrive - Centro de Enseñanza LANIA\Escritorio\EstimAI_\CSV\20230719 100Cm 3S RecortadoDLC_resnet50_EstimAIJul6shuffle1_180000_skeleton.csv'

def dataset_to_list_points(dataset_csv):
    data = pd.read_csv(dataset_csv, header=1)
    length = np.array(data.loc[:, data.columns.str.startswith('length')])
    return length


def plot_results(inertials):
    x, y = zip(*[inertia for inertia in inertials])
    plt.plot(x, y, 'ro-', markersize=8, lw=2)
    plt.grid(True)
    plt.title('Elbow Method')
    plt.xlabel('Num Clusters')
    plt.ylabel('Inertia')
    plt.show()


def select_clusters(dataset_csv, loops, max_iterations, init_cluster, tolerance,
                    num_threads):
    # Read data set
    points = dataset_to_list_points(dataset_csv)

    inertia_clusters = list()

    for i in range(1, loops + 1, 1):
        # Object KMeans
        kmeans = KMeans(n_clusters=i, max_iter=max_iterations,
                        init=init_cluster, tol=tolerance, verbose=num_threads)

        # Calculate Kmeans
        kmeans.fit(points)

        # Obtain inertia
        inertia_clusters.append([i, kmeans.inertia_])

    plot_results(inertia_clusters)


if __name__ == '__main__':


    select_clusters(dataset_csv, LOOPS, MAX_ITERATIONS, INITIALIZE_CLUSTERS,
                    CONVERGENCE_TOLERANCE, NUM_THREADS)

