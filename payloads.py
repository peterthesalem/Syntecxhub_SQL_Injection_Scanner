"""
SQL Injection payloads for authorized testing only.
"""

SQL_PAYLOADS = [
    "'",
    '"',
    "' OR '1'='1",
    "' OR 1=1 --",
    "' UNION SELECT NULL --",
]
