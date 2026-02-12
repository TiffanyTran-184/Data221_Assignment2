def find_lines_containing(filename, keyword):
    with open("sample-file.txt", mode="r") as file:

        for line in filename:
            # case-insensitive search
            matches = []
            line_number = 1
            if keyword.lower() in line.lower():
                matches.append((line_number, line.strip()))

            line_number += 1  # increase line number for each line

        return matches

results = find_lines_containing("sample-file.txt", "lorem")
print("Number of matching lines:", len(results))

print("First 3 matching lines:")
for line_info in results[:3]:
    print(line_info[0], "->", line_info[1])
