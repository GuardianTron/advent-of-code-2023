word_to_digits = {
                "one":'1',
                "two":'2',
                "three":'3',
                "four":'4',
                "five":'5',
                "six":'6',
                "seven":'7',
                "eight":'8',
                "nine":'9'
        }

def get_digit(input):
    if input in word_to_digits.keys():
        return word_to_digits[input]
    else: 
        return input

def decode_digits(line):
    '''
    Extracts first and last digits - only numbers
    '''
    import re
    numbers = re.findall('[0-9]',line)
    number_string = f"{numbers[0]}{numbers[-1]}"
    return int(number_string)


def decode_line(line):
    '''
    Decodes by extracting digits including words.
    '''
    import re
    #get start digits
    start_digits = re.findall('one|two|three|four|five|six|seven|eight|nine|[0-9]',line)
    
    #get end digits (handle edge cases like twone,threeight, and nineight
    end_digits = re.findall('one(?!ight)|two(?!ne)|three(?!ight)|four|five(?!ight)|six|seven|eight(?!wo)|nine(?!ight)|[0-9]',line)
    #convert to list of all digits
    start_digit = get_digit(start_digits[0]) 
    end_digit = get_digit(end_digits[-1])
    #create appropriate string
    number_string = f"{start_digit}{end_digit}"
    print(f"{line[:-1]} - {number_string}")
    return int(number_string)
    
calibrations_digits=[]
calibrations_all=[]
with open('calibration.txt') as f:
    for line in f:
        # calibrations_digits.append(decode_digits(line))
        calibrations_all.append(decode_line(line))
   
print(sum(calibrations_all))

