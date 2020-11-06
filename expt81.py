#!/usr/bin/python3
with open("gg.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
