def brackets(given):
    while len(given)!=0:
        given=given.replace("()","")
        given=given.replace("[]","")
        given=given.replace("{}","")
    if len(given)==0:
        return True
    else:
        return False
str=input()
print(brackets(str))
