#!/usr/bin/env python

import requests
import re



FILENAME_INPUT_CODES = 'codes.csv'
FILENAME_OUTPUT = 'out.csv'
DIGITSTRING_TO_INT = {'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}


def crawl_code(code):
    r = requests.get('http://www.area-codes.org.uk/' + code + '.php')
    if r.status_code == 404:
        r = requests.get('http://www.area-codes.org.uk/' + code + '-area-code.php')
    print 'Crawling code: %s ,response status: %d ' % (code, r.status_code)
    if r.status_code == 404:
        return 'Not found: 404', 'Not found: 404'

    digits__in_number_area = 'Digits in ph not found: no matching string'
    name_of_the_area = 'Name not found: no matching string'
    for each in r.text.splitlines():
        match = re.search('Local telephone numbers \w+ ([\w\s\,\-\.\']+) are ([\w\s]+) digits long',each)
        if match:
            try:
                digits__in_number_area = DIGITSTRING_TO_INT[match.group(2)]
            except:
                # for cases like 'five or six digits long' take the lower one, five
                first_digit = match.group(2).split(' ')[0]
                digits__in_number_area = DIGITSTRING_TO_INT.get(first_digit,'Digits in ph not found or cant parse: ' + match.group(2))
            finally:
                name_of_the_area = match.group(1)
    return name_of_the_area, digits__in_number_area


with open(FILENAME_OUTPUT,'wb') as output_file:
    for line in open(FILENAME_INPUT_CODES,'rb'):
        name_of_the_area, digits__in_number_area = crawl_code(line.rstrip())
        output_file.write('%s,"%s",%s \n' %(line.rstrip(), name_of_the_area, digits__in_number_area))


