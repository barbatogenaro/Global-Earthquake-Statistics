# Advanced Statistical Analysis of Global and Regional Seismicity 🌍

This repository contains an in-depth exploratory and inferential statistical analysis of global earthquake data, with a specialized focus on the **South American margin**. The project transitions from Exploratory Data Analysis (EDA) to complex statistical modeling and hypothesis testing.

## 📊 Key Research Phases

### 1. Regional EDA: South American Margin
* **Targeted Filtering:** Specialized analysis for Chile, Peru, Ecuador, and Colombia, identifying seismic patterns along the Nazca-South American plate boundary.
* **Geospatial Correlations:** Analysis of the **Longitudinal Cartesian Reference (LCR)** to identify the concentration of high-magnitude events relative to the trench.
* **Outlier Analysis:** Use of multi-country boxplots to identify "extreme" seismic events (e.g., Valdivia 1960, Maule 2010) that deviate from central tendencies.

### 2. Statistical Modeling & Distribution Fitting
* **Discrete Variables:** Analysis of seismic frequency per month (2022-2023) for events $M > 5.5$. Fitting and comparison of **Binomial, Poisson, and Uniform** distributions.
* **Continuous Variables:** Modeling of earthquake depth and magnitude using **Normal, Gamma, Weibull, and t-Student** distributions.
* **Inter-seismic Period (GAP):** Evaluation of the time intervals between major events and their probability density functions.

### 3. Hypothesis Testing
* **Inference:** Implementation of **Chi-Squared tests** to validate the fit between observed seismic data and theoretical distributions (e.g., testing Uniform distribution for monthly frequency and t-Student for focal depth in Chile).

## Tech Stack
* **Python 3.12**
* **Analysis:** `Pandas`, `NumPy`, `Statistics`
* **Inference & Math:** `SciPy.stats` (norm, gamma, poisson, chi2, etc.)
* **Visualization:** `Matplotlib` (Subplots, Boxplots, Histograms)

## Key Findings
* **Inverse Relationship:** Confirmed an inverse correlation (negative covariance) between distance from the subduction trench and both earthquake frequency and magnitude.
* **Seismic Window:** Identification of the "Statistical Zone" ($\approx 70^\circ$ Longitude) where the highest density of tectonic stress release occurs.
* **Distribution Performance:** While seismic depth in Chile shows a strong visual fit with a **t-Student distribution**, Chi-Squared tests reveal the complexity and non-random nature of seismic clustering.

---
**Author:** Genaro Barbato Osorio | Geologist & Data Analyst 