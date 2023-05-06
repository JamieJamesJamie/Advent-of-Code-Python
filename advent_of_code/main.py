"""Main module to start the program from."""


from rich import box
from rich.console import Console
from rich.table import Table

from advent_of_code.helper.parse_args import ArgumentParser
from advent_of_code.helper.solve import solve


def main():
    """Main method."""

    args = ArgumentParser().parse_args()

    for year in args.years:
        table = Table(
            title="Advent of Code", show_lines=True, box=box.SQUARE_DOUBLE_HEAD
        )
        table.add_column("Year")
        table.add_column("Day")
        table.add_column("File")
        table.add_column("Part 1", no_wrap=True)
        table.add_column("Part 2", no_wrap=True)

        for day in args.days:
            for file in args.files:
                part1, part2 = solve(input_file=file, year=year, day=day)
                table.add_row(f"Year {year}", f"Day {day}", file.name, part1, part2)

        console = Console()
        console.print(table)


if __name__ == "__main__":
    main()
