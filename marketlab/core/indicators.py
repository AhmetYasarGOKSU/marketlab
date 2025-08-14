
def sma(data, period):
    """
    Calculate Simple Moving Average (SMA) for a list of numbers.

    Args:
        data: list of numbers (floats or ints)
        period: window size for moving average

    Returns:
        List of SMA values
    """
    if period <= 0:
        raise ValueError("Period must be a positive integer")
    if period > len(data):
        raise ValueError("Period cannot be larger than data length")

    total = sum(data[0: period])
    result = [total/period]
    length = len(data)
    for i in range(length-period):
        total = total - data[i] + data[i+period]
        result.append(total/period)

    return result


