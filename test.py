from preprocessing import MissingValueProcessor
from food_statistics import Statistics

data = {
    'idade': [20, 30, None, 50],
    'salario': [500, None, 800, 1200],
    'cidade': ['A', 'B', 'C', None],
    'cat': ['A', 'B', 'A', None]
}

processor = MissingValueProcessor(data)

# result_all_cols = processor.isna()
# print("Testes para funcao isna")
# print(processor.isna())
# print(len(processor.isna(columns={'idade'})['idade']))
# print(len(result_all_cols['idade']))
# print("Testes para funcao notna")
# result_notna = processor.notna(columns={'idade', 'salario'})
# print(result_notna)
# print(len(result_notna['idade']))
# print(len(result_notna['idade']))
# print(len(result_notna['salario']))
# processor.fillna(columns={'cat'}, method='mode')
# print(processor.dataset['cat'][3])
# processor.fillna(columns={'idade'}, method='mean')
# print(processor.dataset['idade'][2])
# print(processor.dropna(columns={'cidade'}))
# print(processor.dataset['idade'])

print(processor.fillna(method='default_value', default_value=100))
