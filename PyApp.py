import pandas as pd

# Пример данных для продуктов
products_data = [
    (1, "Product A"),
    (2, "Product B"),
    (3, "Product C"),
    (4, "Product D"),
]

# Пример данных для категорий
categories_data = [
    (1, "Category 1"),
    (2, "Category 2"),
    (1, "Category 3"),
]

# Пример данных для связей продуктов и категорий
product_category_data = [
    (1, 1),  # Product A - Category 1
    (1, 2),  # Product A - Category 2
    (2, 1),  # Product B - Category 1
    (2, 3),  # Product B - Category 3
]

# Создание DataFrame для продуктов
products_df = pd.DataFrame(products_data, columns=['product_id', 'product_name'])

# Создание DataFrame для категорий
categories_df = pd.DataFrame(categories_data, columns=['category_id', 'category_name'])

# Создание DataFrame для связей продуктов и категорий
product_category_df = pd.DataFrame(product_category_data, columns=['product_id', 'category_id'])

# Объединение данных по ключам (product_id и category_id)
merged_df = product_category_df.merge(products_df, on='product_id').merge(categories_df, on='category_id')

# Вывод результата
print(merged_df)
