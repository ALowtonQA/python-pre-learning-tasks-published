def vowel_swapper(string):
    swaps = {"a": "4", "e": "3", "i": "!", "o": "ooo", "O": "000", "u": "|_|"}
    str_list = list(string) 

    for key in swaps: 
        val = -1
        for _ in range(0, 2): 
            val = string.lower().find(key, val + 1)
        if val == -1:
            continue
        if str_list[val] == "o":
            str_list[val] = swaps.get("o")
        elif str_list[val] == "O":
            str_list[val] = swaps.get("O")
        else:
            str_list[val] = swaps.get(key, key)
  
    return ''.join(str_list)

print(vowel_swapper("aAa eEe iIi oOo uUu")) # Should print "a4a e3e i!i o000o u|_|u" to the console
print(vowel_swapper("Hello World")) # Should print "Hello Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "Ev3rything's Av4!lable" to the console