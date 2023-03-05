import psycopg2

# TODO: Class structure
# Create a class which has connect, update, fetch, delete as functions. These must be as general as possible with
# minimum code reuse.
# Methods:
#   1. Init : Take database, user, password, host, port as arguments in constructor.
#   2. Connect: Connect using the self. variables that we saved in constructor.
#   3. Fetch: Takes in string argument and performs query.
#   4. insert function: Can be used as it is initially, but later on try to automate this also.
#   5. Same goes for delete, update.


class DatabaseTable:

    def __init__(self, db, user, pwd, host, port):
        self.cur = None
        self.conn = None
        self.db = db
        self.user = user
        self.pwd = pwd
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.conn = psycopg2.connect(database=self.db,
                                         user=self.user,
                                         password=self.pwd,
                                         host=self.host,
                                         port=self.port)
            # creating the cursor object
            self.cur = self.conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while creating PostgreSQL table", error)

    def fetch_data_table(self, fetch_queries):
        for query in fetch_queries:
            self.cur.execute(query)
            result = self.cur.fetchall()
            print(query)
            for row in result:
                print(row)
            print()

    def insert_data_table(self, insert_queries):
        for insertquery in insert_queries:
            self.cur.execute(insertquery)
            print(insertquery, 'Inserted successfully!!')
        self.conn.commit()

    def delete_data_table(self, delete_queries):
        for query in delete_queries:
            self.cur.execute(query)
            print("Deleted successfully!!")
        self.conn.commit()

    def update_data_table(self, queries):
        for query in queries:
            self.cur.execute(query)
            self.conn.commit()
            print(query, ': Update operation completed successfully')

