"""."""
import psycopg2


def main():
    conn = psycopg2.connect("dbname=meszi user=meszi")
    cur = conn.cursor()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
