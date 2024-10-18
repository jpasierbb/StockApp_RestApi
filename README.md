# Stock Trading Simulation

## Overview

This project is a stock trading simulation application that allows users to interact with a stock trading API. Users can buy and sell stocks across various exchanges and manage their stock portfolios. The application is divided into several modules, each responsible for different functionalities, including stock data retrieval, user management, and stock trading actions.\
This project was developed as part of our studies, utilizing an API that was prepared during our coursework.

## Modules

The project consists of the following key modules:

1. **stock_checking.py**: Handles the retrieval of stock data from the API, including checking available exchanges, shares, and prices.

2. **stock_user.py**: Manages user authentication and account information, providing methods to fetch user funds, transaction history, and current shares.

3. **stock_action.py**: Contains the logic for executing stock trades (buying and selling) and managing user stock actions.

4. **REST_3_1.py**, **REST_3_2.py**, **REST_3_3.py**, and **REST_3_4.py**: These scripts implement different trading strategies and user interactions for the stock trading simulation. Each script provides a specific trading functionality:
   - **REST_3_1**: Buys a random share from a random exchange for a selected user.
   - **REST_3_2**: Repeats the buying action 50 times across random exchanges and shares.
   - **REST_3_3**: Adjusts the user's stock portfolio to maintain a specific number of shares (40) by buying or selling shares as necessary.
   - **REST_3_4**: Ensures that the user owns one of each unique stock available across exchanges.

5. **REST_sell_all_reset.py**: Provides functionality to reset a user's stock portfolio by selling all shares they own.

6. **main.py**: Serves as the entry point for running the stock trading simulation and allows users to select their accounts.

## Requirements

To run this project, you need:
- Python 3.x
- Required packages for HTTP requests and JSON handling (typically included with Python).


## Getting Started

1. Clone the repository:
2. Navigate to the project directory.
3. Run the main script to start the application:
```bash
python main.py
```

## Usage

Upon running the application, users are prompted to select their account (Andrzej or Kuba). The application will then allow users to execute stock trades based on the defined strategies in the REST files.
