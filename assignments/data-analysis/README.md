# 📘 Assignment: Data Analysis

## 🎯 Objective

Students will practice end-to-end data analysis in Python: loading a CSV, exploring and cleaning the data, producing summary statistics and visualizations, and reporting key insights.

## ⚙️ Prerequisites

- Basic Python programming (loops, functions)
- Familiarity with `pandas` and `matplotlib` or `seaborn` is helpful but not required
- A Python 3.8+ environment

## 📦 Files Provided

- `data.csv` — dataset to analyze
- `starter-code.py` — minimal starter script to load the data
- `README.md` — (this file) assignment instructions

## ⏱️ Estimated Time

60–90 minutes

## 🧭 Difficulty

Beginner → Intermediate

## 📝 Tasks

### 🛠️ Task 1 — Data Loading & Exploration

#### Description
Load the provided CSV and run exploratory analysis to understand the dataset structure and basic statistics.

#### Requirements
Completed work should:

- Load the CSV using `pandas` (or the standard `csv` module)
- Display the first 5 rows of the dataset
- Report summary statistics for numeric columns (count, mean, std, min, 25%, 50%, 75%, max)
- Note any missing or suspicious values and how you handled them

Deliverable: a script or notebook that prints the above and saves a short `exploration.txt` summary.

### 🛠️ Task 2 — Visualization & Insights

#### Description
Create visualizations to help surface patterns and support at least two specific insights about the data.

#### Requirements

- Produce at least two different plot types (for example, histogram and scatter plot)
- Save plot images to files (e.g., `plot1.png`, `plot2.png`)
- Write a short summary (200–300 words) describing at least two insights discovered and supporting evidence from your plots/statistics

Deliverable: image files for the plots and a short `insights.md` or appended section in `exploration.txt`.

## 💡 Hints

- Use `df.head()` and `df.describe()` for quick exploration
- For missing values: consider `df.dropna()` or `df.fillna()` with a short justification
- Use `matplotlib` or `seaborn` for cleaner visuals; `plt.savefig()` will persist images

## ✅ Submission

1. Update the `starter-code.py` (or add a new script) to perform the tasks
2. Include `exploration.txt` and saved plot images in the same assignment folder
3. Submit by creating a pull request or uploading the folder as instructed by the course

## 🎓 Learning Outcomes

- Load and inspect tabular datasets using `pandas`
- Produce summary statistics and basic data cleaning
- Create and save visualizations to support data-driven insights
- Communicate findings concisely in writing
