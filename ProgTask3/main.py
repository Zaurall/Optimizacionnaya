from north_west import north_west
from vogel import vogel
from russell import russell
from input import S, C, D
from tabulate import tabulate


def print_input_table(S, C, D):
    table_data = []
    for i, row in enumerate(C):
        table_row = [f"S{i + 1}"] + list(row) + [S[i]]
        table_data.append(table_row)

    table_data.append(["Demand"] + list(map(str, D)) + ["480"])

    table_headers = [""] + [f"D{j + 1}" for j in range(len(D))] + ["Supply"]
    print(tabulate(table_data, headers=table_headers, tablefmt="grid"))


def main():
    print_input_table(S, C, D)
    north_west(S, C, D)
    vogel(S, C, D)
    russell(S, C, D)


if __name__ == "__main__":
    main()
