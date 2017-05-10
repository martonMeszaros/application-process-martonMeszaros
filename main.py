"""."""
import psycopg2

import menu_sys
import querries


def main():
    """."""
    conn = psycopg2.connect("dbname=meszi user=meszi")
    cur = conn.cursor()

    running = True
    while running:
        user_input = menu_sys.menu()
        if user_input == "0":
            running = False
            break
        elif user_input == "1":
            cur.execute(querries.querries()[0][1])
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
