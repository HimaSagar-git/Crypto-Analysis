import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# Set style for visualizations
plt.style.use('seaborn')
sns.set_palette("deep")

# Load and preprocess data
def load_data(file_path):
    try:
        # Read CSV file
        df = pd.read_csv(file_path, parse_dates=['date'])
        # Ensure date is datetime
        df['date'] = pd.to_datetime(df['date'])
        # Set date as index
        df.set_index('date', inplace=True)
        # Sort by date
        df.sort_index(inplace=True)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Calculate technical indicators
def calculate_indicators(df):
    # Calculate 20-day Simple Moving Average
    df['SMA20'] = df['close'].rolling(window=20).mean()
    
    # Calculate 50-day Simple Moving Average
    df['SMA50'] = df['close'].rolling(window=50).mean()
    
    # Calculate daily returns
    df['daily_return'] = df['close'].pct_change()
    
    # Calculate volatility (20-day rolling std of returns)
    df['volatility'] = df['daily_return'].rolling(window=20).std() * np.sqrt(252)
    
    return df

# Plot price and moving averages
def plot_price_moving_averages(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['close'], label='Close Price', alpha=0.8)
    plt.plot(df.index, df['SMA20'], label='20-day SMA', alpha=0.8)
    plt.plot(df.index, df['SMA50'], label='50-day SMA', alpha=0.8)
    plt.title('Bitcoin Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('price_moving_averages.png')
    plt.close()

# Plot volume
def plot_volume(df):
    plt.figure(figsize=(12, 6))
    plt.bar(df.index, df['volume'], color='blue', alpha=0.6)
    plt.title('Bitcoin Trading Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('volume.png')
    plt.close()

# Plot volatility
def plot_volatility(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['volatility'], color='red', alpha=0.8)
    plt.title('Bitcoin 20-day Annualized Volatility')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('volatility.png')
    plt.close()

# Calculate and display basic statistics
def print_statistics(df):
    stats = {
        'Mean Price': df['close'].mean(),
        'Median Price': df['close'].median(),
        'Std Dev Price': df['close'].std(),
        'Mean Daily Return': df['daily_return'].mean() * 100,
        'Mean Volatility': df['volatility'].mean(),
        'Total Volume': df['volume'].sum()
    }
    
    print("\nBasic Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value:.2f}")

# Main analysis function
def analyze_crypto_data(file_path):
    # Load data
    df = load_data(file_path)
    if df is None:
        return
    
    # Calculate indicators
    df = calculate_indicators(df)
    
    # Generate visualizations
    plot_price_moving_averages(df)
    plot_volume(df)
    plot_volatility(df)
    
    # Print statistics
    print_statistics(df)
    
    # Generate summary report
    with open('crypto_analysis_report.txt', 'w') as f:
        f.write("Cryptocurrency Analysis Report\n")
        f.write("=" * 30 + "\n\n")
        f.write(f"Analysis Period: {df.index[0].strftime('%Y-%m-%d')} to {df.index[-1].strftime('%Y-%m-%d')}\n")
        f.write(f"Total Days: {len(df)}\n\n")
        f.write("Key Statistics:\n")
        for key, value in print_statistics(df).items():
            f.write(f"{key}: {value:.2f}\n")
        f.write("\nGenerated Visualizations:\n")
        f.write("- Price with Moving Averages (price_moving_averages.png)\n")
        f.write("- Trading Volume (volume.png)\n")
        f.write("- Volatility (volatility.png)\n")

# Example usage
if __name__ == "__main__":
    # Replace with your actual data file path
    file_path = "bitcoin_data.csv"
    analyze_crypto_data(file_path)