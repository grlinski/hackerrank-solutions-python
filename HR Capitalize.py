

# Capitalize


def capitalize(s):

    ns = s[0].upper()
    for i in range(1,len(s)):
        if s[i-1] == ' ' and s[i].islower():
            ns = ns+s[i].upper()
        else:
            ns = ns+s[i]
    return (ns)










print(capitalize("aaaa bbb ccc sss"))









