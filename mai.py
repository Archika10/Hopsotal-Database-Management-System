import argparse
from helper import DatabaseTable


def read_queries(file):
    with file as f:
        for line in f:
            yield line.strip()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to fetch data from a database')
    parser.add_argument('--database', type=str, default='hospital_management')
    parser.add_argument('--user', type=str, default='postgres')
    parser.add_argument('--password', type=str, default='fixit')
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=5432)
    parser.add_argument('--filename', type=argparse.FileType('r'), default='queries.txt')
    args = parser.parse_args()

    obj = DatabaseTable(args.database, args.user, args.password, args.host, args.port)

    obj.connect()

    queries = read_queries(args.filename)
    first_query = next(queries, None)
    if first_query and 'SELECT' in first_query.upper():
        obj.fetch_data_table([first_query] + list(queries))
    elif first_query and 'INSERT' in first_query.upper():
        obj.insert_data_table([first_query] + list(queries))
    elif first_query and 'DELETE' in first_query.upper():
        obj.delete_data_table([first_query] + list(queries))
    else:
        obj.update_data_table([first_query] + list(queries))


