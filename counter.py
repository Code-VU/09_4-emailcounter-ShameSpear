def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    fromDict = {}
    with open(name) as file:
        for line in file:
            # line = line.strip

            if line.startswith("From "):
                sender = line.split()[1]
                if sender not in fromDict:
                    fromDict[sender] = 1
                else:
                    fromDict[sender] += 1
    # print(emails)
    # print(max(fromDict), max(fromDict.values()))
    dict_vals = fromDict.values()
    max_val = max(dict_vals)

    print(max(fromDict, key=fromDict.get), max_val)

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
