ascii_list = [86,97,97,110,121,97,106,105,32,109,117,109,109,97,32,107,101,32,98,100,97,121,32,107,101,32,108,105,121,101,32,107,121,97,32,103,105,102,116,32,108,101,110,97,32,104,97,105,32,97,117,114,32,97,100,100,114,101,115,115,32,98,104,101,106,111,32,103,105,116,32,109,101]

result_string = ""

for ascii_value in ascii_list:
    result_string += chr(ascii_value)

print(result_string)