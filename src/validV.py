def validV(str):
    if str=='' or str[0].isdigit()==True:
        return False
    for i in str:
        if i.isdigit() or i=='_' or i.isalpha():
            continue
        else:
            return False
    return True
print(validV(""))