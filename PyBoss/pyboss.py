#!/usr/bin/env python
'''
    Rutgers Data Science Homework Week 3, Assignment #3

    To run this script:

        pyboss.py [--summary_file=SUMMARY_FILE] input_file_1 input_file_2 ...

    <Chan Feng> 2018-02

'''
import csv
from argparse import ArgumentParser

_OUTPUT_FILE = 'employee_data_parsed.csv'
_STATE_CODE_LOOKUP = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

def main():
    '''
    return: 0 for success
    '''
    arg_parser = ArgumentParser()
    arg_parser.add_argument('input_files', type=str, nargs='+',
                            help='One or more input files')
    arg_parser.add_argument('--output_file', type=str,
                            help='Default output file name is ' + _OUTPUT_FILE )
    args = arg_parser.parse_args()

    # Open output file handler in beginning to avoid storing hugh amount of data
    output_file = args.output_file or _OUTPUT_FILE
    try:
        out_fh = open(output_file, 'w')
        out_fh.write(','.join(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']) + "\n")
    except FileNotFoundError as err:
        print('Could not open data file {} to write'.format(output_file))
        quit(-1)

    for input_file in args.input_files:
        with open(input_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)  # Skip header

            # Production sysstem should have more exception handling for things like
            # Empty rows, inccomplete SSN etc.
            for row in reader:
                (id, name, dob, ssn, state) = row
                (first, last) = name.split(' ')
                dob = parse_date(dob)
                ssn = '***-**' + ssn[-5:]
                state = _STATE_CODE_LOOKUP.get(state, 'N/A')
                out_fh.write(','.join([id, name, first, last, dob, ssn, state]) + '\n')

    out_fh.close()
    print('Done!')
    return 0

def parse_date(date):
    '''
    Parse date of brith
    :param date: '1985-12-04'
    :return: '12/04/1985'
    '''
    (year, month, day) = date.split('-')
    return '{}/{}/{}'.format(month, day, year)

if __name__ == '__main__':
    main()