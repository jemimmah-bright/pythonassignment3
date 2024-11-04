#
#
student_name = ['sandra' , 'patricia' , 'phiona' , 'Anitah'] # strings

student_marks = [80 , 56 , 78 , 90] # integers

date = ['sandra' , 80 , 'kamwokya'] # mixed types 

#Access the whole
print(student_name, type(student_name))

#Access the list items
#INDEXES (positive indexing)
print(student_name[0]) #1st item
print(student_name[1]) #2nd item
print(student_name[2]) #3rd item
print(student_name[3]) #last item

#INDEXES (Negative indexing)
print(student_name[-4]) #1st item
print(student_name[-3]) #2nd item
print(student_name[-2]) #3rd item 
print(student_name[-1]) #last item


#ADDING new items to the lists 
#At the end

student_name.append('sandra')
print(student_name)

#Negative indexing
student_name.insert(2,'michelle')
print(student_name)

#Assignment
#print patricia to anitah
student_name.remove('sandra')
print(student_name)


#add masha at the fourth position
student_name.insert(3,'Masha')
print(student_name)

#update the name phiona to phiona Aladina 
name=["patricia","Faith","Anitah","phiona"]
index=name.index('phiona')
name[index] = "phiona Aladina"
print(name)

#display the length of the student list
student=["patricia","Faith","Anitah","phiona Aladina"]
lenght=[len(student) for student in student]
print(lenght)

#print all the students name having updated using a four loop
student_name= ["patricia","Faith","Anitah","phiona Aladina"]
for name in student_name:
    print(student_name)

#calculate the total marks for the student marks variable and the answer is 304
student_marks=[80,56,78,90]
total_marks = sum(student_marks)
print("Total marks:",total_marks)