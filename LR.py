
def create_LR(df,ticker):
    import numpy as np
    y = np.array(data['Adj Close'])
    X = np.array(pd.to_datetime(data['Adj Close'].index).map(dt.datetime.toordinal))

    intercept, slope = np.polynomial.polynomial.polyfit(X, y, deg =1)
    regression_line = (slope * X + intercept)
    # Calculate standard deviation
    std_dev = np.std(y - regression_line)
    # std_dev = np.std(y)
    plus_2_std = regression_line + 2 * std_dev
    minus_2_std = regression_line - 2 * std_dev
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=X, y=y, label='Stock Data', alpha=0.5)
    plt.plot(X, regression_line, color='red', label='Linear Regression Line')
    plt.plot(X, plus_2_std, color='blue', linestyle='--', label='+2.5 Std Dev')
    plt.plot(X, minus_2_std, color='blue', linestyle='--', label='-2.5 Std Dev')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression and ±2 Standard Deviations')
    plt.legend()
    plt.grid(True)
    return plt.show()
    #plt.savefig(f"../LR/{ticker}.png")