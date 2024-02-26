import random


quotes_path = "C:\\users\\peturdaniel\\Documents\\Pétur Pers\\quotes.txt"


def random_line():
    lines: list = []
    with open(quotes_path, "r", encoding="utf-8") as f:
        x = f.readline()
        for x in f:
            lines.append(x)
    print(random.choice(lines))


# Virkilega handy function !
def combine_lines(file_path):
    """Þetta sameinar línur í eina línu, ef að tóm lína er á milli"""
    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    combined_lines = []
    current_line = ''

    for line in lines:
        if line.strip() == '':
            if current_line:
                combined_lines.append(current_line.strip())
                current_line = ''
        else:
            current_line += ' ' + line.strip()

    if current_line:
        combined_lines.append(current_line.strip())

    return combined_lines

# Example usage:
combined_lines = combine_lines(quotes_path)
for line in combined_lines:
    print(line)

