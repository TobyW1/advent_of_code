import numpy as np


# Part 1: How many reports are safe?
# Read the file into a list
with open('../data/input_day2.txt', 'r') as file:
    reports = file.readlines()

reports = [np.array(report.strip('\n').split()) for report in reports]
reports = [[int(number_string) for number_string in report] for report in reports]


def is_report_safe(report):
    '''
    We will run this function on each report.
    It will return True if the report is safe, else False.
    '''

    diffs = np.diff(report)

    # Check monotone increasing/decreasing:
    if not (np.all(diffs > 0) or np.all(diffs < 0)):
        return False
    
    if not np.all(np.abs(diffs)  <= 3):
        return False
    
    return True


print(sum([is_report_safe(report) for report in reports]))

# Part 2: Can we make reports safe by removing 1 entry?

def is_report_nearly_safe(report):
    '''
    We'll iterate through all new permutations
    of a report, and perform is_report_safe() on them.
    If it's safe for any, we return True.
    '''

    for index in range(len(report)):
        if is_report_safe(report[:index] + report[index+1:]):
            return True
        
    return False

print(sum([is_report_nearly_safe(report) for report in reports]))



