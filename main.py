"""."""
import psycopg2

import menu_sys
import printer
import querries


def set_records(cur):
    records = []
    for record in cur:
        records.append(record)
    return records


def main():
    """."""
    conn = psycopg2.connect("dbname=meszi user=meszi")
    cur = conn.cursor()

    running = True
    while running:
        records = []
        user_input = menu_sys.menu()
        if user_input == "0":
            running = False
            break
        elif user_input == "1":
            cur.execute(querries.querries()[0][1])
            records = set_records(cur)
            printer.print_table(querries.querries()[0][0], records)
        elif user_input == "2":
            cur.execute(querries.querries()[1][1])
            records = set_records(cur)
            printer.print_table(querries.querries()[1][0], records)
        elif user_input == "3":
            cur.execute(querries.querries()[2][1])
            records = set_records(cur)
            printer.print_table(querries.querries()[2][0], records)
        elif user_input == "4":
            cur.execute(querries.querries()[3][1])
            records = set_records(cur)
            printer.print_table(querries.querries()[3][0], records)
        elif user_input == "5":
            cur.execute(querries.updates()[0])
            cur.execute(querries.querries()[4][1])
            records = set_records(cur)
            printer.print_table(querries.querries()[4][0], records)
        elif user_input == "6":
            cur.execute(querries.updates()[1])
            cur.execute(querries.querries()[5][1])
            records = set_records(cur)
            printer.print_table(querries.querries()[5][0], records)
        elif user_input == "7":
            cur.execute(querries.updates()[2])
        conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
