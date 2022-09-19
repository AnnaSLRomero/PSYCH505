# Assignment 2
### Anna Romero

```
import numpy as np
import pprint as pp
```

## Print Exercises
```
  print("A")
  print("N")
  print("N")
  print("A")
```
No, the variables did not show up in the variable editor.

## Operation Exercises

1) Yes, I did get the same result for both these operations.
```
print(5/2)
print(5.0/2.0)
```

2) The modulo operator prints out the the remainder when the first number is divided in the second number.
```
print(4%2)
print(10%2)
print(7%3)
print(20%3)
```

3) The ** operator gives us the answer if the first number was to the power of the second number.
```
print(5**10)
print(4**2)
```
The // operator tells us how much the second number goes into the first number and rounds down, not providng a reminder if there was one.
```
print(4//2)
print(16//4)
print(25//5)
print(25//2)
```

4) Python does follow PEDMAS rules of operations.
```
print(7-4*3)
print(5+2+3*3/9)
```

## Variable Exercises
1) Yes, the variables do show up in the variable editor.
  ```
   letter1 = "A"
   letter2 = "N"
   letter3 = "N"
   letter4 = "A"
  ```

2) 
  ```
   letter1 = "A"
   letterX = "N"
   letter3 = "N"
   letter4 = "A"
  ```
   Python does not have a problem with 2 or more different variables having the same value.

3) 
  ```
   letter1 = "A"
   letterX = "K"
   letter3 = "N"
   letter4 = "A"
  ```
Changing the value of letterX did not change the value of other variables, but it did change the value of the variable letterX.

4) 
```
   letter1 = "A"
   letterX = letter3
   letter3 = "N"
   letter4 = "A"
   
   letter1 = "A"
   letterX = letter3
   letter3 = "Z"
   letter4 = "A"
 ```
Changing the value of letter1 did change the value of letterX. This tell us that equating a variable (e.g., letterX) with another variable (e.g., letter3), will give them the same value, depending on which variable is equated to the value.
   
## Boolean Exercises
1)
```
print(1 == 1.0)
print("1" == "1.0")
```
The floats are equivalent, but the strings are not equivalent. The numerical value is equivalent with 1 and 1.0, but as character strings "1" and "1.0" are not the same, namely 1.0 has a decimal and a 0, which 1 does not have.

2)
```
print(5 == (3+2))
```
Yes, they are equivalent, because it outputs TRUE.

3)
```
print((1 == 1.0) and not ("1" == "1.0") and (5 == (3+2)))
print((1 == 1.0) and ("1" != "1.0") and not (5 != (3+2)))
print((1 == 1.0) and not ("1" == "1.0") or (5 != (3+2)))
print((1 == 1.0) or ("1" != "1.0") and (5 == (3+2)))
print((1 == 1.0) and ("1" != "1.0") or (5 == (3+2)))
```
## List Exercises

1)
```
oddlist = [1, 3, 5, 7, 9]
```
Yes, it did become a variable.

2)
```
print(oddlist)
```

3)
```
print(len(oddlist))
```
The output says 5.

4)
```
print(type(oddlist))
```
It does say it is a list type.

5) and 6)
```
intlist = list(range(1, 100))
print(intlist)
```
## Dictionary Exercises
1)
```
about_me = {'name':'Anna', 
            'age':23.0, 
            'studyYear': 17, 
            'faves': ["chocolate almonds", "spaghetti", "coffee"],
            }
pp.pprint(about_me)
```

2)
```
print(type(about_me))
```
It does say it is a dictionary type.

3)
```
print(len(about_me))
```
It says that the length is 4. Python determines the length of the dictionary by using how each information is separated by the comma. There is only 1 list with 3 strings of information inside, therefore, it is counted as a 1 item in the length rather than as 3 different separate items.

## Array Exercises
1)
```
mixnums = np.array([1, 2, 3, 4.0, 5.0, 6.0])
print(mixnums)
```
This ends up making all the values in the array into floats, despite there being both integers and floats.

2)
```
mixtypes = np.array([1, 2, 3.0, 4.0, '5', '6'])
print(mixtypes)
```
This ends up making all the values into strings, despite there being integers, floats, and strings in the array.

3)
```
oddarray = np.arange(0, 100, 3)
print(oddarray)
```
4)
```
logarray = np.logspace(1, 5, 16)
print(logarray)
```
