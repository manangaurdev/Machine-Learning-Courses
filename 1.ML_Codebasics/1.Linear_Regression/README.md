# Linear Regression: Predicting House Prices

This project demonstrates how to use linear regression to predict house prices based on area using Python and scikit-learn.

## Files

- **homeprices.csv**: Training dataset containing `area` and `price` columns.
- **area.csv**: File containing new area values (with a header `area`) for which you want to predict prices.
- **Linear_Regression_Single_Variables.py**: Main Python script for training, predicting, and visualizing.
- **predicted_prices.csv**: Output file with predicted prices for the areas in `area.csv`.

## How It Works

1. **Load Data**: Reads `homeprices.csv` into a pandas DataFrame.
2. **Visualize Data**: Plots a scatter plot of area vs. price.
3. **Train Model**: Trains a linear regression model using scikit-learn.
4. **Predict Prices**: Reads new areas from `area.csv` and predicts their prices.
5. **Save Predictions**: Saves the predicted prices to `predicted_prices.csv`.
6. **Visualize Regression Line**: Plots the regression line on the scatter plot.

## Usage

1. Place your `homeprices.csv` and `area.csv` files in the same directory as the script.
2. Run the script:
    ```bash
    python Linear_Regression_Single_Variables.py
    ```
3. Check `predicted_prices.csv` for the results.

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- scikit-learn

Install dependencies with:
```bash
pip install pandas numpy matplotlib scikit-learn
```

## Example

**homeprices.csv**
```
area,price
2600,550000
3000,565000
3200,610000
3600,680000
4000,725000
```

**area.csv**
```
area
3300
4000
5000
```

**predicted_prices.csv** (output)
```
area,prices
3300, predicted_value_1
4000, predicted_value_2
5000, predicted_value_3
```

---

*Created for educational purposes. Adapt as needed for your own datasets!*