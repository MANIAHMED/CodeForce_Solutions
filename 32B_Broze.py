inp=list((input()))

j=0
temp=[]
ans=[]
for i in inp:

    if i == "-" and temp == []:
        temp.append(i)
    elif i == "-" and "-" in temp:
        ans.append("2")
        temp.clear()


    elif i == "." and temp == []:
        ans.append("0")

    elif i =="." and "-" in temp:
        ans.append("1")
        temp.clear()

ans="".join(ans)
print(ans)

