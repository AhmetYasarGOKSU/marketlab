from marketlab.core.indicators import sma

data = [10, 20, 30, 40, 50]
period = 3

sma_values = sma(data, period)

print("Sma values:", sma_values)