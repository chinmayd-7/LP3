
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA

# 1. Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# 2. Select important numeric columns
X = df[["QUANTITYORDERED", "PRICEEACH", "SALES", "MSRP"]].dropna()

# 3. Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Find optimal clusters using Elbow Method
wcss = []

for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    wcss.append(model.inertia_)

# Plot Elbow Graph
plt.plot(range(1, 11), wcss, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# 5. Select number of clusters
k = 3

# 6. Apply K-Means Clustering
km = KMeans(n_clusters=k, random_state=42, n_init=10)
kmeans_labels = km.fit_predict(X_scaled)

# 7. Apply Hierarchical Clustering
hc = AgglomerativeClustering(n_clusters=k, linkage="ward")
hierarchical_labels = hc.fit_predict(X_scaled)

# 8. Reduce dimensions for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 9. Display both clustering results
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans_labels)
plt.title("K-Means Clustering")

plt.subplot(1, 2, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=hierarchical_labels)
plt.title("Hierarchical Clustering")

plt.tight_layout()
plt.show()

print("Number of clusters:", k)
print("K-Means clustering completed.")
print("Hierarchical clustering completed.")
