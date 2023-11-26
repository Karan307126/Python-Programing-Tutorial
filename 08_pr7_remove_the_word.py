def remove_and_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

this="    Karan is good boy    "
n=remove_and_split(this,"Karan")
print(n)