def normalize(line):
    result = ""
    for char in line:
        char = char.lower()
        if char.isalnum():
            result += char
    return result


file = open(file="sample-file.txt", mode="r")
lines = file.readlines()
normalizedLines = {} # dictionary that holds all the line position of near-duplicate lines e.g: {"data":[1,3,4,5]}
for i in range(len(lines)):
    normalizedLine= normalize(lines[i].strip())
    if normalizedLine not in normalizedLines:
        normalizedLines[normalizedLine] = []
    if normalizedLine == "":
        pass
    else:
        normalizedLines[normalizedLine].append(i+1) # line in the sample-file

nearDuplicateSets = []
for normalizeLine, lineNumber in normalizedLines.items():
    if len(lineNumber) >= 2:
        nearDuplicateSets.append(lineNumber)
#Print nunmber of such set
print("Number of near-duplicate sets:", len(nearDuplicateSets))

# Print first 2 set you find,  including line numbers and original lines.
for duplicateSet in nearDuplicateSets[:2]:
    for lineNumber in duplicateSet:
        print(lineNumber, "-> ", normalize(lines[lineNumber-1].strip()))