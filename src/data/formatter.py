def format_item(data):
    if isinstance(data, str):
        return f"'{data}'"
    return str(data)


def format_dict(data):
    items = []
    for k, v in data.items():
        items.append(f'{k}={format_item(v)}')
    return items
