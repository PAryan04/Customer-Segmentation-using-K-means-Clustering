# Customer Segmentation Using K-Means Clustering

## Project Overview
This project implements **Customer Segmentation using the K-Means Clustering algorithm** on the Online Retail dataset. The aim is to group customers with similar purchasing behavior into meaningful clusters for business analysis and decision-making.
---

## Objective
The main objectives of this project are:

- Analyze customer purchase behavior
- Segment customers into different groups
- Identify high-value and low-value customers
- Discover popular products in each customer segment
- Visualize customer insights using dashboards

---

## Dataset

Dataset used: **Online Retail Dataset**

Dataset contains attributes such as:

- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- OpenPyXL

---

## Project Workflow

### Step 1: Data Collection
- Load Online Retail dataset from Excel file

### Step 2: Data Preprocessing
- Remove missing CustomerID values
- Create TotalPrice column

Formula:

```
TotalPrice = Quantity × UnitPrice
```

### Step 3: Customer Aggregation

Generate customer-level features:

- TotalQuantity
- Frequency
- TotalSpend

### Step 4: Feature Scaling

Apply StandardScaler for normalization.

### Step 5: K-Means Clustering

Use K-Means algorithm to divide customers into clusters.

Features used:

- TotalQuantity
- Frequency
- TotalSpend

### Step 6: Customer Labeling

Clusters are assigned meaningful names:

1. Big Spenders
2. Frequent Shoppers
3. Low Value Customers
4. Occasional Bulk Buyers

### Step 7: Visualization

Dashboard includes:

- Total Spend Contribution Pie Chart
- Top Products per Customer Segment
- Customer segmentation insights

---

## Output

The project generates:

### Dashboard 1
- Total Spend Contribution by Cluster

### Dashboard 2
- Top Products for Customer Segments

---

## How to Run

### Install dependencies

```bash
pip install pandas matplotlib seaborn scikit-learn openpyxl
```

### Run project

```bash
python project.py
```

---

## Project Structure

```text
Customer-Segmentation-KMeans/
│
├── Online Retail.xlsx
├── project.py
├── README.md
```

---

## Results

The K-Means algorithm successfully segmented customers into meaningful categories:

- Big Spenders → Customers with high spending behavior
- Frequent Shoppers → Customers purchasing regularly
- Low Value Customers → Customers with low spending and activity
- Occasional Bulk Buyers → Customers making large purchases occasionally

These insights can help businesses improve:

- Targeted marketing
- Customer retention
- Product recommendations
- Business decision making
