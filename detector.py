SQL_ERRORS = [
    "sql syntax",
    "mysql",
    "sqlite",
    "postgresql",
    "oracle",
    "syntax error"
]

def detect_sql_error(response_text):
    response_text = response_text.lower()

    for error in SQL_ERRORS:
        if error in response_text:
            return True

    return False
