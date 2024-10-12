names_of_students = {
    'Leo' : '60',
    'Oliver' : '65',
    'Ethan' : '57',
    'Edmond' : '80'
}
print ('Names: ', names_of_students.keys())
print ('grades: ', names_of_students.values())
for key, values in names_of_students.items():
    print (f'{key}: {values}')