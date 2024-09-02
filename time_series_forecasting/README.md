# Time Series Forecasting for Socioeconomic Indicators

## Overview

This repository contains several Jupyter notebooks and datasets aimed at forecasting various socioeconomic indicators. This project explores different forecasting methodologies, including traditional statistical methods and machine learning approaches, to determine which is best suited for different types of socioeconomic data.

## Datasets

The datasets used in this project are sourced from the [Statistics Agency of Kazakhstan](https://stat.gov.kz/en/), covering various socioeconomic indicators such as GDP, CPI, housing, income, and population statistics.

### Data Files

- `CPI_data.csv`: Consumer Price Index data
- `GDP_data.csv`: Gross Domestic Product data
- `housing_data.csv`: Housing statistics
- `income_data.csv`: Income data
- `population_data.csv`: Population data

## Methodologies

The project employs three different time series forecasting methods, each implemented in its respective Jupyter notebook:

- `ARIMA.ipynb`: Autoregressive Integrated Moving Average model
- `ETS.ipynb`: Exponential Smoothing State Space model
- `LSTM.ipynb`: Long Short-Term Memory neural network model

## Key Findings

- **Traditional Methods**: For datasets exhibiting clear seasonal or linear trends, such as GDP and population data, traditional statistical methods like ARIMA and ETS were found to be more effective.
- **LSTM**: For more complex datasets with less discernible patterns, such as the Consumer Price Index, LSTM models performed better, capturing complex nonlinear relationships that traditional models could not.

## Conclusions

The analysis indicates that the choice of time series forecasting method heavily depends on the characteristics of the data. While traditional methods are well-suited for data with clear patterns, LSTM offers advantages in handling more complex and subtle trends.
