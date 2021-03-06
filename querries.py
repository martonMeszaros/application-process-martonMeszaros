"""."""


def updates():
    """."""
    return [
        ("INSERT INTO applicants "
         "(first_name, last_name, phone_number, email, application_code) "
         "VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', '54823');"),

        ("UPDATE applicants "
         "SET phone_number='003670/223-7459' "
         "WHERE first_name='Jemima' AND last_name='Foreman';"),

        ("DELETE FROM applicants "
         "WHERE email LIKE '%@mauriseu.net';")
    ]


def querries():
    """."""
    return [
        [
            ["first_name", "last_name"],
            ("SELECT first_name, last_name "
             "FROM mentors;")
        ],
        [
            ["nick_name"],
            ("SELECT nick_name "
             "FROM mentors "
             "WHERE city='Miskolc';")
        ],
        [
            ["full_name", "phone_number"],
            ("SELECT first_name||' '||last_name, phone_number "
             "FROM applicants "
             "WHERE first_name='Carol';")
        ],
        [
            ["full_name", "phone_number"],
            ("SELECT first_name||' '||last_name, phone_number "
             "FROM applicants "
             "WHERE email LIKE '%@adipiscingenimmi.edu';")
        ],
        [
            ["ID", "first_name", "last_name", "phone_number", "email", "application_code"],
            ("SELECT * "
             "FROM applicants "
             "WHERE application_code='54823';")
        ],
        [
            ["phone_number"],
            ("SELECT phone_number "
             "FROM applicants "
             "WHERE first_name='Jemima' AND last_name='Foreman';")
        ]
    ]
