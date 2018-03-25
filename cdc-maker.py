cdc_map = {
    'A' : 23,
    'B' : 47,
    'I' : 397,
    'L' : 507,
    'O' : 581,
    'P' : 635,
    'R' : 687,
    'U' : 763,
    'Y' : 901,
    '0' : 405,
    '1' : 73,
    'E' : -1,
    'N' : -1,
    'D' : -1
}

message = ""
while not message.upper() == "END":
    message = input("Enter your code: ")
    cdc_code = 0

    for char in message:
        cdc_code = cdc_code + int(cdc_map[char.upper()])
        cdc_code = cdc_code * 521
        cdc_code = cdc_code % 10000
        cdc_code = cdc_code + 450
        cdc_code = cdc_code % 967

    print(cdc_code)
