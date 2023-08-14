<div class='PortMarker'>

### Description

<div class='StyledHR StyledHRProjects'></div>

1. Problem Statement
Predict the number of Dengue cases in San Juan and Iquitos using environmental variables. The goal is to predict the total_cases label for each combination of (city, year, weekofyear) in the test set.

2. Data Sources
Data for this project comes from multiple sources, including:

U.S. Centers for Disease Control and Prevention: Provides Dengue surveillance data.
National Oceanic and Atmospheric Administration (NOAA): Supplies environmental and climate data.
3. Features
The dataset includes various features on a (year, weekofyear) timescale, such as:

Climate data: Temperature (max, min, avg), precipitation, diurnal temperature range.
Satellite measurements: Precipitation amounts, dew point temperature, air temperature, humidity, vegetation index (NDVI).
4. Target Cities
Predictions are made for two cities:

San Juan, Puerto Rico (sj)
Iquitos, Peru (iq)
5. Performance Metric
The performance of the model is evaluated using the Mean Absolute Error (MAE).

6. Significance
Accurate predictions of Dengue spread can help public health workers and governments take steps to reduce the impact of epidemics. This project aligns with the Predict the Next Pandemic Initiative, consolidating various data sets to tackle the complex task of predicting Dengue fever.

7. Project Deployment
The findings are planned to be displayed interactively through a Streamlit web application, showcasing relationships between features and labels for each city and enabling direct comparisons between cities.