# Week 7 Data Visualization Notes

## 1. Line Plot (Weekly Average Attendance)

- **Analytical Question:** How does average student attendance change over the 6-week period?
- **Observations:**
  1. Attendance starts at 78% in Week 1 and rises steadily to 85% by Week 6.
  2. A minor dip occurs between Week 3 (81%) and Week 4 (79%) before recovering.
- **Interpretation:** Overall student engagement shows a positive upward trend over time across the weeks.
- **Limitation:** Aggregated weekly averages mask individual student variations and course-specific attendance patterns.

---

## 2. Scatter Plot (Attendance vs. Final Marks)

- **Analytical Question:** Is there a relationship between student attendance percentages and their final exam marks?
- **Observations:**
  1. Data points cluster upward from left to right across the plot.
  2. Higher attendance values generally align with higher final mark scores.
- **Interpretation:** There is a clear positive association between student attendance and final performance.
- **Limitation:** Scatter plots show correlation, not causation; higher attendance alone does not prove attendance directly caused higher scores (other confounding variables like study hours exist).

---

## 3. Histogram (Weighted Score Distribution)

- **Analytical Question:** What is the shape and spread of the overall student weighted score distribution?
- **Observations:**
  1. Most student weighted scores are concentrated between 60 and 80.
  2. The distribution appears roughly symmetric around the center with clear bell-like frequency peaks.
- **Interpretation:** Class performance follows a normal-like distribution where most students achieve average to above-average results.
- **Limitation:** The visual shape of the distribution is sensitive to the chosen bin count (e.g., comparing 5, 10, and 15 bins).

---

## 4. Bar Chart (Average Weighted Score by Program)

- **Analytical Question:** How do average weighted scores compare across different degree programs?
- **Observations:**
  1. Average scores vary slightly across degree programs once sorted.
  2. Overall mean score differences between programs remain relatively small.
- **Interpretation:** Program-level performance is generally balanced, though minor variations exist among specific cohorts.
- **Limitation:** Bar charts only summarize category means and obscure internal variance or distribution within each program.

---

## 5. Box Plot (Weighted Score Summary)

- **Analytical Question:** What are the median, spread, quartiles, and potential outliers in the weighted score dataset?
- **Observations:**
  1. The median line sits centrally inside the interquartile range (IQR) box.
  2. Individual data points extend beyond the whiskers, highlighting extreme values.
- **Interpretation:** Scores show moderate spread, and identified outliers represent data points that warrant further investigation rather than automatic deletion.
- **Limitation:** Box plots summarize data statistics well but do not show underlying point density or multimodal distributions.