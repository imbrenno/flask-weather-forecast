from main.database.database import get_db

class Users:
    def __init__(self, username, email):
        self.username = str(username)
        self.email = str(email)

    def save(self):
        db = get_db()
        result = db.users.insert_one(
            {
                "username": self.username,
                "email": self.email,
            }
        )
        print(f"result: {result.inserted_id}")

    @staticmethod
    def get_all():
        db = get_db()
        return list(db.users.find())

    @staticmethod
    def get_one(document):
        db = get_db()
        return db.users.find_one(
            {"username": document},
        )

    @staticmethod
    def delete(document):
        db = get_db()
        query_filter = {
            "username": document,
        }
        result = db.users.delete_one(query_filter)
        print(f"Detele in users, total of delected: {result.deleted_count}")

    @staticmethod
    def update(document, data):
        db = get_db()
        query_filter = {
            "username": document,
        }
        result = db.users.update_one(
            query_filter,
            {"$set": data},
        )
        print(f"Update in users, total of update: {result.modified_count}")
