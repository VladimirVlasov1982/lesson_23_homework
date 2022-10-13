import functions

CMD_VALID_PARAM = {
    "filter": functions.filter_query,
    "map": functions.map_query,
    "unique": functions.unique_query,
    "sort": functions.sorted_query,
    "limit": functions.limit_query,
}


def file_reader(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line


def build_query(req):
    data = file_reader(f"data/{req.get('file_name')}")
    result = CMD_VALID_PARAM[req.get('cmd1')](param=req.get('value1'), data=data)
    result = CMD_VALID_PARAM[req.get('cmd2')](param=req.get('value2'), data=result)
    return result


query = {
    "file_name": "apache_logs.txt",
    "cmd1": "filter",
    "value1": "POST",
    "cmd2": "map",
    "value2": "0"
}
