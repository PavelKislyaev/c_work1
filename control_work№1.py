gradess=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
print(gradess)
print(type(gradess))
students={'Johny','Bilbo','Steve','Khendrik','Aaron'}
print(students)
print(type(students))
aaron_gradess=[5,3,3,5,4]
print('Aaron:',aaron_gradess)
average_rating_aaron=sum(aaron_gradess)/len(aaron_gradess)
print('Aaron средний балл:',average_rating_aaron)
bilbo_gradess=[2,2,2,3]
print('Bilbo:',bilbo_gradess)
average_rating_bilbo=sum(bilbo_gradess)/len(bilbo_gradess)
print('Bilbo средний балл:',average_rating_bilbo)
khendrik_gradess=[4,5,5,2]
print('Khendrik:',khendrik_gradess)
average_rating_khendrik=sum(khendrik_gradess)/len(khendrik_gradess)
print('Khendrik средний балл:',average_rating_khendrik)
steve_gradess=[4,4,3]
print('Steve:',steve_gradess)
average_rating_steve=sum(steve_gradess)/len(steve_gradess)
print('Steve средний балл:',average_rating_steve)
johnny_gradess=[5,5,5,4,5]
print('Johnny:',johnny_gradess)
average_rating_johnny=sum(johnny_gradess)/len(johnny_gradess)
print('Johnny средний балл:',average_rating_johnny)
average_student_grade={'Aaron':average_rating_aaron,'Bilbo':average_rating_bilbo,'Khendrik':average_rating_khendrik,'Steve':average_rating_steve,'Johnny':average_rating_johnny}
print(average_student_grade)
print(type(average_student_grade))