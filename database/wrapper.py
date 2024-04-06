
class wrapper:
    def __init__(self, db):
        self.db = db

    def insert(self, table, data):
        return self.db.insert(table, data)

    def select(self, table, where):
        return self.db.select(table, where)

    def update(self, table, data, where):
        return self.db.update(table, data, where)

    def delete(self, table, where):
        return self.db.delete(table, where)