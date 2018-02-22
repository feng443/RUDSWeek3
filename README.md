## Unit 3 | Assignment - Py Me Up, Charlie

*Note*: 
- Instead of using main.py, which is confusing, I used file name pattern of pybank.py, pyboss.py etc. 
- I also use argparse to handle input file and summary file so the scripts can handle arbitrary input file name/path.

TODO: 
- Add better alignment in summary
- Better handling of percentage format
- Put negative sign after $ sign?

## Option 1: PyBank

[PyBank/pybank.py](PyBank/pybank.py)

Output with both input files (Can also pass single input file)
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

Output with both input file.
```buildoutcfg
Election Results
-------------------------
Total Votes: 4,324,001
-------------------------
Cordin: 0.6% (24,090)
Correy: 16.3% (704,200)
Khan: 51.3% (2,218,231)
Li: 11.4% (492,940)
O'Tooley: 2.4% (105,630)
Seth: 0.9% (40,150)
Torres: 8.2% (353,320)
Vestal: 8.9% (385,440)
-------------------------
Winner: Khan
-------------------------
```

## Option 3: PyBoss

[PyBoss/pyboss.py](PyBoss/pyboss.py)

[PyBoss/employee_data_parsed.csv](PyBoss/employee_data_parsed.csv)

## Option 4: PyParagraph

[PyParagraph/pyparagraph.py](PyParagraph/pyparagraph.py)

I got 121 word count instead of 122 word count using the example text. I tried with Microsoft Word 2016 and it got 121 and Google Doc get 120. Looks like both Word and Goodle does treate world like 'bob-cat' as a single world, and Google is more aggresive.

Also the regexp in the homework specifications does not work. Looks like some one copy "<" in its smpersand HTML format.
```
re.split("(?&lt;=[.!?]) +", paragraph)
```

Should be

```buildoutcfg
re.split("(?<=[.!?]) +", paragraph)
```

Output with both input files.
```buildoutcfg
Paragraph Analysis
-----------------
Approximate Word Count: 426
Approximate Sentence Count: 25
Average Letter Count: 5.43
Average Sentence Length: 17.04
```
