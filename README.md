# S&P500 Bollinger Bands Analysis (GUI)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![Status](https://img.shields.io/badge/Status-Maintained-success)

## Overview

A Python desktop application for technical analysis of the S&P 500 index using Bollinger Bands. The app fetches real-time data from Yahoo Finance and visualizes the trends in an interactive GUI.

## Key Features

* **Data Fetching:** Automatically downloads the last 12 months of daily data for the S&P 500 index (`^GSPC`) using the `yfinance` library.
* **Technical Analysis:** Calculates simple moving averages (SMA) and Bollinger Bands (Upper & Lower) based on user-defined window.
* **Interactive Visualization:** Displays a dynamic chart with:
    * Close Price (Blue)
    * Moving Average (Orange)
    * Bollinger Bands (Green/Red dashed lines)
* **Customizable Parameter:** Users can adjust the moving average window (5 to 60 days) via a slider to see real-time updates on the chart.


## Methodology

The application calculates Bollinger Bands using the following logic:
1.  **Moving Average:** Calculates the mean of the 'Close' price over the selected window $n$ (slider input).
2.  **Standard Deviation (STD):** Calculates the STD over the same window.
3.  **Upper Band:** $SMA + (2 \times STD)$
4.  **Lower Band:** $SMA - (2 \times STD)$

## Screenshot

<img width="637" height="587" alt="image" src="https://github.com/user-attachments/assets/d8bc8be6-7e06-4a81-9105-430af8dd14da" />

## Tech

* **Python 3**
* **tkinter** (GUI)
* **yfinance** (Financial Data)
* **pandas** (Data Manipulation)
* **matplotlib** (Data Visualization)

## Installation & Usage
To run this app locally:
1.  Clone the repository:
    ```bash
    git clone [https://github.com/margor6/SP500-Bollinger-Analyzer.git](https://github.com/margor6/SP500-Bollinger-Analyzer.git)
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    python main.py
    ```


