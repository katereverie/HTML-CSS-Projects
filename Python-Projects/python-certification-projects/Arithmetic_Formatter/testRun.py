from arithmetic_arranger import arithmetic_arranger

# test1 = ['3801 - 2', '123 + 49']
# test2 = ['1 + 2', '1 - 9380']
# test3 = ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']
# test4 = ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
# test5 = ['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']
# test6 = ['3 / 855', '3801 - 2', '45 + 43', '123 + 49']
# test7 = ['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']
# test8 = ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
# test9 = ['3 + 855', '988 + 40'], True
# test10 = ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True




# print(arithmetic_arranger(test))
# print(type(test))
# for t in test:
#     t = t.split(' ')
#     print(t)
#     print(t[1])
#     if t[1] != '+' and '-':
#       print("Error: Operator must be '+' or '-'.")

# print(type('-')) 
# print(type(' '))
# print(type('\n'))

# for problem in test1:
#   problem = problem.split()
#   problem = list(problem)
#   print(problem)

print(arithmetic_arranger(['1444 + 1', '1 - 1', '1 - 1','1 - 1', '1 - 1'], True))

# test right align
# op1 = '32'
# op2 = '698'
# line1 = op1.rjust(5)
# print(line1)

    
# print('test1')
# print(arithmetic_arranger(test1))
# print('test2')
# print(arithmetic_arranger(test2))
# print('test3')
# print(arithmetic_arranger(test3))
# print('test4')
# print(arithmetic_arranger(test4))
# print('test5')
# print(arithmetic_arranger(test5))
# print('test6')
# print(arithmetic_arranger(test6))
# print('test7')
# print(arithmetic_arranger(test7))
# print('test8')
# print(arithmetic_arranger(test8))
# print(dir(test9[0]))
# print(type(test9))
# print('test9')
# print(arithmetic_arranger(test9)) # traceback - error in the arranger function: line 20 p = p.split() list object has no attribute split
# print('test10')
# print(arithmetic_arranger(test10))
