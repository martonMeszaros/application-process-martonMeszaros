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
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            pass
        elif user_input == "6":
            pass
        elif user_input == "7":
            pass

    cur.close()
    conn.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
