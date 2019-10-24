#List creation and searching
names  = []
count=0
while count<10:
    name=input ("Enter a name:")
    names.append(name)
    count+=1
print (names)

print("Enter a name or type 'End' to end the program")
EndProg=False
while (EndProg!=True):
    search=input ("Search for a name:")
    if search in names:
        print(search, "was found")
    elif search=="End":
        print ("Thank you for testing the program!")
        EndProg=True
    else:
        print (search, "was not found")






