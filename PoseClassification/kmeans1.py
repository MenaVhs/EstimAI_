import matplotlib.pyplot as plt
from PoseClassification.elbowAlgorithm import *

n_clusters = 3

# Read the orientations points from Skeleton csv created with DeepLabCut
length_points = dataset_to_list_points(dataset_csv)

# Build and running the model
clustering = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=100, n_init=10)
clustering.fit(length_points)

# Obtaining centroids with its labels
centroids, labels = clustering.cluster_centers_, clustering.labels_

# Prediction of 
# prediction = clustering.predict(orientation_points)

dataset_df = pd.read_csv(dataset_csv, header=1)
dataset_df['clustering'] = labels

# print(dataset_df)


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
ax.set_xlabel('Componente 1', fontsize=15)
ax.set_ylabel('Componente 2', fontsize=15)
ax.set_title('Componentes Principales', fontsize=20)
color_theme = np.array(["blue", "green", "orange"])
ax.scatter(x=pca_lengths_names.Comp_1, y=pca_lengths_names.Comp_2, s=5,
           c=clustering.labels_)
plt.show()
