from preprocessing import MissingValueProcessor

data = {
    'idade': [20, 30, None, 50],
    'salario': [500, None, 800, 1200],
    'cidade': ['A', 'B', 'C', None]
}

processor = MissingValueProcessor(data)
print(processor.isna())
