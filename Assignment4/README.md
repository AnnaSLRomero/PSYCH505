# Assignment 4

## Conditional Exercises
1)
```
response = "1"

if response == "1" or response == "2":
    print("OK")
    
elif response == "NaN":
    print("Subject did not respond")
    
else: print("Subject pressed the wrong key")   
```

2)
```
response = "1"

if response == "1" or response == "2":
    print("OK")
    if response == "1":
        print("Correct!")
    if response == "2":
        print("Incorrect!")
    
elif response == "NaN":
    print("Subject did not respond")
    
else: print("Subject pressed the wrong key")   
```

3) It does do what I want it to when I run it. 


## For Loop Exercises
1)
```
letters = ["A", "N", "N", "A"]

for i in letters:
    print(i)
```

2)
```
letters = ["A", "N", "N", "A"]
count = -1

for i in letters:
    print(i)
    count = count + 1
    print("This letter has a count of %i" %count) 
```

3)
```
names = ("Amy", "Rory", "River")

for i in names:
    if i == "Amy":
        print(names[0][0],
              names[0][1],
              names[0][2])
    
    elif i == "Rory":
        print(names[1][0],
              names[1][1],
              names[1][2],
              names[1][3])
    
    elif i == "River":
        print(names[2][0],
              names[2][1],
              names[2][2],
              names[2][3],
              names[2][4])
 ```

4)


## While Loop Exercises
1)

2)

3)
