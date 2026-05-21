import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# -------------------------------
# Load and Preprocess Data
# -------------------------------
df = pd.read_excel(r"E:\College Files\dwdm project\k-means\Online Retail.xlsx", engine="openpyxl")
df = df.dropna(subset=['CustomerID'])
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

customer_df = df.groupby('CustomerID').agg({
    'Quantity': 'sum',
    'InvoiceNo': 'count',
    'TotalPrice': 'sum'
}).reset_index()

customer_df.rename(columns={
    'InvoiceNo': 'Frequency',
    'Quantity': 'TotalQuantity',
    'TotalPrice': 'TotalSpend'
}, inplace=True)

# -------------------------------
# K-Means Clustering
# -------------------------------
X = customer_df[['TotalQuantity', 'Frequency', 'TotalSpend']]
X_scaled = StandardScaler().fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
customer_df['Cluster'] = kmeans.fit_predict(X_scaled)

cluster_labels = {
    0: "Big Spenders",
    1: "Frequent Shoppers",
    2: "Low Value Customers",
    3: "Occasional Bulk Buyers"
}
customer_df['ClusterLabel'] = customer_df['Cluster'].map(cluster_labels)

# -------------------------------
# DASHBOARD 1 — PIE CHART ONLY
# -------------------------------
plt.figure(figsize=(10, 10))
sns.set_style("whitegrid")

spend_per_cluster = customer_df.groupby('ClusterLabel')['TotalSpend'].sum()

# Pie chart with direct labels
wedges, texts, autotexts = plt.pie(
    spend_per_cluster,
    labels=spend_per_cluster.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette("Set2"),
    pctdistance=0.85
)

# Bold main title
plt.title("Customer Segmentation Dashboard\nTotal Spend Contribution by Cluster",
          fontsize=18, fontweight='bold', pad=20)

# Improve text readability
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)

plt.tight_layout()
plt.show()

# -------------------------------
# DASHBOARD 2 — BAR CHARTS (2x2 GRID, NO AXIS LABELS)
# -------------------------------
sns.set_style("whitegrid")
clusters_to_plot = [0, 1, 2, 3]  # All clusters

fig, axs = plt.subplots(2, 2, figsize=(18, 12))  # 2x2 grid
axs = axs.flatten()  # flatten for easy iteration

for idx, cluster in enumerate(clusters_to_plot):
    cluster_customers = customer_df[customer_df['Cluster'] == cluster]['CustomerID']
    cluster_data = df[df['CustomerID'].isin(cluster_customers)]
    top_products = cluster_data['Description'].value_counts().head(5)

    ax = axs[idx]
    bars = sns.barplot(x=top_products.values, y=top_products.index, palette="Set2", ax=ax)
    
    # Remove axis labels
    ax.set_xlabel("")
    ax.set_ylabel("")
    
    ax.set_title(f"Top 5 Products - {cluster_labels[cluster]}", fontsize=13)

    # Add bar labels
    for bar in bars.patches:
        width = bar.get_width()
        ax.text(width + 2, bar.get_y() + bar.get_height()/2, f'{int(width)}', va='center')

# Bold main title for dashboard 2
plt.suptitle("Customer Segmentation Dashboard\nTop Products per Cluster",
             fontsize=18, fontweight='bold', y=0.95)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()
