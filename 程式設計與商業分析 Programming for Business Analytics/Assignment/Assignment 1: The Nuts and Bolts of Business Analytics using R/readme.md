# PBA AS1: The Nuts and Bolts of Business Analytics Using R

## Background
This assignment consists of two parts, each focusing on different datasets and aspects of business analytics we have covered so far in class. You are required to use **R Markdown** (or **Quarto**, which is an upgraded version of R Markdown) to generate your responses for this and all subsequent assignments.  

Before you begin working on the questions, please make sure you have gone through the following guidelines:

### Guidelines
- **Package Loading**  
  Make sure to load all the necessary packages in the setup chunk, which should be the first code chunk in your document. For example:
  ```r
  require(lubridate)
  require(gapminder)
  ```
- **Verbal Explanation**  
  Throughout the assignment, you’ll be asked to provide explanations or interpretations of your findings. Make sure to include these in the main text, outside of any code chunks.

**Note:** This document is also created using R Markdown; if you’re unfamiliar with R Markdown, please refer to the materials shared on Canvas.

---

## PART I: Online Retail Data Analysis

The first part of this assignment uses data provided by the **UC Irvine Machine Learning Repository**, an open-source repository of datasets that can be freely downloaded.  
You will use the **“Online Retail Data Set”**, which can be downloaded here:

- **Dataset:** Online retail transactions in CSV format (44.5 MB)

**Description:** This dataset contains all transactions from **January 12, 2010, to September 12, 2011**, for a UK-based non-store online retailer that primarily sells unique all-occasion gifts. Many customers are wholesalers (B2B).

**Variable Descriptions:**

| Name | Description |
|------|--------------|
| InvoiceNo | 6-digit transaction number; if it starts with “C”, it indicates a cancellation. |
| StockCode | 5-digit product code. |
| Description | Product name. |
| Quantity | Number of units sold per transaction. |
| InvoiceDate | Transaction date and time (mm/dd/yy). |
| UnitPrice | Product price per unit (in sterling). |
| CustomerID | 5-digit customer ID (missing if not logged in). |
| Country | Customer’s country. |

---

### Question 1
Locate the directory path where the dataset is stored, load it into R, and inspect the data using `head()` and `str()`.

---

### Question 2
Convert `InvoiceDate` to date class and filter transactions to include only those from **July to August 2011**. Use this filtered dataset for all subsequent questions in Part I.

---

### Question 3
Perform basic data analysis on the dataset:

**Tasks:**
- Compute the mean of `Quantity` and `UnitPrice`.
- Determine the data types of each column.
- Compute the number of unique values in each column.

---

### Question 4
Conduct a **country-specific analysis** for **U.K., Netherlands, and Australia**.

**Tasks:**
- Subset the data for each country.  
- Report the average and standard deviation of `UnitPrice`.  
- Report the number of unique transactions and customers in each country.

---

### Question 5
Identify and count customers who made a **refund** (where `InvoiceNo` starts with “C”).  
Store their IDs in a vector called `cust_refund`.

---

### Question 6
Analyze transactions with **missing CustomerID** (NA).

**Tasks:**
- Create a variable called `Sales = Quantity * UnitPrice`.
- Calculate total sales amount for transactions with missing `CustomerID`.

---

## PART II: Data Visualization with Gapminder

In this part, you will explore data visualization using **ggplot2** and the **Gapminder dataset**, which contains economic and demographic data for countries over time.

**Variable Descriptions:**

| Name | Description |
|------|--------------|
| country | Name of the country |
| continent | Continent name |
| year | Year of measurement (1952–2007, every 5 years) |
| lifeExp | Life expectancy at birth (years) |
| pop | Population |
| gdpPercap | GDP per capita (US dollars, inflation-adjusted) |

---

### Question 7
Ensure the `gapminder` and `tidyverse` packages are loaded. Use `glimpse()` to display dataset details.  
In the main text, report:
- Number of rows and columns.  
- Which variables are factors.

---

### Question 8
Investigate how **life expectancy varies across continents** using **ggplot2**.

Create **boxplots** showing the distribution of life expectancy for each continent, similar to the reference figure provided.  
Include appropriate labels and a clean theme.

---

### Question 9
From the boxplot in Question 8:
- Identify which continent has the highest median life expectancy.  
- Explain which part of the boxplot this can be observed from.

---

## End of Assignment
- **Deliverables:** R Markdown (`.Rmd` or `.qmd`) + Compiled HTML report  
- **Software:** R, tidyverse, ggplot2, lubridate
