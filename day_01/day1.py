


def decode_line(line):
    '''
    Decodes by first extracting digits, creating string with first and last digit, and casting to int.
    '''
    import re
    numbers = re.findall('[0-9]',line)
    number_string = f"{numbers[0]}{numbers[-1]}"
    return int(number_string)
    
calibrations=[]
with open('calibration.txt') as f:
    calibrations = [decode_line(line) for line in f ]
    
print(sum(calibrations))
    

