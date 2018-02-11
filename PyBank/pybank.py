#!/usr/bin/env python
'''
    Rutgers Data Science Homework Week 3, Assignment #1

    To run this script:

        pybankl.pl [--summary_file=SUMMARY_FILE] input_file_1 input_file_2 ...

    <Chan FEng> 2018--02=11

'''
import csv
from argparse import ArgumentParser

_SUMMARY_FILE = 'pybank_summary.txt'
_SUMMARY_FORMAT = '''
Financial Analysis'
--------------------------------
Total Month: {total_month}
Total Revenue: ${total_revenue:,}
Average Revenue Change: ${avg_revenue_change:,}
Greatest Increase in Revenue: {greatest_increase_month} (${greatest_increase:,})
Greatest Decrease in Revenue: {greatest_decrease_month} (${greatest_decrease:,})'''
_MONTH_LOOKUP = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

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
            month = normalize_month(row[0])
            revenue = row[1]
            data[month] = data.get(month, 0) + int(revenue)

def normalize_month(month):
    '''
    :param month:
    :return: month normalized to Jan-12

    Assume either Jan-12 or Jan-2012 format.
    Production system will need to a lot more sophisticated
    '''
    (mth, year) = month.split('-')
    if int(year) > 2000:
        return '{}-{:02d}'.format(mth, int(year) - 2000)
    return month

def summarize(data, summary_file=None):
    '''
    :param data: data objectu
    :param summary_file: optional summary file name
    :return: 0 for success
    '''
    total_revenue = 0
    change = 0
    total_change = 0
    total_change_cnt = 0
    prev_revenue = None
    increase_month = None
    increase_revenue = 0
    decrease_month = None
    decrease_revenue = 0

    for month in sorted(data, key=month_sort_key):
        revenue = data[month]
        total_revenue += revenue

        if prev_revenue:
            change = revenue - prev_revenue
            if change > increase_revenue:
                increase_month = month
                increase_revenue = change

            if change < decrease_revenue:
                decrease_month = month
                decrease_revenue = change

            total_change += change
            total_change_cnt += 1
        prev_revenue = revenue

    summary = _SUMMARY_FORMAT.format(
        total_month=len(data),
        total_revenue=total_revenue,
        avg_revenue_change=int(round(total_change/total_change_cnt)),
        greatest_increase_month=increase_month,
        greatest_increase=increase_revenue,
        greatest_decrease_month=decrease_month,
        greatest_decrease=decrease_revenue,
    )
    print(summary)

    if summary_file:
        with open(summary_file, 'w') as outfile:
            outfile.write(summary)

    return 0

def month_sort_key(month):
    '''
    Define how month are sorted

    :param month: 'Jan-12' format
    :return: 12-01
    '''
    (month, year) = month.split('-')
    return '{}-{:02d}'.format(year, _MONTH_LOOKUP[month])

if __name__ == '__main__':
    main()