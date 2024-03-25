p = [
    ["a", 1, "file1.py"],
    ["b", 2, "file2.py"],
    ["c", 3, "file3.py"],
    ["d", 4, "file4.py"],
    ["e", 5, "file5.py"],
    ["f", 6, "file6.py"],
]

def dcol():
    for col in p:
        yield col[0], col[1], col[2]

if __name__ == "__main__":
    for col in dcols():
        print(col)