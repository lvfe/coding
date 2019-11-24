def retatestr(str, n):
    if n== 0:
        return str
    else:
        n=n+1
        return str[n:]+str[:n]

print(retatestr("abcdefg",3))