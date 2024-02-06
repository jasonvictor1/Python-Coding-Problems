
# Prompt the user to enter their marks for five subjects
print("Enter your marks:")
marks = []  # Initialize an empty list to store the marks
for i in range(5):
    subject = int(input(f"Subject {i+1}: "))  # Get the mark for each subject
    marks.append(subject)  # Add the mark to the 'marks' list

# Calculate the average of the marks
avg = sum(marks) / len(marks)

# Determine the grade based on the average mark using conditional statements
if avg >= 90:
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 70:
    print("Grade: C")
elif avg >= 60:
    print("Grade: D")
else:
    print("Grade: F")
