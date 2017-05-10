"""."""


def print_table(columns, records):
    col_widths = []
    padding = 4
    # Set baseline column width based on headers.
    for column in columns:
        col_widths.append(len(column) + padding)
    # Override column widths if an entry is longer.
    for record in records:
        for index, column in enumerate(record):
            if len(str(column)) + padding > col_widths[index]:
                col_widths[index] = len(str(column)) + padding
    # Print out table headers
    for index, column in enumerate(columns):
        print("{:^{}}".format(column, col_widths[index]), end="")
    print()
    # Print records
    for record in records:
        for index, column in enumerate(record):
            print("{:<{}}".format(column, col_widths[index]), end="")
        print()
    print()
