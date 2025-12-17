class MockDB:
    def upsert(self, table, data):
        print(f"[DB UPSERT] Table: {table}, Data: {data}")


def db_connection():
    return MockDB()