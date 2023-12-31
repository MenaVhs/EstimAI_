import matplotlib.pyplot as plt
from PoseClassification.elbowAlgorithm import *
from GenerateCSV.writeInCSV import import_clusters

n_clusters = 5

# Read the orientations points from Skeleton csv created with DeepLabCut
length_points = dataset_to_list_points(dataset_csv)

# Build and running the model
clustering = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=100, n_init=10)
clustering.fit(length_points)

# Obtaining centroids with its labels
centroids, labels = clustering.cluster_centers_, clustering.labels_
# print(centroids)
# Prediction of 
# prediction = clustering.predict(orientation_points)

dataset_df = pd.read_csv(dataset_csv, header=1)
dataset_df['clustering'] = labels
import_clusters(dataset_df, centroids)


# PCA
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca_orientations = pca.fit_transform(length_points)

# df con dos de los valores de los compoenentes pricipales
pca_lengths_df = pd.DataFrame(data=pca_orientations, columns=['Comp_1', 'Comp_2'])
pca_lengths_names = pd.concat([pca_lengths_df, dataset_df['clustering']], axis=1)
# print(pca_lengths_names)

# Plotting

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Component 1', fontsize=15)
ax.set_ylabel('Component 2', fontsize=15)
ax.set_title('Principal Components', fontsize=20)
# color_theme = np.array(["blue", "green", "orange"])

scatter = ax.scatter(x=pca_lengths_names.Comp_1, y=pca_lengths_names.Comp_2, s=5,
           c=clustering.labels_)

# Add legend
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="upper right", title="Clusters")
ax.add_artist(legend1)
plt.show()
