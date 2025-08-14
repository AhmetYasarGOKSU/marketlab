from marketlab.core.indicators import sma
def test_sma_basics():
    data = [1,2,3,4,5]
    result = sma(data, period=3)
    assert result == [2.0, 3.0, 4.0]

test_sma_basics()