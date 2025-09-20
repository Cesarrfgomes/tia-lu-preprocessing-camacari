from preprocessing import MissingValueProcessor

data = {
    'coluna1': [1, 2, 3, None, 5],
    'coluna2': [None, 2, 3, 4, 5],
    'coluna3': [1, 2, 3, 4, None]
}

processor = MissingValueProcessor(data)
print(processor.isna(columns={'coluna1', 'coluna2', 'coluna3'}))
