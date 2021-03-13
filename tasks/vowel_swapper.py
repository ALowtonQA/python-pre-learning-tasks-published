def vowel_swapper(string):
    swaps = {"a": "4", "e": "3", "i": "!", "o": "ooo", "O": "000", "u": "|_|"}
    
    for c in swaps:
        replacement = swaps.get(c, c)
        if c in ("o", "O"):
            string = string.replace(c, replacement)
        else:
            string = string.replace(c, replacement).replace(c.upper(), replacement)
    return string
            
print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console