# Cryptocurrency Exchange Data Analysis Project

## Overview
This project is a Python-based data analysis tool designed to analyze historical Bitcoin price data from a cryptocurrency exchange. It calculates technical indicators, generates visualizations, and produces a summary report to help understand price trends, trading volume, and volatility patterns.

## Features
- **Data Preprocessing**: Loads and cleans historical Bitcoin price data from a CSV file.
- **Technical Indicators**:
  - 20-day and 50-day Simple Moving Averages (SMA)
  - Daily returns
  - 20-day annualized volatility
- **Visualizations**:
  - Price chart with 20-day and 50-day SMAs
  - Trading volume chart
  - Volatility chart
- **Statistics**: Calculates and displays basic statistics (mean, median, standard deviation of price, etc.).
- **Report Generation**: Creates a text-based summary report with key findings.

## Prerequisites
To run this project, ensure you have the following installed:
- **Python 3.8+**
- **Required Python libraries**:
  - `pandas` (for data manipulation)
  - `matplotlib` (for plotting)
  - `seaborn` (for enhanced visualizations)
  - `numpy` (for numerical calculations)

You can install the required libraries using pip:
```bash
pip install pandas matplotlib seaborn numpy
```

## Data Requirements
The project expects a CSV file (`bitcoin_data.csv`) with the following columns:
- `date`: Date of the record (e.g., YYYY-MM-DD)
- `open`: Opening price of Bitcoin in USD
- `high`: Highest price of Bitcoin in USD
- `low`: Lowest price of Bitcoin in USD
- `close`: Closing price of Bitcoin in USD
- `volume`: Trading volume

You can obtain historical Bitcoin price data from cryptocurrency exchanges or data providers like CoinGecko, CoinMarketCap, or Binance API. Ensure the CSV file is placed in the same directory as the script or update the file path in the script.

## Project Structure
- `crypto_analysis.py`: Main Python script containing the analysis logic.
- `bitcoin_data.csv`: Input data file (not included; user must provide).
- Output files (generated after running the script):
  - `price_moving_averages.png`: Plot of Bitcoin price with 20-day and 50-day SMAs.
  - `volume.png`: Bar chart of trading volume.
  - `volatility.png`: Plot of 20-day annualized volatility.
  - `crypto_analysis_report.txt`: Text file summarizing the analysis results.

## Installation
1. Clone or download this project to your local machine.
2. Ensure the required Python libraries are installed (see Prerequisites).
3. Place your `bitcoin_data.csv` file in the project directory or update the file path in `crypto_analysis.py` if the file is located elsewhere.

## Usage
1. Open a terminal or command prompt in the project directory.
2. Run the script using Python:
   ```bash
   python crypto_analysis.py
   ```
3. The script will:
   - Load and process the data from `bitcoin_data.csv`.
   - Calculate technical indicators (SMAs, returns, volatility).
   - Generate three visualization files (PNG format).
   - Create a summary report (`crypto_analysis_report.txt`).
   - Display basic statistics in the console.

## Output Details
- **Visualizations**:
  - `price_moving_averages.png`: Shows Bitcoin's closing price alongside 20-day and 50-day SMAs to identify trends.
  - `volume.png`: Displays trading volume over time, highlighting periods of high/low activity.
  - `volatility.png`: Plots 20-day annualized volatility, indicating periods of price instability.
- **Report** (`crypto_analysis_report.txt`):
  - Analysis period (start and end dates)
  - Total days analyzed
  - Key statistics (mean price, median price, standard deviation, etc.)
  - List of generated visualizations
- **Console Output**:
  - Basic statistics, including mean price, median price, standard deviation, mean daily return, mean volatility, and total volume.

## Example Data Format
Your `bitcoin_data.csv` should look like this:
```csv
date,open,high,low,close,volume
2023-01-01,16500.50,16600.75,16450.25,16550.30,250000
2023-01-02,16550.30,16700.00,16400.00,16600.45,300000
...
```

## Customization
To customize the analysis:
- Modify the moving average windows (e.g., change `SMA20` to a different period) in the `calculate_indicators` function.
- Adjust the visualization styles or add new plots in the respective plotting functions.
- Update the file path in the `analyze_crypto_data` function if your data file has a different name or location.

## Troubleshooting
- **File Not Found Error**: Ensure `bitcoin_data.csv` exists in the project directory or update the file path in the script.
- **Missing Libraries**: Install all required libraries using pip (see Prerequisites).
- **Data Format Issues**: Verify that your CSV file has the required columns and correct data types (e.g., dates in YYYY-MM-DD format, numerical values for prices and volume).

## Limitations
- The project assumes daily data; intraday data may require modifications.
- Only Bitcoin data is supported in the current implementation. To analyze other cryptocurrencies, ensure the data follows the same format.
- No real-time data fetching is included; you must provide historical data in CSV format.

## Future Enhancements
- Add support for multiple cryptocurrencies.
- Include additional technical indicators (e.g., RSI, Bollinger Bands).
- Implement real-time data fetching via exchange APIs.
- Add interactive visualizations using libraries like Plotly.

## License
This project is open-source and available under the MIT License.

## Contact
For questions or contributions, please contact the project maintainer or open an issue on the project repository.