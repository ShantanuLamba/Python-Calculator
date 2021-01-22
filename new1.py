print("Welcome to SL Calculator")
print("Choose between Addition, Subtraction, Multiplication, Division")
print("Enter a for addition")
print("Enter m for multiplication")

operation = input()
#addition code -
if operation == "a":
    print("How many numbers you want to add?")
    anumber = input()
    anumber = int(anumber)
    alist = []
    awhilevar = 1
    while(awhilevar < anumber or awhilevar == anumber):
        if awhilevar == 1:
            print("Enter 1st number to add")
        elif awhilevar == 2:
            print("Enter 2nd number to add")
        elif awhilevar == 3:
            print("Enter 3rd number to add")
        else:
            print("Enter",awhilevar,"th number to add")
        awhilevardigit = input()
        awhilevardigit = int(awhilevardigit)
        alist.append(awhilevardigit)
        awhilevar += 1
    awhilevar2 = 0
    addnumber = 0
    while(awhilevar2 < anumber):
        addnumber = alist[awhilevar2] + addnumber
        awhilevar2 += 1
    print("The answer is",addnumber)

#multiplication code
if operation == "m":
    print("How many numbers you want to multiply?")
    mnumber = input()
    mnumber = int(mnumber)
    mlist = []
    mwhilevar = 1
    while(mwhilevar < mnumber or mwhilevar == mnumber):
        if mwhilevar == 1:
            print("Enter 1st number to multiply")
        elif mwhilevar == 2:
            print("Enter 2nd number to multiply")
        elif mwhilevar == 3:
            print("Enter 3rd number to multiply")
        else:
            print("Enter",mwhilevar,"th number to multiply")
        mwhilevardigit = input()
        mwhilevardigit = int(mwhilevardigit)
        mlist.append(mwhilevardigit)
        mwhilevar += 1
    mwhilevar2 = 0
    multiplynumber = 1
    while (mwhilevar2 < mnumber):
        multiplynumber = mlist[mwhilevar2] * multiplynumber
        mwhilevar2 += 1
    print("The answer is", multiplynumber)


            










