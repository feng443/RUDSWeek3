## Unit 3 | Assignment - Py Me Up, Charlie

*Note*: instead of using main.py, which is confusing, I used file name pattern of pybank.py, pyboss.py

## Option 1: PyBank

[PyBank/pybank.py](PyBank/pybank.py)

## Option 2: PyPoll

[PyPoll/pypoll.py](PyPoll/pypoll.py)

## Option 3: PyBoss

[PyBoss/pyboss.py](PyBoss/pyboss.py)


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
