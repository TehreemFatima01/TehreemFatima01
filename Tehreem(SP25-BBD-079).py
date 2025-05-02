#part a
person = {
    "name": "Tehreem",
    "age": 18,
    "city": "Lahore",
    "hobbies": ["reading", "painting", "sleeping", "Eating"]
}
print(person)

#part b
text = 'hello world hello everyone'
words = text.split()
word_count = {}
for words in words :
    if word in word_count :
        word_count[word] +=1
    else:
        word_count[word]=1
        print(word_count)

#part c
inventory={
    'mango':{'quantity':10,
             'price':5},
             'banana':{'quantity':12'
                       'price':3}
}
print(inventory)

#part d
orders = [
    {'category': 'electronics'},
    {'category': 'clothes'}, 
    {'category': 'books'},
    {'category': 'clothes'},
    {'category': 'electronics'},
    {'category': 'clothes'}
]

category_count = {}

for order in orders:
    category = order['category']
    if category in category_count:
        category_count[category] += 1
    else:
        category_count[category] = 1

print(category_count)

#Part e 
students ={
    'tehreem':[85,90,78]
    'fatima': [90,84,69]
}
for name , grades in students.items():
    avg=sum(grades)/len(grades)
    print(f"{name}'s average:{avg}")

#part f
inventory={}
inventory['laptop']=
{'quiantity':2, 'price':1000}
inventory['mouse']={'quantity':1 , 'price':400}
inventory['keyboard']={'quantity':6, 'price':600}
print(inventory)
orders['laptop']['quantity']=4
print(inventory)
total_value=0
for item in inventory:
    quantity=inventory[item]['price']
    price=inventory[item]
    ['price']
    total_value+=quantity*price
    print('total inventory value:',total_value)
    print('Low stock items:')
    for item in inventory:
        if inventory [item]
        ['quantity']<5:
        print(item,'->', inventory[item])

# Part g: Create a dictionary
students = {
    "saba": {"maths": 90, "computer": 85, "sst": 88},
    "zara": {"maths": 75, "computer": 80, "sst": 85}
}

# Calculate the average for each student
for name, grades in students.items():
    avg = sum(grades.values()) / len(grades)
    print(f"{name}'s average: {avg:.2f}")  # :.2f formats to 2 decimal places

# Find highest and lowest in maths
highest = -1  # Initialize with a value lower than possible marks
lowest = 101  # Initialize with a value higher than possible marks
highest_name = ""
lowest_name = ""

for name in students:
    mark = students[name]["maths"]
    if mark > highest:
        highest = mark
        highest_name = name
    if mark < lowest:
        lowest = mark
        lowest_name = name

print("\nHighest in maths:", highest_name, "(", highest, ")")
print("Lowest in maths:", lowest_name, "(", lowest, ")")



