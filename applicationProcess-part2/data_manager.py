import os

import psycopg2


def database_connection(function):
    """Wrapper for each function to have it's own database connection.
    Copied over from the AskMate by SzószKód
    """
    def wrapper(*args, **kwargs):
        global _cursor
        _db_connection = None
        _cursor = None
        connection_data = {
            "dbname": os.environ.get("MY_PSQL_DBNAME"),
            "user": os.environ.get("MY_PSQL_USER"),
            "host": os.environ.get("MY_PSQL_HOST"),
            "password": os.environ.get("MY_PSQL_PASSWORD")
        }
        connect_string = "dbname='{dbname}' user='{user}' host='{host}' password='{password}'"
        connect_string = connect_string.format(**connection_data)
        _db_connection = psycopg2.connect(connect_string)
        _db_connection.autocommit = True
        _cursor = _db_connection.cursor()
        result = function(*args, **kwargs)
        _cursor.close()
        _db_connection.close()
        return result
    return wrapper


@database_connection
def mentors():
    query_string = ("SELECT mentors.first_name, "
                    "       mentors.last_name, "
                    "       schools.name, "
                    "       schools.country "
                    "FROM mentors "
                    "LEFT JOIN schools "
                    "ON mentors.city = schools.city "
                    "ORDER BY mentors.id ASC;")
    _cursor.execute(query_string)
    return _cursor.fetchall()


@database_connection
def all_school():
    query_string = ("SELECT mentors.first_name, "
                    "       mentors.last_name, "
                    "       schools.name, "
                    "       schools.country "
                    "FROM mentors "
                    "FULL JOIN schools "
                    "ON mentors.city = schools.city "
                    "ORDER BY mentors.id ASC;")
    _cursor.execute(query_string)
    return _cursor.fetchall()


@database_connection
def mentors_by_country():
    query_string = ("SELECT schools.country, "
                    "       COUNT(mentors.id) as count "
                    "FROM schools "
                    "LEFT JOIN mentors "
                    "ON schools.city = mentors.city "
                    "GROUP BY schools.country "
                    "ORDER BY schools.country ASC;")
    _cursor.execute(query_string)
    return _cursor.fetchall()


@database_connection
def contacts():
    query_string = ("SELECT schools.name, "
                    "       mentors.first_name, "
                    "       mentors.last_name "
                    "FROM schools "
                    "INNER JOIN mentors "
                    "ON schools.contact_person = mentors.id "
                    "ORDER BY schools.name ASC;")
    _cursor.execute(query_string)
    return _cursor.fetchall()


@database_connection
def applicants():
    query_string = ("SELECT applicants.first_name, "
                    "       applicants.application_code, "
                    "       applicants_mentors.creation_date "
                    "FROM applicants "
                    "INNER JOIN applicants_mentors "
                    "ON applicants.id = applicants_mentors.applicant_id "
                    "ORDER BY applicants_mentors.creation_date DESC;")
    _cursor.execute(query_string)
    return _cursor.fetchall()


@database_connection
def applicants_and_mentors():
    query_string = ("SELECT applicants.first_name, "
                    "       applicants.application_code, "
                    "       mentors.first_name, "
                    "       mentors.last_name "
                    "FROM applicants "
                    "FULL JOIN applicants_mentors "
                    "ON  applicants.id = applicants_mentors.applicant_id "
                    "   LEFT JOIN mentors "  # We want to display the record even if there's no connection to mentors
                    "   ON applicants_mentors.mentor_id = mentors.id "
                    "ORDER BY applicants.id;")
    _cursor.execute(query_string)
    return _cursor.fetchall()
