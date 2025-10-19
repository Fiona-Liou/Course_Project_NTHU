# PBA AS2: Visualization and Causality

## Background
This assignment consists of two parts, each focusing on different datasets and aspects of business analytics we have covered so far in class. You are required to use **R Markdown** (or **Quarto**, which is an upgraded version of R Markdown) to generate your responses for this and all subsequent assignments.  

Before you begin working on the questions, please make sure you have gone through the following guidelines:

### Guidelines
- **Package Loading**  
  Make sure to load all the necessary packages in the setup chunk, which should be the first code chunk in your document.  
- **Verbal Explanation**  
  Throughout the assignment, you’ll be asked to provide explanations or interpretations of your findings. Include these in the main text, outside any code chunks.

---

## PART I: Data Visualization

In this part of the assignment, you will analyze national monitoring data on fine particulate matter (**PM2.5**) air pollution in the United States from the years **1999** and **2012**.  
The dataset, provided by the **U.S. Environmental Protection Agency (EPA)**, contains detailed information on PM2.5 levels from monitoring sites across the U.S.

Your task is to explore the data and assess whether there has been a change in PM2.5 outdoor air pollution levels between these two years.  
You suspect that nationwide regulatory efforts, especially those under the **Clean Air Act**, might have led to a decrease in the average levels of PM2.5.

---

### Question 1
Import the air pollution data for 1999 and 2012 using `read_csv()` from the provided URLs.  

**Data Links:**
- 1999: [https://bit.ly/3c4AHbL](https://bit.ly/3c4AHbL)  
- 2012: [https://bit.ly/3nZicL2](https://bit.ly/3nZicL2)

**Tasks:**
1. Store the datasets as `air99` and `air12`.  
2. Use `mutate()` to add a `Year` column to each dataset.  
3. Rename `Sample.Value` to `PM2.5`.  
4. Use `drop_na()` to remove incomplete rows.  
5. Combine the datasets with `bind_rows()` into `air_combined`.  
6. Check the structure using `glimpse()`.

---

### Question 2
Some PM2.5 observations are negative due to sensor errors.  
Use `group_by()` and `summarize()` to calculate summary statistics (mean, median, min, max) for each year.  
Filter observations with PM2.5 > 0, and overwrite the cleaned dataset as `air_combined`.

---

### Question 3
Create a **boxplot** comparing PM2.5 distributions for 1999 and 2012, using a **log2 transformation**.

**Instructions:**
- Center and size plot with `fig.align='center'`, `fig.width=10`, `fig.height=3`.  
- Use `ggplot2` with `aes(x = as.factor(Year), y = log2(PM2.5), fill = as.factor(Year))`.  
- Apply `scale_fill_brewer(palette = "Set1")`.  
- Label axes and use `theme_minimal()`.

---

### Changes in PM Levels at an Individual Monitor
To avoid network bias, analyze a single monitor in **New York State**.

#### Question 4
Subset `air_combined` to `State.Code == 36` and store as `ny_data`.  
Create `site.code` using `paste0(County.Code, ".", Site.ID)`.

---

#### Question 5
Find monitors in `ny_data` active in both years using `group_by(site.code)` and `n_distinct(Year)`.  
Extract site codes into `active_both_year`.

---

#### Question 6
Identify the monitor with the highest number of observations across both years.  
Filter for `active_both_year`, count, and arrange in descending order.

---

#### Question 7
Focus on **monitor 101.0003** (most active).  
Subset `ny_data` for this monitor into `air101.0003`.  
Convert `Date` to date object with `ymd()` and extract day of year with `yday()`.

---

#### Question 8
Replicate the scatter plot of daily PM2.5 for monitor **101.0003** in 1999 vs. 2012.

**Instructions:**
- Use `facet_wrap(~Year)` for side-by-side panels.  
- Label x-axis “Day of the Year”.  
- Analyze differences and trends.

---

## PART II: Causality

This part uses data from **Robert Lalonde (1986)**, studying the impact of job training on employee earnings.  
Participants were randomly assigned to **treatment** (training) and **control** groups.

Dataset: [https://bit.ly/3sJJKuk](https://bit.ly/3sJJKuk)  
Source: [MIT Economics Archive](https://economics.mit.edu/people/faculty/josh-angrist/mhe-data-archive)

---

### Question 9
Assess **covariate balance** between treatment and control groups.

**Steps:**
1. Read data as `lalonde`.  
2. Use `group_by(treatment)` and `summarize()` to compute averages for:  
   `age`, `education`, `black`, `hispanic`, `married`, `nodegree`.  
3. Store result as `balance_table`.  
4. Display table with `knitr::kable()`.  
5. Comment on balance.

---

### Question 10
Estimate **average treatment effect (ATE)** on earnings.

**Steps:**
1. Create variable `change = re78 - re75`.  
2. Compute mean change for treated (`trt_change`) and control (`ctr_change`).  
3. Compute ATE = trt_change − ctr_change.  
4. Interpret results.

---

### Question 11
Explain the **potential outcomes** for an individual and the **fundamental problem of causal inference** in this experiment.

---

### Question 12
Discuss whether using `re75` or `re78` alone as the outcome would be valid.  
Explain why or why not.

---

### Question 13
Test if **education level (nodegree)** modifies the treatment effect.

**Steps:**
1. Create labels for treatment (`Treated` / `Control`) and education (`Dropped out` / `Finished HS`).  
2. Use `group_by()` and `summarize()` to compute mean change by group.  
3. Pivot wider to show columns: dropout, Treated, Control, ATE.  
4. Format with `knitr::kable()`.

---

### Question 14
Analyze heterogeneity of treatment effects by **age group**.

**Steps:**
1. Create variable `age_group` with:
   - "30 and under"
   - "31–40"
   - "Over 40"  
2. Use same process as Question 13 to compute `ate_age`.

---

### Question 15
Plot **ATE by age group** using `ggplot` and store as `age_plot`.

**Tasks:**
- Include informative axis labels and title.  
- Discuss whether treatment effects vary by age.

---

## End of Assignment
- **Deliverables:** R Markdown (`.Rmd` or `.qmd`) + Compiled HTML report  
- **Software:** R, tidyverse, ggplot2, lubridate, knitr
