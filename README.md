# ⚽ Footylytics Football Stats Analyzer

A data-driven football statistics project that uses **FBref** datasets to explore player and team performances.  
The goal is to clean, analyze, and visualize football data to uncover meaningful insights for fans, analysts, and researchers.  

---

## 📊 Features
- 📥 Import structured data from **FBref** (players, teams, seasons)  
- 🧹 Data cleaning & preprocessing for consistency  
- 📈 Generate descriptive stats (goals, assists, xG, passing accuracy, etc.)  
- 📊 Visualize trends (heatmaps, bar plots, scatter plots)  
- 🔎 Compare players, teams, and seasons with custom queries  

---

## 📂 Dataset
The dataset comes from [FBref](https://fbref.com/en/), powered by **StatsBomb** and **Sports Reference**.  

**Examples of available stats:**
- **Player-level**: Goals, Assists, xG, xA, Passing %, Progressive Carries  
- **Team-level**: Possession %, Shots per Game, Goals Against, Pressing Efficiency  
- **Season/match aggregates**  

---

## 🛠️ Tech Stack
- **Python**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`  
- **Jupyter Notebook** or **Streamlit** for analysis and dashboards  
- **FBref dataset** (scraped/exported CSVs)  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/football-stats-analyzer.git
cd football-stats-analyzer
