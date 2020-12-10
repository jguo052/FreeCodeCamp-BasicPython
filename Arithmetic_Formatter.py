"""
Takes in arrays with less than five entries of the form ["integer +/- integer", ... ]
and formats each array entry side by side as a right alligned problem.

    integer      integer
+   integer    - integer    ...
___________    _________
     answer       answer
     
"""

def arithmetic_arranger(problems,*show_answers):
    sep_prob = list()
    for problem in problems:
        sep_prob.append(problem.split())

    test_results = test_valid_input(sep_prob)
    if test_results != 'Valid':
        return test_results

    first_line = ''
    second_line = ''
    underlines = ''
    answers = ''
    
    for i in range(len(sep_prob)):
        #get answer
        if sep_prob[i][1] == '+':
            answer = str(int(sep_prob[i][0]) + int(sep_prob[i][2]))
        if sep_prob[i][1] == '-':
            answer = str(int(sep_prob[i][0]) - int(sep_prob[i][2]))

        #include white space
        total_space = max(len(sep_prob[i][0]),len(sep_prob[i][2])) + 2
        sep_prob[i][0] = sep_prob[i][0].rjust(total_space)
        sep_prob[i][2] = sep_prob[i][2].rjust(total_space - 1)
        answer = answer.rjust(total_space)

        #concatenate problem lines
        if i != (len(sep_prob)-1):
            first_line = first_line + sep_prob[i][0] + '    '
            second_line = second_line + sep_prob[i][1] + sep_prob[i][2] + '    '
            answers = answers + answer + '    '
            underlines = underlines + '-'*total_space + '    '
        else:
            first_line = first_line + sep_prob[i][0]
            second_line = second_line + sep_prob[i][1] + sep_prob[i][2]
            answers = answers + answer
            underlines = underlines + '-'*total_space
        

    arranged_problems = first_line + '\n' + second_line + '\n' + underlines
    if show_answers:
        arranged_problems = arranged_problems + '\n' + answers

    return arranged_problems


### TESTS ###
def test_valid_input(problems):

    if not check_length(problems):
        return 'Error: Numbers cannot be more than four digits.'

    if len(problems) > 5:
        return 'Error: Too many problems.'

    if not check_operator(problems):
        return "Error: Operator must be '+' or '-'."

    if not check_integer(problems):
        return 'Error: Numbers must only contain digits.'

    return 'Valid'
    


def check_length(problems):
  for problem in problems:
    if len(problem[0]) > 4 or len(problem[2]) > 4:
      return False
  return True

def check_operator(problems):
  for problem in problems:
    if problem[1] != '+' and problem[1] != '-':
      return False
  return True

def check_integer(problems):
    for problem in problems:
        try:
            x = int(problem[0])
            y = int(problem[2])
        except:
            return False
    return True


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 - 401", "2 + 8"],True))
