def transform_data(data):
    for row in data:
        row['name'] = row['name'].capitalize()  # Capitalize names
    return data
