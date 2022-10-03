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

for name in names:
    print(name)
    for letter in name:
        print(letter)
 ```

4)
```
names = ("Amy", "Rory", "River")
count = 0

for name in names:
    print(name)
    letterCount = -1
    for letter in name:
        letterCount = letterCount + 1
        print(letter)
        print("This letter has a count of %i" %letterCount)
  ```


## While Loop Exercises
1)
```
counter = 1
while counter <= 10:
    print("image1.png")
    print(counter)
    counter = counter + 1
while counter <= 20:
    print("image2.png")
    print(counter)
    counter = counter + 1
```

2)
```
response = False
iteration = 0

while not response:
    print("image.png")
    iteration = iteration + 1
    print("iteration %i" %iteration)
    if random.randint(0,3) == 1 or random.randint(0,3) == 2:
        response == True
        break
```

3)
```
response = False
failsafe = -1

while not response:
    failsafe = failsafe + 1
    if failsafe == 5:
        break
    print("image.png")
    if random.randint(0,3) == 1 or random.randint(0,3) == 2:
        response == True
```        
