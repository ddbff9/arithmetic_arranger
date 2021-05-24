# Example of how problem is sent from Main.py
    # print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(problems, answer = False):
    
    i = 0
    #Create lists to store the values for the pieces of the problems
    top = []    
    bot = []
    op = []
    ans= []

    #Create lists to store the widths of the columns
    col_width= []

    #Problems need 4 blank spaces between them
    col_spacing = "    "

    #Creates lists to store spacing info
    top_spacing = []
    bot_spacing = []
    dash_spacing = []
    ans_spacing = []
    
    
    for problem in problems:    
        
        problem_pieces = problem.split()

        top.append(problem_pieces[0].strip())
        bot.append(problem_pieces[2].strip())
        op.append(problem_pieces[1].strip())

        if op[i] == "+":
            try:
                ans.append(str(int(top[i]) + int(bot[i])))
            except:
                return "Error: Numbers must only contain digits."
        else:
            try:
                ans.append(str(int(top[i]) - int(bot[i])))
            except:
                return "Error: Numbers must only contain digits."

        col_width.append(max(len(top[i]),len(bot[i])) + 2)
        
        i +=1
 
    #Check for errors:
    error_count = 0
    if len(problems) > 5:
        error_count +=1
        return 'Error: Too many problems.'

    
    if "*" in op or "/" in op:
        error_count +=1
        return "Error: Operator must be '+' or '-'."

    for x in top:
        if len(x) > 4:
            error_count +=1
            return "Error: Numbers cannot be more than four digits."
        try:
            str(x)
        except:
            return "Error: Numbers must only contain digits."


    for x in bot:
        if len(x) > 4:
            error_count +=1
            return "Error: Numbers cannot be more than four digits."
        try:
            str(x)
        except:
            return "Error: Numbers must only contain digits."

    #Only create spacing lists and print results if there are no errors
    if error_count < 1:
        for x in range(len(top)):
            top_spacing.append(" " * (int(col_width[x])-int(len(top[x]))) + top[x] + col_spacing)
        
        for x in range(len(bot)):
            bot_spacing.append(op[x] + " " * (int(col_width[x])-int(len(bot[x]))-1) + bot[x] + col_spacing)
        
        for x in range(len(bot)):
            dash_spacing.append("-"*col_width[x] + col_spacing)
        
        for x in range(len(ans)):
            ans_spacing.append(" " * (int(col_width[x])-int(len(ans[x]))) + ans[x] + col_spacing)
    
    if answer == False:
        arranged_problems = "".join(top_spacing).rstrip() + "\n" + "".join(bot_spacing).rstrip() + "\n" + "".join(dash_spacing).rstrip()
    else:
        arranged_problems = "".join(top_spacing).rstrip() + "\n" + "".join(bot_spacing).rstrip() + "\n" + "".join(dash_spacing).rstrip() + "\n" + "".join(ans_spacing).rstrip()

    return arranged_problems

# #Test Arrangment:
# print("\nTest Arrangment:\n"+ "*"*20 + "\n")
# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))

# #Test Too Many Problems:
# print("\nToo Many Problems:\n"+ "*"*20 + "\n")
# print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))

# #Test Incorrect Operator:
# print("\nIncorrect Operator:\n"+ "*"*20 + "\n")
# print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))

# #Test Too Many Digits:
# print("\nToo Many Digits:\n"+ "*"*20 + "\n")
# print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))

# #Test Only Digits:
# print("\nTest Only Digits:\n"+ "*"*20 + "\n")
# print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))

# #Test Solutions:
# print("\nTest Solution:\n"+ "*"*20 + "\n")
# print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))
