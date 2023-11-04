"""Common functions/classes used in programs of the project"""

from random import choice, randint, uniform


CORRECT_WORDS = ['Correct', 'Right', 'Good', 'Great', 'Excellent', 'Terrific',
                 'Awesome', 'Amazing', 'Fabulous', 'Fantastic', 'Wonderful',
                 'Incredible', 'Outstanding', 'Impressive', 'Marvelous',
                 'Perfect', 'Super', 'Superb', 'Splendid', 'Exactly', 'Bravo',
                 'Bingo', 'Hooray', 'Well done', 'Five-star', 'High-five']


def question_generator(*question_types, count=2, perfect_score=100):
    """Generate questions of different questoin types and calculate score.
    
    question_types: tuple of functions. Each function generates a certain type of question
                    and returns True/False depending on if the answer is correct. 
    count: number of questions to generate.
    perfect_score: score for answering all questions correctly.
    """
    score_per_question = perfect_score / count
    score = 0
    for i in range(count):
        print(f'Question {i + 1}/{count}:  ', end='')
        question_type = choice(question_types)
        if question_type():
            print(f'{choice(CORRECT_WORDS)}!\n')
            score += score_per_question
    print(f'Your score is {round(score)}/{perfect_score}.\n')


def answer_check(correct_answer, prompt='? ', check_mode='equal',
                 displayed_answer=None, is_unique=True):
    """Input an answer and check if it is correct.
    Return True if the answer is correct, otherwise, show the correct answer and return False.

    correct_answer: used to check if the answer is correct.
    prompt: input prompt string.
    check_mode:
        'equal': the answer must be equal to correct_answer in value.
        'same' : the answer must be exactly the same as correct_answer.
        'fraction': the answer may be a fraction or decimal and must be equal to
                    correct_answer in value.
        'fraction_only': the answer must be a fraction and equal to correct_answer in value.
    displayed_answer: the correct answer for displaying. if not given, correct_answer will
                      be displayed.
    is_unique: whether the answer is unique or not.
    """
    answer = input(prompt)
    if check_mode == 'equal':
        try:
            if float(answer) == correct_answer:
                return True
        except ValueError:
            pass
    elif check_mode == 'same':
        if answer.strip() == correct_answer:
            return True
    else:
        value = eval_fraction(answer)
        if value is not None and value == correct_answer:
            return True
        if value is None and check_mode == 'fraction':
            try:
                if float(answer) == correct_answer:
                    return True
            except ValueError:
                pass

    if is_unique:
        print(f'Incorrect. The answer is {displayed_answer or correct_answer}.\n')
    else:
        print(f'Incorrect. One possible answer is {displayed_answer or correct_answer}.\n')
    return False


def input_natural_number(prompt='', minimum=0, maximum=None, digit_count=None):
    """Input a valid natural number and return it as a string.
    
    prompt: input prompt string.
    minimum/maximum: the natural number should be in the range of [minimum, maximum].
                     Default starts from 0.
    digit_count: number of digits required for the natural number.
    """
    while True:
        num = input(prompt)
        # Ensure the input is a valid natural number after removing any commas and whitespaces.
        num = ''.join(num.replace(',', '').split())
        if num.isdecimal():
            # Remove leading zeros if any exist.
            num = str(int(num))
            # Check if digit_count is satisfied.
            if not digit_count or digit_count == len(num):
                # Check if it is within range.
                if maximum is None:
                    if int(num) >= minimum:
                        return num
                    print(f'The number must be larger than {minimum - 1}.')
                else:
                    if minimum <= int(num) <= maximum:
                        return num
                    print(f'The number must be in the range from {minimum} to {maximum}.')
            else:
                print(f'The number should have {digit_count} '
                      + ('digit.' if digit_count == 1 else 'digits.'))
        else:
            print("You didn't enter a valid natural number, please try again.")


def input_decimal(prompt='', minimum=0, maximum=None, minimum_inclusive=True, fraction=False):
    """Input a decimal between minimum and maximum and return it as a string.
    
    prompt: input prompt string.
    minimum/maximum: the decimal should be in the range of [minimum, maximum].
    minimum_inclusive: whether minimum is included in the range.
    fraction: whether users can input a fraction.
    """
    while True:
        decimal = input(prompt)
        try:
            decimal = float(decimal)
            if (decimal == minimum and minimum_inclusive
                or decimal > minimum and (maximum is None or decimal <= maximum)):
                return str(decimal)
        except ValueError:
            if fraction:
                value = eval_fraction(decimal)
                if value is not None:
                    if (value == minimum and minimum_inclusive
                        or value > minimum and (maximum is None or value <= maximum)):
                        return str(value)
        if fraction:
            print("You didn't enter a valid decimal or fraction. Please try again.")
        else:
            print("You didn't enter a valid decimal. Please try again.")


def input_fraction(prompt=''):
    """Input a fraction and return its numerator and denominator.
    
    prompt: input prompt string.
    """
    while True:
        fraction = input(prompt)
        # Remove all whitespaces in fraction.
        fraction = ''.join(fraction.split())
        # Check if fraction is a integer.
        if fraction.isdecimal():
            return int(fraction), 1
        # Split fraction into a tuple containing three elements to check if fraction is valid.
        string_tuple = fraction.partition('/')
        if (string_tuple[1] == '/' and string_tuple[0].isdecimal()
            and string_tuple[2].isdecimal() and int(string_tuple[2]) != 0):
            return int(string_tuple[0]), int(string_tuple[2])
        print("You didn't enter a valid fraction. Please try again.")


def eval_fraction(string):
    """If string is a fraction, return its float type value, otherwise return None."""
    # Remove all whitespaces in string.
    string = ''.join(string.split())
    # Split string into a tuple containing three elements.
    string_tuple = string.partition('/')
    if (string_tuple[1] == '/' and string_tuple[0].isdecimal()
        and string_tuple[2].isdecimal() and int(string_tuple[2]) != 0):
        return int(string_tuple[0]) / int(string_tuple[2])
    return None


def decimal_generator(minimum=0, maximum=1, decimal_place_count=1, decimal_place_count_dist=None):
    """Generate a decimal between minimum and maximum and return the decimal and its number of
    decimal places.

    minimun/maximum: the decimal generated is in the range of [minimum, maximum].
    decimal_place_count: number of decimal places, 0 for integer.
    decimal_place_count_dist:
        a list representing the probability distribution of different numbers of
        decimal places. Eg, [1, 1, 1, 2, 2] means the number of decimal places is
        60% likely to be 1 and 40% likely to be 2.
    """
    if decimal_place_count_dist:
        decimal_place_count = choice(decimal_place_count_dist)
    # Generate an integer if decimal_place_count is 0.
    if decimal_place_count == 0:
        return randint(minimum, maximum), 0
    # Generate a decimal with decimal_place_count decimal places.
    decimal_str = ''
    while (len(decimal_str) - 1 - decimal_str.find('.') != decimal_place_count
           or decimal_str[-2:] == '.0'):
        # round() will return a decimal with all trailing zeros removed except for the zero in
        # the tenth place. while loop is used to ensure decimal has required decimal places.
        decimal = round(uniform(minimum, maximum), decimal_place_count)
        decimal_str = str(decimal)

    return decimal, decimal_place_count


def remove_trailing_zeros(decimal):
    """Remove trailing zeros of a decimal without changing its value.
    
    decimal: a string type decimal.
    """
    decimal = decimal.rstrip('0')
    if decimal[-1] == '.':
        decimal = decimal[:-1]
    return decimal
