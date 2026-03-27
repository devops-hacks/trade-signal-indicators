from matplotlib.axes import Axes
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import numpy as np

# Create a figure with 2 rows (Price and RSI) and 2 columns (Bearish and Bullish examples)
fig: Figure
axs: np.ndarray
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
plt.style.use('seaborn-v0_8-whitegrid')

# --- DATA GENERATION ---

# 1. BEARISH DIVERGENCE SETUP (Top Left & Bottom Left)
# Price makes a Higher High
price_bearish_peak1 = 100
price_bearish_peak2 = 110 
price_bearish_trend = np.linspace(90, 105, 20)
price_bearish_correction = np.linspace(105, 95, 10)
price_bearish_rally = np.linspace(95, 110, 15)
price_bearish_data = np.concatenate([price_bearish_trend, price_bearish_correction, price_bearish_rally])

# RSI makes a Lower High (Momentum fading)
rsi_bearish_peak1 = 75
rsi_bearish_peak2 = 65 # Lower than 75
rsi_bearish_trend = np.linspace(40, 75, 20)
rsi_bearish_correction = np.linspace(75, 55, 10)
rsi_bearish_rally = np.linspace(55, 65, 15)
rsi_bearish_data = np.concatenate([rsi_bearish_trend, rsi_bearish_correction, rsi_bearish_rally])

# 2. BULLISH DIVERGENCE SETUP (Top Right & Bottom Right)
# Price makes a Lower Low
price_bullish_low1 = 100
price_bullish_low2 = 90
price_bullish_drop1 = np.linspace(110, 100, 15)
price_bullish_bounce = np.linspace(100, 105, 10)
price_bullish_drop2 = np.linspace(105, 90, 20)
price_bullish_data = np.concatenate([price_bullish_drop1, price_bullish_bounce, price_bullish_drop2])

# RSI makes a Higher Low (Momentum strengthening)
rsi_bullish_low1 = 30
rsi_bullish_low2 = 40 # Higher than 30
rsi_bullish_drop1 = np.linspace(50, 30, 15)
rsi_bullish_bounce = np.linspace(30, 45, 10)
rsi_bullish_drop2 = np.linspace(45, 40, 20)
rsi_bullish_data = np.concatenate([rsi_bullish_drop1, rsi_bullish_bounce, rsi_bullish_drop2])


# --- PLOTTING ---

# Function to plot the setup
def plot_divergence(
    ax_price: Axes,
    ax_rsi: Axes,
    price_data: np.ndarray,
    rsi_data: np.ndarray,
    title: str,
    div_type: str,
) -> None:
    # Plot Price
    ax_price.plot(price_data, color='black', linewidth=2, label='Price')
    ax_price.set_title(f'{title} - Price Chart', fontsize=12, fontweight='bold')
    ax_price.legend(loc='upper left')
    
    # Plot RSI
    ax_rsi.plot(rsi_data, color='purple', linewidth=2, label='RSI')
    ax_rsi.axhline(70, color='red', linestyle='--', alpha=0.5)
    ax_rsi.axhline(30, color='green', linestyle='--', alpha=0.5)
    ax_rsi.set_title('RSI Indicator', fontsize=12)
    ax_rsi.legend(loc='upper left')
    
    # Connect the divergence lines
    if div_type == 'bearish':
        # Identify peaks roughly
        idx_p1 = 20 # Approx index of first peak
        idx_p2 = 44 # Approx index of second peak
        
        # Price Higher High Line (Red)
        ax_price.plot([idx_p1, idx_p2], [price_data[idx_p1], price_data[idx_p2]], 
                      color='red', linestyle='--', linewidth=2, marker='o', label='Price Higher High')
        ax_price.annotate('Higher High', (idx_p2, price_data[idx_p2]), xytext=(5,5), textcoords='offset points', color='red')
        
        # RSI Lower High Line (Red)
        ax_rsi.plot([idx_p1, idx_p2], [rsi_data[idx_p1], rsi_data[idx_p2]], 
                    color='red', linestyle='--', linewidth=2, marker='o', label='RSI Lower High')
        ax_rsi.annotate('Lower High', (idx_p2, rsi_data[idx_p2]), xytext=(5,5), textcoords='offset points', color='red')
        
        # Mark Reversal Area
        ax_price.axvspan(idx_p2, len(price_data)-1, color='red', alpha=0.1, label='Potential Reversal Zone')

    elif div_type == 'bullish':
        # Identify troughs roughly
        idx_t1 = 15 # Approx index of first low
        idx_t2 = 44 # Approx index of second low
        
        # Price Lower Low Line (Green)
        ax_price.plot([idx_t1, idx_t2], [price_data[idx_t1], price_data[idx_t2]], 
                      color='green', linestyle='--', linewidth=2, marker='o', label='Price Lower Low')
        ax_price.annotate('Lower Low', (idx_t2, price_data[idx_t2]), xytext=(5,5), textcoords='offset points', color='green')
        
        # RSI Higher Low Line (Green)
        ax_rsi.plot([idx_t1, idx_t2], [rsi_data[idx_t1], rsi_data[idx_t2]], 
                    color='green', linestyle='--', linewidth=2, marker='o', label='RSI Higher Low')
        ax_rsi.annotate('Higher Low', (idx_t2, rsi_data[idx_t2]), xytext=(5,5), textcoords='offset points', color='green')
        
        # Mark Reversal Area
        ax_price.axvspan(idx_t2, len(price_data)-1, color='green', alpha=0.1, label='Potential Reversal Zone')

# Plot Bearish Divergence (Left Column)
plot_divergence(axs[0, 0], axs[1, 0], price_bearish_data, rsi_bearish_data, 
                'BEARISH DIVERGENCE (Sell Signal)', 'bearish')

# Plot Bullish Divergence (Right Column)
plot_divergence(axs[0, 1], axs[1, 1], price_bullish_data, rsi_bullish_data, 
                'BULLISH DIVERGENCE (Buy Signal)', 'bullish')

plt.tight_layout()
plt.show()