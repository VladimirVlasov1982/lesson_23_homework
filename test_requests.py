import requests


def get_filter_map():
    url = "http://127.0.0.1:5000/perform_query"

    payload = {
        "file_name": "apache_logs.txt",
        "cmd1": "filter",
        "value1": "POST",
        "cmd2": "map",
        "value2": "0"
    }

    response = requests.request(method="POST", url=url, data=payload)
    print("===filter_map===")
    print(response.text)
    print("")


def get_unique_map():
    url = "http://127.0.0.1:5000/perform_query"

    payload = {
        'file_name': 'apache_logs.txt',
        'cmd1': 'unique',
        'value1': '',
        'cmd2': 'sort',
        'value2': 'asc'
    }

    response = requests.request("POST", url, data=payload)
    print(response.text)


if __name__ == "__main__":
    get_filter_map()
    get_unique_map()
