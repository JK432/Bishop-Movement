# Given an empty chess board and one Bishop placed in any square, say (r,c) generate the list of all squares the Bishop could not move to 
x=int(input())
y=int(input())

if(x==8 and y==1):
    print(x-1,y)
    print(x,y+1)
if(x==8 and y==8):
    print(x-1,y)
    print(x,y-1)
if(x==1 and y==1):
    print(x+1,y)
    print(x,y+1)
if(x==1 and y==8):
    print(x+1,y)
    print(x,y-1)
if(x==1 and y<8 and y>1):
    print(x+1,y)
    print(x,y-1)
    print(x,y+1)
if(y==1 and x<8 and x>1):
    print(x+1,y)
    print(x-1,y)
    print(x,y+1)
if(x==8 and y<8 and y>1):
    print(x-1,y)
    print(x,y-1)
    print(x,y+1)
if(y==8 and x<8 and x>1):
    print(x+1,y)
    print(x-1,y)
    print(x,y-1)
if(y<8 and y>1 and x<8 and x>1):
    
    print(x,y-1)  #1
    print(x,y+1)  #2
    print(x+1,y) #3
    print(x-1,y)  #4
    
    
   