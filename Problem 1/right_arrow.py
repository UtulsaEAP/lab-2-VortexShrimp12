def right_arrow():
    base_char = input()
    head_char = input()

    row1 = '      ' + head_char
    ''' Type your code here. '''
    row1 = head_char
    row2 = head_char + head_char
    row3 = head_char + head_char + head_char
    lines = [row1, row2, row3]
    lineNumber = 0
    maxLength = 0
    amountOfBase = 0

    while amountOfBase < 5:
        if amountOfBase < 1:
            base = "      "
        else:
            base = base_char + base_char + base_char + base_char + base_char + base_char
        print(base + lines[lineNumber])
        if lineNumber < 2 and maxLength < 2:
            lineNumber = lineNumber + 1 
            maxLength = maxLength + 1
        else:
            lineNumber = lineNumber - 1
        amountOfBase = amountOfBase + 1

if __name__ == "__main__":
    right_arrow()