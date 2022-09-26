# Assignment 3

### Variable operations exercises
1)
```
sub_code = "sub"
subnr_int = 2
subnr_str = "2"

print(sub_code + subnr_str)
print(sub_code + subnr_int)
```
Only sub_code and subnr_str can create the output 'sub2'. This is because they are both string values that can operations can work on. Meanwhile subnr_int, is an integer that operations cannot work on with string values.

2)
```
#sub2
print(sub_code + " " + subnr_str)

#sub 222
print(sub_code + " " + subnr_str*3)

#sub2sub2sub2
print((sub_code + subnr_str)*3)

#subsubsub222
print((sub_code*3)+(subnr_str*3))
```

### List operation exercises
1)
```
numlist = [1,2,3]
numlist * 2
```

2)
```
numarr = np.array([1,2,3])
numarr*2
```
In a list when we multiply it by 2, the values in the list are repeated twice, therefore doubling the length of the list (i.e., from 3 integers it becomes 6 integers). In the array when we multiply it by 2, the integers in the array are multipled by 2, therefore [1,2,3] become [2,4,6]. The length of the array stays the same, but the values of the integers change.

3)
```
strlist = ['do', 're', 'mi', 'fa']

#['dodo','rere','mimi','fafa'] 
print(strlist[0]*2, strlist[1]*2, strlist[2]*2, strlist[3]*2)

#['do','re','mi','fa','do','re','mi','fa'] 
print(strlist * 2)

#['do','do','re','re','mi','mi','fa','fa'] 
print(strlist[0], strlist[0], 
      strlist[1], strlist[1],
      strlist[2],strlist[2],
      strlist[3], strlist[3])

#[['do','do'],['re','re'],['mi','mi'],['fa','fa']]
print([strlist[0], strlist[0]], 
      [strlist[1], strlist[1]],
      [strlist[2],strlist[2]],
      [strlist[3], strlist[3]])
```

### Zipping exercises
```
faces = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png'] * 2
houses = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png'] * 2
postCue = ['cue1'] * 5 + ['cue2'] * 5

completeOrder = list(zip(faces, houses, postCue))
print(completeOrder)

np.random.shuffle(completeOrder)
print(completeOrder)
```


### Indexing exercises
1)
```
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
```

2)
```
print(colors[-2])
```

3)
```
print(colors[-2][-2] + " " + colors[-2][-1])
```

4)
```
colors.remove(colors[-1])
colors.extend(["indigo", "violet"])
print(colors)
```

### Slicing exercises
1)
```
list100 = list(range(0, 101))
```

2)
```
print(list100[:10])
```

3)
```
print(list100[99::-2])
```

4)
```
print(list100[:-5:-1])
```

5)
```
print(list100[39] == 39)
print(list100[43] == 43)
```
Yes, the 40-44th numbers are equal to the integers 39-43
