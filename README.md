## Unit 3 | Assignment - Py Me Up, Charlie

*Note*: instead of using main.py, which is confusing, I used file name pattern of pybank.py, pyboss.py etc.

## Option 1: PyBank

[PyBank/pybank.py](PyBank/pybank.py)

```buildoutcfg
Financial Analysis
--------------------------------
Total Month: 86
Total Revenue: $55,945,323
Average Revenue Change: $4,444
Greatest Increase in Revenue: Sep-14 ($2,214,907)
Greatest Decrease in Revenue: Aug-14 ($-2,293,129)
```

## Option 2: PyPoll

[PyPoll/pypoll.py](PyPoll/pypoll.py)

```buildoutcfg
Financial Analysis
--------------------------------
Total Month: 86
Total Revenue: $55,945,323
Average Revenue Change: $4,444
Greatest Increase in Revenue: Sep-14 ($2,214,907)
Greatest Decrease in Revenue: Aug-14 ($-2,293,129)
```

## Option 3: PyBoss

[PyBoss/pyboss.py](PyBoss/pyboss.py)

[PyBoss/employee_data_parsed.csv](PyBoss/employee_data_parsed.csv)

## Option 4: PyParagraph

[PyParagraph/pyparagraph.py](PyParagraph/pyparagraph.py)

I got 121 word count instead of 122 word count using the example text. I tried with WOrd and it got 121 and Google Doc get 120. Looks like both Word and Goodle does treate world like 'bob-cat' as a single world, and Google is more aggresive.

Also the regexp in the homework specifications does not work. Looks like some one copy "<" in its smpersand HTML format.
```
re.split("(?&lt;=[.!?]) +", paragraph)
```

Should be

```buildoutcfg
re.split("(?<=[.!?]) +", paragraph)
```

```buildoutcfg
Paragraph Analysis
-----------------
Approximate Word Count: 426
Approximate Sentence Count: 25
Average Letter Count: 5.43
Average Sentence Length: 17.04
```
