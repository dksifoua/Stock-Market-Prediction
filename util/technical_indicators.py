import ta


def add_momentum_indicators(data):
    df = data.copy()
    # Rate of Change (ROC)
    df['roc'] = ta.momentum.roc(close=df.close)
    # Relative Strength Index (RSI)
    df['rsi'] = ta.momentum.rsi(close=df.close)
    # True strength index (TSI)
    df['tsi'] = ta.momentum.tsi(close=df.close)
    return df


def add_volume_indicators(data):
    df = data.copy()
    # On Balance Volume (OBV)
    df['obv'] = ta.volume.on_balance_volume(close=df.close, volume=df.volume)
    # Volume-price trend (VPT)
    df['vpt'] = ta.volume.volume_price_trend(close=df.close, volume=df.volume)
    # Force Index (FI)
    df['fi'] = ta.volume.force_index(close=df.close, volume=df.volume)
    # Negative Volume Index (NVI)
    df['nvi'] = ta.volume.negative_volume_index(close=df.close,
                                                volume=df.volume)
    return df


def add_volatility_indicators(data):
    df = data.copy()
    bb_indicator = ta.volatility.BollingerBands(close=df.close)

    # Add Bollinger Bands features
    df['bb_bbm'] = bb_indicator.bollinger_mavg()
    df['bb_bbh'] = bb_indicator.bollinger_hband()
    df['bb_bbl'] = bb_indicator.bollinger_lband()
    # Add Bollinger Band high indicator
    df['bb_bbhi'] = bb_indicator.bollinger_hband_indicator()
    # Add Bollinger Band low indicator
    df['bb_bbli'] = bb_indicator.bollinger_lband_indicator()
    # Add Width Size Bollinger Bands
    df['bb_bbw'] = bb_indicator.bollinger_wband()
    return df


def add_trend_indicators(data):
    df = data.copy()
    aroon_indicator = ta.trend.AroonIndicator(close=df.close)
    macd_indicator = ta.trend.MACD(close=df.close)
    kst_indicator = ta.trend.KSTIndicator(close=df.close)

    # Aroon Down Channel
    df['aroon_down'] = aroon_indicator.aroon_down()
    # Aroon Indicator
    df['aroon'] = aroon_indicator.aroon_indicator()
    # Aroon Up Channel
    df['aroon_up'] = aroon_indicator.aroon_up()
    # MACD Line
    df['macd_line'] = macd_indicator.macd()
    # MACD Histogram
    df['macd_hist'] = macd_indicator.macd_diff()
    # MACD Signal Line
    df['macd_signal'] = macd_indicator.macd_signal()
    # Know Sure Thing (KST)
    df['kst'] = kst_indicator.kst()
    # Diff Know Sure Thing (KST)
    df['kst_diff'] = kst_indicator.kst_diff()
    # Signal Line Know Sure Thing (KST)
    df['kst_signal'] = kst_indicator.kst_sig()
    # Detrended Price Oscillator (DPO)
    df['dpo'] = ta.trend.dpo(close=df.close)
    # Exponential Moving Average (EMA)
    df['ema'] = ta.trend.ema_indicator(close=df.close)
    # Simple Moving Average (SMA)
    df['ema'] = ta.trend.sma_indicator(close=df.close)
    df['ema_30'] = ta.trend.sma_indicator(close=df.close, n=30)
    df['ema_60'] = ta.trend.sma_indicator(close=df.close, n=60)
    # Trix (TRIX)
    df['trix'] = ta.trend.trix(close=df.close)
    return df
