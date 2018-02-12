#!/usr/bin/env python
'''
    Rutgers Data Science Homework Week 3, Assignment #2

    To run this script:

        pypoll.pl [--summary_file=SUMMARY_FILE] input_file_1 input_file_2 ...

    <Chan Feng> 2018-02

'''
import csv
from argparse import ArgumentParser

_SUMMARY_FILE = 'pypoll_summary.txt'
_SUMMARY_FORMAT = '''
Election Results
-------------------------
Total Votes: {total_votes:,}
-------------------------
{each_votes}
-------------------------
Winner: {winer}
-------------------------'''

def main():
    '''
    return: 0 for success
    '''
    arg_parser = ArgumentParser()
    arg_parser.add_argument('input_files', type=str, nargs='+',
                            help='One or more input files')
    arg_parser.add_argument('--summary_file', type=str,
                            help='Default summary file name is ' + _SUMMARY_FILE )
    args = arg_parser.parse_args()

    data = {}
    for input_file in args.input_files:
        gather_data(data, input_file)

    summarize(data, args.summary_file or _SUMMARY_FILE)

    return 0

def gather_data(data, input_file):
    '''
    :param data: data object
    :param input_file: Input file name
    :return: 0 for success
    '''
    with open(input_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None) # Skip header
        for row in reader:
            (voter_id, county, candidate) = row
            data[candidate] = data.get(candidate, 0) + 1

def summarize(data, summary_file=None):
    '''
    :param data: data objectu
    :param summary_file: optional summary file name
    :return: 0 for success
    '''
    total_votes = sum([data[d] for d in data])
    each_votes = '\n'.join(['{}: {:2.1f}% ({:,})'.format(d, 100 * data[d]/total_votes, data[d]) for d in sorted(data)])
    winner = sorted(data, key=lambda d: data[d], reverse=True)[0]

    summary = _SUMMARY_FORMAT.format(
        total_votes=total_votes,
        each_votes=each_votes,
        winer=winner
    )
    print(summary)

    if summary_file:
        with open(summary_file, 'w') as outfile:
            outfile.write(summary)

    return 0
if __name__ == '__main__':
    main()