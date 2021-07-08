from typing import Iterator, Any

def lines(path: str) -> Iterator[str]:
    with open(path) as f:
        for line in f:
            yield line

def parse_csv(lines: Iterator[str]) -> Iterator[list[str]]:
    for line in lines:
        yield line.replace("\n ", "  ").split(',')
print(list(parse_csv(["Datum,Verwendungszweck,Betrag",
"30.12.2020,Bafoeg-Foerdergeld,+514.00"])))

