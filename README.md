# 🏀 NBA Shooting Trends Analysis 📊

## 📌 Overview
This project analyzes NBA shooting trends from the **2000-01 season to the 2023-24 season**, focusing on:
- 🎯 The shift from two-point to three-point attempts.
- 📈 Effective Field Goal Percentage (eFG%).
- 🔥 The ratio of three-point attempts to total field goal attempts.
- 📊 The relationship between 3P Attempt Ratio and eFG% using regression analysis.

Each program in this repository handles **one specific analysis and visualization** to ensure clarity and modularity.

---

## ⚙️ Installation & Requirements
### **📦 Required Libraries**
Make sure you have the following Python libraries installed before running the scripts:

```sh
pip install pandas matplotlib seaborn statsmodels nba_api
```

### **🌐 NBA API Setup**
The scripts use the **NBA API** to fetch data. Ensure that you have an active internet connection.

---

## 📂 File Descriptions
Each file corresponds to a specific analysis:

### **1. `two_vs_three_attempts.py`**
- 📊 Fetches and plots **two-point vs. three-point attempts per season**.
- 🎯 Visualizes the growing preference for three-pointers.
- 📈 Saves and displays a line graph.

### **2. `efg_percentage.py`**
- 📊 Computes and plots **Effective Field Goal Percentage (eFG%)** over seasons.
- 📈 Helps in understanding overall shooting efficiency.
- 🎯 Displays a trend line of eFG%.

### **3. `three_point_ratio.py`**
- 📊 Calculates and plots the **ratio of three-point attempts to total field goal attempts**.
- 🔥 Demonstrates the NBA’s increasing reliance on three-pointers.
- 📈 Displays a trend line of 3P Attempt Ratio.

### **4. `regression_analysis.py`**
- 📊 Analyzes the relationship between **3P Attempt Ratio and eFG%**.
- 📉 Uses **Ordinary Least Squares (OLS) regression** to determine correlation.
- 📈 Prints a regression summary and plots a regression graph.

---

## 🚀 How to Run the Scripts
Each script is **standalone** and can be run independently:

```sh
python two_vs_three_attempts.py
python efg_percentage.py
python three_point_ratio.py
python regression_analysis.py
```

The scripts will fetch data, process it, and generate the corresponding visualization.

---

## ⚠️ Notes & Considerations
- 🔄 Data is fetched **directly from the NBA API**, which may have occasional downtime.
- ⏳ A **1-second delay** is added between API calls to prevent rate limits.
- 📉 Some seasons may have **missing or incomplete data** due to API limitations.
- 📊 The regression analysis assumes a linear relationship between 3P Attempt Ratio and eFG%.

---

## 🔮 Future Enhancements
- 🤖 Add more advanced machine learning models to predict future shooting trends.
- 🏀 Explore per-team shooting data instead of league-wide averages.
- ⚡ Improve API request efficiency by caching data locally.

---

## 👨‍💻 Author
Developed for **NBA analytics enthusiasts and data science practitioners** interested in basketball trends and statistical analysis.

**Happy Analyzing! 🏀📊**

