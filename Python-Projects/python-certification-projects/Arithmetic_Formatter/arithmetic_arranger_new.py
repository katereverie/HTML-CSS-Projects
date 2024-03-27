def arithmetic_arranger_new(problems, show_answer = None):

  if len(problems) > 5:
    return "Error: Too many problems."
  
  count_problems = len(problems) # number of problems 
  
  operand1 = [] #string
  operand2 = [] #string
  operator= [] #string
  dash_count= [] # integer, number of dashes for each problem
  operand1_count = 0
  operand2_count = 0
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

  operand1_count = len(operand1)
  operand2_count = len(operand2)

  if show_answer != True:
    l = 4 # how man lines to be shown
    c = 0
    while l < 5 and operand1_count != 0:
      arranged_problems = operand1[c].rjust(dash_count) + ' '*4
      
      
    

  return arranged_problems