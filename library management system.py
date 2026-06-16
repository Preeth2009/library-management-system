a=[]
b=[]
def add(a):
    c=input("Enter book name:",)
    a.append(c)
    print("Book added successfully")

def view(a,b):
    print("----- Book List -----")
    print()
    if (len(a)+len(b))!=0:
        if len(a)!=0:
            for i in a:
                print(i,"- Available")
        if len(b)!=0:
            for j in b:
                print(j,"- Borrowed")
    else:
        print("No books found.")

def borrow(a,b):
    d=input("Enter book name:")
    if d in b:
        print("Book is alredy borrowed.")
    elif d in a:
        e=a.index(d)
        a.pop(e)
        b.append(d)
        print("Book borrowed successfully!")
    else:
        print("Book not found.")

def retun(a,b):
    f=input("Enter book name:")
    if f in a:
        print("Book is already available.")
    elif f in b:
        g=b.index(f)
        b.pop(g)
        a.append(f)
        print("Book returned successfully")
    else:
        print("Book not found.")

def exi():
    print("Thank you for using Library Management System")

while True:
    print("===== Library Management System=====")
    print()
    print("1.Add Book")
    print("2.View Books")
    print("3.Borrow Book")
    print("4.Return Book")
    print("5.Exit")
    print()
    k=int(input("Enter choice:"))
    if k==1:
        add(a)
    elif k==2:
        view(a,b)
    elif k==3:
        borrow(a,b)
    elif k==4:
        retun(a,b)
    elif k==5:
        exi()
        break
        
    
        







        

    
    
