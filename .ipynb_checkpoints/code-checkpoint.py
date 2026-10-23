# python data analysis report

# count students from region A -> expected a single output

count = 0
for line in open("student_record.txt"):
    each_field = line.strip().split(";")
    region_code = each_field[0]
    if region_code == "A":
        count += 1

print(f'Students from region A: {count}')


# Calculate the average Maths marks for region B (Assuming marks is at 6th position)

marks = []
for line in open("student_record.txt"):
    each_field = line.strip().split(";")
    region = each_field[0]
    
    region_math_marks = each_field[5]
    convert_marks = float(region_math_marks) # converting string into float
    
    if region == "B":
        marks.append(convert_marks)

avg_math_marks = sum(marks) / len(marks)
print(f'Average marks from region B is {avg_math_marks}') 


# Count students who scored above 50 in Maths

count = 0
for line in open("student_record.txt"):
    each_feild = line.strip().split(";")
    
    maths_marks = each_feild[5]
    converted_marks = float(maths_marks)

    if converted_marks > 50:
        count += 1

print(f'Count of students who scored > 50: {count}')
     
# find the highest math marks

# empty list to store highest marks
marks = [] 

for line in open("student_record.txt"):
    each_feild = line.strip().split(";")
    
    maths_marks = each_feild[5] 
    converted_marks = float(maths_marks)
    
    marks.append(converted_marks)

max_marks = max(marks) # aggregation function
print(f'Highest marks of student: {max_marks}')

# Calculate the pass percentage
# Assume a Maths mark of 35 or more is a pass. Calculate the percentage of students who passed.
# Formula: passed students ÷ total students × 100

marks = [] # empty list to store marks >= 35
total_students = 0

for line in open("student_record.txt"):
    each_feild = line.strip().split(";")
    total_students += 1
    
    
    maths_marks = each_feild[5]
    converted_marks = float(maths_marks)
    
    if converted_marks >= 35:
        marks.append(converted_marks)

passed_students = len(marks) # total number of student scored >= 35 in maths
percentage = passed_students / total_students * 100
print(f'Percentage if passed students: {percentage}')

# intermediate level
    
    

