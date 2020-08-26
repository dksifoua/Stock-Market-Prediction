__author__ = 'Dimitri K. Sifoua <dimitri.sifoua@gmail.com>'

import os
import tqdm
import argparse
import requests
import pandas as pd


def get_months_dates(year):
    date = [*map(lambda month: f'{year}{month:02d}', [*range(1, 13)])]

    start_dates = pd.to_datetime(date, format="%Y%m")
    end_dates = pd.to_datetime(date, format="%Y%m") \
        + pd.tseries.offsets.MonthEnd(1)

    start_dates = [*map(pd.Timestamp.date, start_dates)]
    end_dates = [*map(pd.Timestamp.date, end_dates)]

    return [*zip(start_dates, end_dates)]


def get_stock_prices(ticker, year, freq, token):
    data = []
    for (start_date, end_date) in tqdm.tqdm(
        get_months_dates(year=2019),
        desc=f"Download {year} {ticker} stock prices"
    ):
        request = f"https://api.tiingo.com/iex/{ticker}/prices?" + \
            f"startDate={start_date}&" + \
            f"endDate={end_date}&" + \
            f"resampleFreq={freq}&" + \
            f"token={token}&columns=open,high,low,close,volume"
        # print(request)
        data += requests.get(request).json()
    return pd.DataFrame.from_dict(data)


def save(ticker, year, freq, data, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, f'{year}_{ticker}_{freq}.csv')
    data.to_csv(path, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download & save stock price data'
    )
    parser.add_argument(
        '--tickers', action='store', type=str, default='S&P500',
        help='Tickers (comma separated values). Eg. AAPL,MSFT,WMT,GS. '
        'Default S&P500 (Will download all stock data)'
    )
    parser.add_argument(
        '--year', action='store', type=str, default='2019',
        help='Year (to download data). Default: 2019'
    )
    parser.add_argument(
        '--token', action='store', type=str, required=True, help='API token'
    )
    parser.add_argument(
        '--path', action='store', type=str, default='./data',
        help='Path to store data. Default: ./data'
    )
    parser.add_argument(
        '--freq', action='store', type=str, default='1min',
        help='Frequency ([min], [hour]) in which you want '
        'data resampled. Eg. 1min 5min 1hour. Default: 1min')

    args = parser.parse_args()

    if args.tickers == "S&P500":
        if os.path.exists(os.path.join(args.path, 'tickers-s&p500.csv')):
            tickers = pd.read_csv(
                os.path.join(args.path, 'tickers-s&p500.csv')
            ).Symbol.tolist()
        else:
            df = pd.read_html(
                'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
            )[0]
            if not os.path.exists(args.path):
                os.makedirs(args.path)
            df.to_csv(
                os.path.join(args.path, 'tickers-s&p500.csv'), index=False
            )
            tickers = df.Symbol.to_list()
    else:
        tickers = args.tickers.split(',')

    for i, ticker in enumerate(tickers):
        print(f'{i + 1}/{len(tickers)} ->')
        if os.path.exists(
            os.path.join(args.path, f'{args.year}_{ticker}_{args.freq}.csv')
        ):
            print(f'{args.year} {ticker} stock prices already downloaded!')
        else:
            data = get_stock_prices(ticker, args.year, args.freq, args.token)
            save(ticker, args.year, args.freq, data, args.path)
