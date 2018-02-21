#!/usr/bin/env python
'''
    Rutgers Data Science Homework Week 3, Assignment #4

    Assumptions:
    1) Senseces are broken up by period.
    2) Paragraphs are broken up by new line
    3) - are not divider

    To run this script:

        pyparagraph.py [--summary_file=SUMMARY_FILE] input_file_1 input_file_2 ...

    <Chan Feng> 2018-02

'''

import os
import re
from argparse import ArgumentParser

_RE_SENTENCE = re.compile('(?<=[.!?]) +')
_RE_WORD = re.compile('[, ]+') # Count world with - as single word as both Word and Google doc both do that.

_SUMMARY_FILE = 'pyparagraph_summary.txt'
_SUMMARY_FORMAT = '''
Paragraph Analysis
-----------------
Approximate Word Count: {word_count}
Approximate Sentence Count: {sentence_count}
Average Letter Count: {average_letter_count:.2f}
Average Sentence Length: {average_sentence_length:.2f}'''
_DATA_DIR = 'raw_data'

def main():
    '''
    return: 0 for success
    '''
    arg_parser = ArgumentParser()
    arg_parser.add_argument('input_files', type=str, nargs='+',
                            help='One or more input files')
    arg_parser.add_argument('--summary_file', type=str,
                            help='Default output file name is ' + _SUMMARY_FILE )
    args = arg_parser.parse_args()

    paragraphs = []
    for input_file in [os.path.join(_DATA_DIR, f) for f in args.input_files]:
        with open(input_file, 'r') as f:
            for paragraph in f:
                paragraphs.append(paragraph)

    summarize(paragraphs, args.summary_file or _SUMMARY_FILE)
    return 0

def summarize(paragraphs, summary_file):
    '''
    Summarize
    :param data: collected data
    :return: 0 for success
    '''

    word_count = 0
    sentence_count = 0
    letter_count = 0

    for p in paragraphs:
        for sentence in _RE_SENTENCE.split(p):
            sentence_count += 1
            for word in _RE_WORD.split(sentence):
                word_count += 1
                letter_count += len(word)

    summary = _SUMMARY_FORMAT.format(
        word_count=word_count,
        sentence_count=sentence_count,
        average_letter_count=letter_count/word_count,
        average_sentence_length=word_count/sentence_count
    )

    print(summary)
    if summary_file:
        with open(summary_file, 'w') as outfile:
            outfile.write(summary)

    return 0

if __name__ == '__main__':
    main()