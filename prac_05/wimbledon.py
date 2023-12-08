"""
estimate: 30 mins
actual: 40 mins
"""

def main():
    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()[1:]
        data = [line.strip().split(",") for line in data]
    champions = get_champions(data)
    countries = get_countries(data)
    champions_name(champions)
    print()
    countries_name(countries)

def get_champions(data):
    champions = {}
    for line in data:
        winner = line[2]
        if winner in champions:
            champions[winner] += 1
        else:
            champions[winner] = 1
    return champions

def get_countries(data):
    countries = set()
    for line in data:
        country = line[1]
        countries.add(country)
    return sorted(countries)

def champions_name(champions):
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")

def countries_name(countries):
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()
