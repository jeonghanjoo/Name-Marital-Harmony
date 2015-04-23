# Name-Marital-Harmony
Korean young people sometimes calculate 'Marital Harmony' with their name, based on the count of the strokes.
It is written on python3, and there is no interface(or wrapper) without target list variable.


## How - To - Use

* Open the file, and rewrite the 'people' variable.
``` python
people = ['김철수', '김미영', '오유진', '김진수', '박현진', '박지성', '김연아']
```


* Run
-- following code is for printing result.
``` python
for i in range(len(people)):
    for j in range(len(people)):
        s1 = people[i]
        s2 = people[j]
        print(str(goongHap(s1,s2)),end='\t')
    print()
```



* Result

The results are provided by n*n matrix. 
result[i][j] is the score how people[i] likes people[j]. 



* Why for this code.

'Channel A', Korean 2nd class news channel, report Name-Marital-Harmony between the bribe-accused Korean prime minister and the ceo who accused. 




  
