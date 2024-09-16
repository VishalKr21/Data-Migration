def validate_data(data):
    for row in data:
        if row['id'] is None or row['name'] is None:
            raise ValueError(f"Invalid data: {row}")
    return True
