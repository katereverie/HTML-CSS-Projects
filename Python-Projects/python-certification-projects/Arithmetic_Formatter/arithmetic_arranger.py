def arithmetic_arranger(problems, show_answer = None):

  if len(problems) > 5:
    return "Error: Too many problems."
  
  s = ' ' # string
  d = '-' # string
  operand1 = [] #string
  operand2 = [] #string
  operator= [] #string
  dash_count= [] # integer, number of dashes for each problem
  s1 = [] # integer, number of spaces for line 1 in each problem
  s2 = [] # integer, number of spaces for line 2 in each problem
  answer= [] # integer for line 4, answer for each arithmetic problem
  answer_count= [] # integer, how many characters does each answer have
  s4= [] # integer, number of spaces for line 4
  arranged_problems = str()
  

  for p in problems:
    p = p.split()
    p = list(p)
    if p[1] != '-' and p[1] != '+': # Debug: not 'or'.
      return "Error: Operator must be '+' or '-'."
    if not p[0].isdigit() or not p[2].isdigit(): 
      return "Error: Numbers must only contain digits."
    if len(p[0]) > 4 or len(p[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    operand1.append(p[0])
    operator.append(p[1])
    operand2.append(p[2])
    if p[1] == '+':
      answer.append(int(p[0]) + int(p[2]))
    if p[1] == '-':
      answer.append(int(p[0]) - int(p[2]))
    answer_count.append(len(str(answer[-1])))
    if len(p[0]) >= len(p[2]):
      dash_count.append(len(p[0]) + 2)
      s1.append(2)
      s2.append(len(p[0]) - len(p[2]) + 1)
    elif len(p[0]) < len(p[2]):
      dash_count.append(len(p[2]) + 2)
      s1.append(len(p[2]) - len(p[0]) + 2) # how many spaces for line 1
      s2.append(1) #  how many spaces for line 2 
    s4.append(dash_count[-1] - answer_count[-1]) # how many spaces for line 4

  if show_answer == True:
    if len(problems) == 1: arranged_problems = s*s1[0] + operand1[0] + '\n' + operator[0] + s*s2[0] + operand2[0] + '\n' + d * dash_count[0] + '\n' + s*s4[0] + str(answer[0])
    elif len(problems) == 2: arranged_problems = s*s1[0] + operand1[0] + s*4 + s*s1[1] + operand1[1] + '\n' + operator[0] + s*s2[0] + operand2[0] + s*4 + operator[1] + s*s2[1] + operand2[1]+ '\n' + d*dash_count[0] + s*4 + d*dash_count[1]+ '\n' + s*s4[0] + str(answer[0]) + s*4 + s*s4[1] + str(answer[1])
    elif len(problems) == 3: arranged_problems = s*s1[0] + operand1[0] + s*4 + s*s1[1] + operand1[1] + s*4 + s*s1[2] + operand1[2] + '\n' + operator[0] + s*s2[0] + operand2[0] + s* 4 + operator[1] + s*s2[1] + operand2[1] + s*4 + operator[2] + s*s2[2] + operand2[2]+ '\n' + d*dash_count[0] + s*4 + d*dash_count[1] + s*4 + d*dash_count[2] + '\n' + s*s4[0] + str(answer[0]) + s*4 + s*s4[1] + str(answer[1]) + s*4 + s*s4[2] + str(answer[2])
    elif len(problems) == 4: arranged_problems = s*s1[0] + operand1[0] + s*4 + s*s1[1] + operand1[1] + s*4 + s*s1[2] + operand1[2] + s*4 + s*s1[3] + operand1[3] + '\n' + operator[0] + s*s2[0] + operand2[0] + s*4 + operator[1] + s*s2[1] + operand2[1] + s*4 + operator[2] + s*s2[2] + operand2[2] + s*4 + operator[3] + s*s2[3] + operand2[3] + '\n' + d*dash_count[0] + s*4 + d*dash_count[1] + s*4 + d*dash_count[2] + s*4 + d*dash_count[3] + '\n' + s*s4[0] + str(answer[0]) + s*4 + s*s4[1] + str(answer[1]) + s*4 + s*s4[2] + str(answer[2]) + s*4 + s*s4[3] + str(answer[3])
    elif len(problems) == 5: arranged_problems = s*s1[0] + operand1[0] + s*4 + s*s1[1] + operand1[1] + s*4 + s*s1[2] + operand1[2] + s*4 + s*s1[3] + operand1[3] + s*4 + s*s1[4] + operand1[4] + '\n' + operator[0] + s*s2[0] + operand2[0] + s*4 + operator[1] + s*s2[1] + operand2[1] + s*4 + operator[2] + s*s2[2] + operand2[2] + s*4 + operator[3] + s*s2[3] + operand2[3] + s*4 + operator[4] + s*s2[4] + operand2[4] + '\n' + d*dash_count[0] + s*4 + d*dash_count[1] + s*4 + d*dash_count[2] + s*4 + d*dash_count[3] + s*4 + d*dash_count[4] + '\n' + s*s4[0] + str(answer[0]) + s*4 + s*s4[1] + str(answer[1]) + s*4 + s*s4[2] + str(answer[2]) + s*4 + s*s4[3] + str(answer[3]) + s*4 + s*s4[4] + str(answer[4])
  else :
    if len(problems) == 1: arranged_problems = s*s1[0] + operand1[0]+ '\n' + operator[0] + s*s2[0] + operand2[0]+ '\n' + d*dash_count[0]  
    elif len(problems) == 2: arranged_problems = s*s1[0] + operand1[0] + s*4 + s*s1[1] + operand1[1] + '\n' + operator[0] + s*s2[0] + operand2[0] + s*4 + operator[1] + s*s2[1] + operand2[1]+ '\n' + d*dash_count[0] + s*4 + d*dash_count[1]
    elif len(problems) == 3: arranged_problems = s*s1[0] + operand1[0] + s*4 + s*s1[1] + operand1[1] + s*4 + s*s1[2] + operand1[2] + '\n' + operator[0] + s*s2[0] + operand2[0] + s*4 + operator[1] + s*s2[1] + operand2[1] + s*4 + operator[2] + s*s2[2] + operand2[2]+ '\n' + d*dash_count[0] + s*4 + d*dash_count[1] + s*4 + d*dash_count[2]
    elif len(problems) == 4: arranged_problems = s*s1[0] + operand1[0] + s*4 + s*s1[1] + operand1[1] + s*4 + s*s1[2] + operand1[2] + s*4 + s*s1[3] + operand1[3] + '\n' + operator[0] + s*s2[0] + operand2[0] + s*4 + operator[1] + s*s2[1] + operand2[1] + s*4 + operator[2] + s*s2[2] + operand2[2] + s*4 + operator[3] + s*s2[3] + operand2[3] + '\n' + d*dash_count[0] + s*4 + d*dash_count[1] + s*4 + d*dash_count[2] + s*4 + d*dash_count[3]
    elif len(problems) == 5: arranged_problems = s*s1[0] + operand1[0] + s*4 + s*s1[1] + operand1[1] + s*4 + s*s1[2] + operand1[2] + s*4 + s*s1[3] + operand1[3] + s*4 + s*s1[4] + operand1[4] + '\n' + operator[0] + s*s2[0] + operand2[0] + s*4 + operator[1] + s*s2[1] + operand2[1] + s*4 + operator[2] + s*s2[2] + operand2[2] + s*4 + operator[3] + s*s2[3] + operand2[3] + s*4 + operator[4] + s*s2[4] + operand2[4] + '\n' + d*dash_count[0] + s*4 + d*dash_count[1] + s*4 + d*dash_count[2] + s*4 + d*dash_count[3] + s*4 + d*dash_count[4]

  return arranged_problems