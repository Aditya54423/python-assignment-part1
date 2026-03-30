##Part 1:- Python Basics and Control Flow 
##Theme:- Student Grade Tracker 
##----------------------------------------
## TASK 1 :- DATA PARSING AND PROFILE CLEANING
## --------------------------------------------
raw_students =[
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

## Now I will store cleaned version of raw students here :-
cleaned_students = []
print("\n" + "="*32)
print("     Task 1 : PROFILE CARDS")
print("=" * 32)      

for student in raw_students:
      #Step 1 :- we will clean the name :  strip space and then title case it
      # Here we will use .title() that handles the casing and stip() kills the padding.
      clean_name = student["name"].strip().title()
      
      #Step 2 :- Now we will convert roll number from string to integer
      roll_num = int(student ["roll"])
      
      # Step 3:- marks : split by ", " then cast each piece to int
      # Here I will e using list comprehension as it's cleaner than a loop
      marks_list = [int(m) for m in student["marks_str"].split(", ")]
      
      # Now building a cleaned record and save it
      cleaned = {
          "name": clean_name,
          "roll": roll_num,
          "marks": marks_list
      }
      cleaned_students.append(cleaned)
      
      
      #Now we will perform Name validation where every word must be purely alphabetic
      #We will use split() on the name to give us individual words like ["Ayesha", "Sharma" ]
      words = clean_name.split()
      name_ok = all(word.isalpha() for word in words)
      validity_check = "✓ Valid name" if name_ok else "✗ Invalid name"
      
      # Now Printing the profile card
      print("\n --------------------------------------")
      print(f"Student: {clean_name}  [{validity_check}]")
      print(f"Roll No : {roll_num}")
      print(f"Marks: {marks_list}")
      print("------------------------------------------")
 
# Now for prining roll no 103 student's name in ALL CAPS and lowercase
# Now we will search by roll number insted of the index because roll numbers are more reliable to idnetifier than position
for s in cleaned_students:
    if s ["roll"] == 103:
        print(f"\nRoll 103 name in ALL CAPS : {s['name'].upper()}")
        print(f"Roll 103 name in lowercase : {s['name'].lower()}")
        break
 
#-------------------------------------------------
#TASK 2:- MARKS ANALYSIS USING LOOPS AND CONDITIONALS 
#----------------------------------------------------------         
print("\n\n" + "=" * 32)  
print( "Task 2: MARKS ANALYSIS")
print("=" * 32) 

student_name = "Ayesha Sharma"
subjects = ["Math","Physics","CS","English","Chemistry"]
marks = [88,72,95,60,78]

# Now we will have Grading Logic
# I will try to check from highest to lowest and then grab the first match

def get_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >=70 :
        return "B"
    elif score >=60:
        return "C"
    else:
        return "F"

print(f"\nSubject wise breakdown for {student_name}:\n")  

# Now I will prefer using zip() to pair subjects and marks together
for subject,mark in zip(subjects,marks):
    grade = get_grade(mark)
    print(f"{subject:<12} -> {mark: >3}  Grade :{grade}")  

# Now for summary stats
total = sum(marks)
average = round(total/len(marks),2)  
 
 
#  To find highest/lowest I am pairing them and sorting them
pair = list(zip(subjects,marks))
pair_sorted =sorted(pair,key = lambda x:x[1])   

lowest_subject,lowest_mark = pair_sorted[0]
highest_subject,highest_mark = pair_sorted[-1]

print(f"\n Total Marks :{total}")
print(f" Average Marks : {average}")
print(f" Highest :  {highest_subject} ({highest_mark})")
print(f" Lowest  : {lowest_subject} ({lowest_mark})")

print(f"\n Add new subjects (type 'done' to stop)")
print(" (enter subject name first,then marks 0-100)\n")

new_subjects =[]
new_marks = []

while True:
    subject_input = input( "Subject name : ").strip()
    
    if subject_input.lower() == "done":
         break
    
    mark_input =input(f"  Marks for {subject_input} (0-100) :").strip()
    
    
    #Validating that marks should be number and within specified range
    #I am using a try/except so that non numeric input does not come
    
    try:
        mark_val = int(mark_input)
        if 0 <= mark_val <= 100:
            new_subjects.append(subject_input)
            new_marks.append(mark_val)
            print(f"✓ Added {subject_input}:{mark_val}\n")
        else:
            print(" !Marks must be between 0 and 100.Skipping.\n")
    except ValueError:
        print( "!That's not a valid number. Skipping.\n")    
        

#Summary after all this
all_marks = marks + new_marks
new_average = round(sum(all_marks)/ len(all_marks),2)
      
print(f"\n  New subjects added : {len(new_subjects)}")
print(f"  Updated average: {new_average}")     
       
#---------------------------------
#TASK 3 CLASS PERFORMANCE SUMMARY
#-------------------------------
print("\n\n" + "=" * 32)     
print( "  TASK 3 : CLASS PERFORMANCE SUMMARY")
print("=" * 32)

class_data = [
    ("Ayesha Sharma", [88,72,95,60,78]),
    ("Rohit Verma", [55,68,49,72,61]),
    ("Priya Nair", [91,85,88,94,79]),
    ("Karan Mehta", [40,55,38,62,50]),
    ("Sneha Pillai", [75,80,70,68,85])   
]

print(f"\n{'Name':<18}| {'Average':>7}|{'Status'}")
print("-"* 40)

all_averages = []
pass_count = 0
fail_count = 0
topper_name = ""
topper_avg = -1 # I will follow a approach where we will start low so the first real value always beats it

for name, mark_list in class_data:
        avg = round(sum(mark_list) / len(mark_list),2)
        status = "Pass" if avg >= 60 else "Fail"
        
        all_averages.append(avg)
        
        if status == "Pass":
            pass_count +=1
        else:
            fail_count +=1
            
        
        #Now tracking the topper if there's a tie ,first one wins which is fair enough
        if avg > topper_avg:
            topper_avg = avg
            topper_name = name        
        
        print(f"{name:<18} | {avg:>7.2f} | {status}")
        
     # Class level status
class_avg = round(sum(all_averages) / len(all_averages),2)
     
     
print(f"\n  Students passed : {pass_count}")
print(f"    Students failed : {fail_count}")
print(f"   Class topper :    {topper_name} ({topper_avg})") 
print(f"Class average : {class_avg}")

#-----------------------------------------------------
#TASK 4 :- STRING MANIPULATION UTILITY
#-----------------------------------------------------
print("\n\n" + "=" * 32)
print(" TASK 4 : STRING MANIPULATION")
print("=" * 32)

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

#Step 1 : We will strip whitespace;
clean_essay = essay.strip()
print(f"\n [Step 1 - Stripped]\n{clean_essay}")

#Step 2 : title case
print(f"\n [Step 2 - Title Case]\n{clean_essay.title()}")

#Step 3: count occurences of "python" as it's already in lowercse so no .lower() is needed
python_count = clean_essay.count("python")
print(f"\n[Step 3 - 'python' appears {python_count} time(s)]")

#Step 4 : replace "python with "Python"
replaced_essay = clean_essay.replace("python","Python 🐍")
print(f"\n[Step 4 - Replaced]\n{replaced_essay}")

#Step 5 : split into sentences on ". "
sentences = clean_essay.split(". ")
print(f"\n[Step 5 - Sentence List]\n{sentences}")

#Step 6 : numbered sentences,each ending with a period
print(f"\n[Step 6 - Numbered Sentences]")
for i,sentence in enumerate(sentences,start =1):
    #We will only add a period if the sentenc doesn't already end with one
    if not sentence.endswith("."):
        sentence = sentence + "."
    print(f" {i}.{sentence}")

print("\n" + "=" * 32) 
print(" ALL TASKS COMPLETED")
print("=" * 32 + "\n")       
