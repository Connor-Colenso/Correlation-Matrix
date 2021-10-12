import pandas as pd


def sp500_stocks():
    """
    :return: Returns a list of all the companies in the S&P 500 index.
    """
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

    return tuple(table[0]['Symbol'])
