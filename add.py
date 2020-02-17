import json
from connect import PostgresDB
from errors import Error


class Add:
    def __init__(self, request):
        super().__init__()
        values = request.get_json()
        self.user_id = values.get("id")
        self.to_url = values.get("to_url")
        self.data = values.get("data")
        self.type = values.get("type")
        self.correct_data = True
        self._add_to_db()

    def _add_to_db(self):
        if self._check_values():
            with PostgresDB() as cursor:
                query = f"insert into queue(to_url, type, data, user_id) values (%s, %s, %s, %s)"
                cursor.execute(query, (
                    self.to_url,
                    self.type,
                    json.dumps(self.data),
                    self.user_id
                ))
            return True

    def _check_values(self):
        if not (self.user_id and self.to_url and self.data and self.type):
            Error("Please provide all the values", 400)
            self.correct_data = False
            self.message = "Please provide all the values"
            return False
        return True
