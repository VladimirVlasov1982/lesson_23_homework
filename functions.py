def filter_query(param, data):
    return list(filter(lambda v: param in v, data))


def map_query(param, data):
    column_number = int(param)
    return list(map(lambda v: v.split(' ')[column_number], data))


def unique_query(data, *args, **kwargs):
    return list(set(data))


def sorted_query(param, data):
    reverse = True if param == 'desc' else False
    return sorted(data, reverse=reverse)

def limit_query(param, data):
    limit = int(param)
    return list(data)[:limit]
