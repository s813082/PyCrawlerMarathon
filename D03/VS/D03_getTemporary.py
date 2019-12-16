# File I/O
with open("./Doc/example/64_72hr_CH.xml", "r", encoding="utf-8") as fh:
    xml = fh.read()
print(xml)