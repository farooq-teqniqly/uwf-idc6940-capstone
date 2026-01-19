# Capstone Project: Trip Duration Forecasting and Prediction

## Project Overview

This capstone project extends previous time-series forecasting work on Uber trip durations by incorporating machine learning-based prediction methods and comparing their performance.

## Project Scope and Goals

### Primary Focus

- **Trip Duration Forecasting and Prediction**: The capstone focuses on developing and evaluating both time-series forecasting models and ML-based prediction models for Uber trip durations in New York City
- **Comparative Analysis**: Compare the performance of time-series forecasting methods (extending previous ARIMA work) with ML-based prediction methods

### Previous Work

- Previous time-series analysis was completed using ARIMA models for daily average Uber trip durations
- Previous work is documented in: `uwf-sta6856/finalproject/docs/finalproject-report.tex`
- Previous work used NYC TLC data aggregated to daily averages (365 data points for 2024)

### Current Capstone Scope

1. **Time-Series Forecasting**: Extend previous ARIMA work for trip duration forecasting
2. **ML-Based Prediction**: Develop machine learning models for trip duration prediction
3. **Performance Comparison**: Compare accuracy and performance of time-series vs ML methods
4. **Data Source**: Use Uber ride-sharing data from NYC TLC (not yellow taxi data)

### Out of Scope

- **Charging Optimization**: Charging optimization for electric ride-hailing fleets is NOT in scope for this capstone
  - While accurate trip duration predictions could potentially benefit charging optimization frameworks in future work, that integration is outside the capstone scope
  - Charging optimization might be a side benefit but is not the main focus

## Data Details

- **Source**: NYC Taxi and Limousine Commission (TLC) - Uber ride-sharing data
- **Note**: The capstone uses Uber ride-sharing data, NOT yellow taxi data (which is used in some related papers)
- **Previous preprocessing**: Used PySpark to aggregate 200+ million records to daily averages

## Methodology

### Time-Series Approach

- Extends previous ARIMA modeling work
- Focuses on temporal patterns and historical trends
- Uses daily aggregated trip duration data

### Machine Learning Approach

- Develops ML models to capture complex non-linear relationships
- Considers multiple factors: temporal patterns, origin-destination pairs, demand volatility, congestion
- Feature engineering informed by stochastic demand modeling

### Comparison Framework

- Evaluate both approaches on the same dataset
- Compare accuracy metrics and performance
- Identify strengths and limitations of each approach

## Key Insights from Related Work

- Temporal patterns (daily, weekly, seasonal) are important for trip duration prediction
- Stochastic customer demand affects trip durations through congestion and demand volatility
- Multi-scale temporal modeling (different decision horizons) may benefit both time-series and ML approaches
- Anticipative planning based on historical patterns is valuable for forecasting

## Project Context

- **Course**: UWF IDC6940 Capstone
- **Previous Course**: UWF STA6856 (Time Series Analysis)
- **Related Papers**: Ma et al. (2024) on coordinated vehicle dispatching and charging scheduling (provides methodological insights but focuses on charging optimization, which is out of scope)

## Important Notes

- When discussing this project, remember that charging optimization is NOT part of the capstone scope
- The focus is purely on trip duration forecasting/prediction and comparing time-series vs ML methods
- Data source is Uber ride-sharing data from NYC TLC, not yellow taxi data
- The project builds on previous ARIMA work but extends it with ML methods for comparison
