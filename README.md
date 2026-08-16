# Stock Return Calculator
A simple Python program that calculates stock profit, loss and percentage return based on initial and final prices.

## Features

- Calculates Profit or Loss
- Calculates percentage return
- Validates that stock prices are positive
- Formats prices and returns to two decimals

## How to Run

1. Make sure Python is installed.
2. Clone this repository.
3. Open the project folder in your terminal.
4. Run the following command:

```bash
python stock_return.py
```

## Formula

The percentage return is calculated as:

Return=((Final Price - Initial Price) / Initial Price) * 100

## Example

Input:

Stock:AAPL
Initial Price: $100.00
Final Price: $120.00

Output:

Stock: AAPL
Initial Price: $100.00
Final Price: $120.00
Profit: $20.00 
Return: 20.00 %

## Future Improvements

- Automatically retrieve stock market data using a financial data library such as yfinance
- Display stock data and calculated returns in a table
- Allow users to select a custom time period