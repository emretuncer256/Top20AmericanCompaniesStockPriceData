import time
from datetime import date

import pandas as pd
import yfinance as yf


def fetch_data(
        company: str,
        start_date: date | str,
        end_date: date | str,
        debug: bool = False
) -> pd.DataFrame | None:
    """
        Fetches historical stock prices for a specific company within a specified date range.

        Args:
            - company (str): Company symbol (e.g., 'AAPL', 'GOOGL').
            - start_date (str or date): Start date of the data range in the format 'YYYY-MM-DD' or as a date object.
            - end_date (str or date): End date of the data range in the format 'YYYY-MM-DD' or as a date object.
            - debug (bool, optional): If True, displays additional information including the number of rows,
                                    number of columns, elapsed time, and the company symbol. Defaults to False.

        Returns:
            pandas DataFrame or None: A DataFrame containing the historical stock price data for the specified
                                      company within the given date range. Returns None if the data cannot be fetched
                                      or an error occurs during the retrieval process.
        """
    try:
        if isinstance(start_date, date):
            start_date = start_date.strftime("%Y-%m-%d")
        if isinstance(end_date, date):
            end_date = end_date.strftime("%Y-%m-%d")

        start_time = time.time()
        stock = yf.download(company, start=start_date, end=end_date)
        elapsed_time = time.time() - start_time

        if debug:
            num_rows = stock.shape[0]
            num_cols = stock.shape[1]
            print(f"Stock data for    : {company}")
            print(f"Number of rows    : {num_rows}")
            print(f"Number of columns : {num_cols}")
            print(f"Elapsed time      : {elapsed_time:.2f} seconds")
            print("Fetched successfully.")
        return pd.DataFrame(stock)
    except Exception as e:
        print(f"Failed to fetch data for {company}: {str(e)}")
        return None
