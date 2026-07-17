# Data Cleaning and Exploratory Analysis Report

## Task Overview

This task takes a raw messy dataset and transforms it into an analysis-ready dataset through a reproducible data pipeline. The process includes data inspection, cleaning, exploratory data analysis (EDA), feature engineering, and extracting meaningful insights.

The complete pipeline can be executed from start to finish without manual intervention.

---

# Dataset Description

## Dataset Used
**Dataset Name:** Titanic Dataset

## Dataset Source
The dataset was sourced from [Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset).

## Dataset Overview

The dataset contains information about passengers aboard the Titanic, including demographic details, travel class, ticket information, fare, and survival outcome.

Each row represents **one passenger**, and each column represents a feature related to that passenger.

### Dataset Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| PassengerId | Integer | Unique identifier for each passenger |
| Survived | Integer | Survival status (0 = No, 1 = Yes) |
| Pclass | Integer | Passenger class (1st, 2nd, 3rd) |
| Name | String | Passenger name |
| Sex | String | Passenger gender |
| Age | Float | Passenger age |
| SibSp | Integer | Number of siblings/spouses aboard |
| Parch | Integer | Number of parents/children aboard |
| Ticket | String | Ticket number |
| Fare | Float | Ticket fare paid |
| Cabin | String | Cabin number |
| Embarked | String | Port of embarkation |

---

# Phase 1: Data Inspection

## Initial Dataset Information

Shape:

```
Rows: 891
Columns: 12
```

Initial inspection was performed using:

- `df.shape`
- `df.head()`
- `df.info()`
- `df.describe()`

## Missing Values

Missing values were identified using:

```python
df.isnull().sum()
```

Missing values were found in columns such as:

- Age: 177
- Embarked: 2
- Cabin: 687

---

# Phase 2: Data Cleaning

## 1. Duplicate Removal

Duplicate records were checked using:

```python
df.duplicated().sum()

The dataset did not contain any duplicate rows.

Result:

- Before: 0 duplicate rows
- After: 0 duplicate rows

No duplicate removal was required.
---

## 2. Standardizing Categories

Categorical columns were checked for inconsistent values, extra spaces, and different text casing.

The dataset categories were already mostly standardized, so no major category corrections were required. Basic text cleaning was applied where necessary to ensure consistent formatting.

Operations performed:

- Checked categorical columns for unique values
- Removed unnecessary whitespace
- Ensured consistent text formatting

Result:

- Categories are standardized and ready for analysis.

---

## 3. Fixing Data Types

The data types of all columns were inspected using:

```python
df.info()
```

The dataset already contained appropriate data types:

- Numerical columns such as `Age`, `Fare`, `SibSp`, and `Parch` were stored as numeric types.
- Categorical columns such as `Sex`, `Name`, `Ticket`, `Cabin`, and `Embarked` were stored as text values.

No major data type conversion was required.

Result:

- All columns have appropriate data types for analysis.

---

## 4. Handling Missing Values

Missing values were handled using appropriate strategies:

| Column | Method | Reason |
|--------|--------|--------|
| Age | Median filling | Age distribution contains outliers |
| Embarked | Mode filling | Most frequent category represents majority |
| Cabin | Unknown category | Large number of missing values |

After cleaning:

```
No unhandled missing values remain.
```

---

# Phase 3: Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the patterns, distributions, and relationships between different variables in the Titanic dataset.

Four visualizations were created using Matplotlib and Seaborn. Each chart includes proper titles and axis labels with a key takeaway.

---

## Chart 1: Correlation Heatmap

A correlation heatmap was created using numerical columns to identify relationships between features.

```python
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True)
```

**Chart Purpose:**  
The heatmap shows the strength of relationships between numerical variables such as survival, passenger class, age, fare, and family-related features.

**Takeaway:**  
Survival has a relationship with passenger class and fare, indicating that socio-economic factors influenced survival chances.

---

## Chart 2: Survival Count

A count plot was created to show the number of passengers who survived and did not survive.

```python
sns.countplot(x="Survived", data=df)
```

**Chart Purpose:**  
This chart compares the number of passengers in each survival category.

**Takeaway:**  
The number of passengers who did not survive was higher than the number of passengers who survived.

---

## Chart 3: Survival by Gender

A count plot was created to analyze survival differences between male and female passengers.

```python
sns.countplot(x="Survived", hue="Sex", data=df)
```

**Chart Purpose:**  
This visualization compares survival outcomes across different genders.

**Takeaway:**  
Female passengers had a much higher survival rate compared to male passengers, showing that gender was an important factor in survival.

---

## Chart 4: Age Distribution

A histogram was created to understand the distribution of passenger ages.

```python
sns.histplot(df["Age"], bins=20, kde=True)
```

**Chart Purpose:**  
This chart shows how passenger ages were distributed across the dataset.

**Takeaway:**  
Most passengers were young adults, with fewer passengers in older age groups. Age distribution helps understand the demographic structure of passengers.

# Phase 4: Feature Engineering

New features were created from existing columns.

## 1. Family Size

Formula:

```
family_size = sibsp + parch + 1
```

**Purpose:**  
Combines family-related information into a single feature to analyze whether traveling with family affected survival.

---

## 2. Is Alone

Formula:

```
is_alone = 1 if family_size == 1 else 0
```

**Purpose:**  
Identifies passengers traveling alone, which may influence survival probability.

---

## 3. Extract Passenger Title

A new feature called `Title` was created by extracting the title from the passenger's name.

```python
df["Title"] = df["Name"].str.extract(r",\s*([^\.]+)\.")
```

**Purpose:**  
Titles can provide insights into social status, which may have influenced survival chances.

---

# Key Insights
# Key Insights

The following insights were extracted from the cleaned dataset using group-based survival analysis.

---

## 1: Survival Rate by Gender

Survival rates were calculated using:

```python
df.groupby("Sex")["Survived"].mean() * 100
```

**Insight:**  
Gender was an important factor influencing survival on the Titanic.

---

## 2: Survival Rate by Passenger Class

Survival rates were analyzed across passenger classes using:

```python
df.groupby("Pclass")["Survived"].mean() * 100
```

Passengers from higher classes had better survival rates compared to lower classes.

**Insight:**  
Passenger class had a strong relationship with survival probability.

---

## 3: Survival Rate by Traveling Status

Survival differences between passengers traveling alone and passengers traveling with family were analyzed using:

```python
df.groupby("IsAlone")["Survived"].mean() * 100
```

Passengers traveling alone and passengers traveling with family showed different survival patterns.

**Insight:**  
Family presence influenced survival outcomes, although its impact was smaller compared to gender and passenger class.

---

## Summary of Findings

- Female passengers had a much higher chance of survival than male passengers.
- First-class passengers had better survival rates than second and third-class passengers.
- Traveling status (`IsAlone`) showed differences in survival probability, indicating that family relationships may have influenced survival.

# Before and After Summary

| Metric | Before Cleaning | After Cleaning |
|--------|----------------|----------------|
| Rows | 891 | 891 |
| Duplicate Rows | 0 | 0 |
| Missing Values | 866 | 0 |
| Data Types | Correct | Correct |
| New Features | 0 | 3 |

---

# Data Ethics and Privacy Review

The dataset was checked for personally identifiable information (PII).

Potential sensitive columns:

- Passenger names
- Ticket numbers

In a real-world system, these fields should be protected or removed before public sharing.

The cleaned dataset used for analysis does not expose unnecessary personal information.

---

# Conclusion

The raw dataset was successfully cleaned, transformed, and analyzed through a reproducible workflow. The final dataset contains standardized values, correct data types, no duplicates, no missing values, and additional engineered features that improve analysis capability.