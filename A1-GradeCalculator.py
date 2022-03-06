# asks for their first and last name
first_name = input('What is your first name?')
print(first_name)

# asks for scores in each category
pro_score = input()
midterms = input()
final_exam = input()
labs = input()
ebook = input()

# calculates the final score
final_grade = (50 * float(pro_score) + 18 * float(midterms) + 12 * float(final_exam) + 10 * float(labs) + 10 * float(ebook)) / 100
final_grade = str(final_grade)
print(first_name + ',', 'your final score for CS1400 is', final_grade + '.')
