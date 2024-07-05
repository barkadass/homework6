my_dict = {'Ilay': 1984, 'Anna': 1984, 'Maria': 2017, 'Misha': 2021, 'Amalia': 2007 }
print(my_dict)
my_dict = {'Ilay': 1984, 'Anna': 1984, 'Maria': 2017, 'Misha': 2021, 'Amalia': 2007 }
print(my_dict['Ilay'])
my_dict = {'Ilay': 1984, 'Anna': 1984, 'Maria': 2017, 'Misha': 2021, 'Amalia': 2007 }
print(my_dict.get('Vasya'))
my_dict = {'Ilay': 1984, 'Anna': 1984, 'Maria': 2017, 'Misha': 2021, 'Amalia': 2007 }
my_dict.update({'Pasha': 1990,
                'Daniil': 1993})
my_dict.update({'Vera': 1980,
                'Olga': 1993})
print(my_dict)
del my_dict['Vera']
del my_dict['Olga']
print(my_dict)

my_dict = {'Ilay': 1984, 'Anna': 1984, 'Maria': 2017, 'Misha': 2021, 'Amalia': 2007 }
my_dict.update({'Pasha': 1990,
                'Daniil': 1993})
my_dict.update({'Vera': 1980,
                'Olga': 1993})
a = my_dict.pop('Vera')
b = my_dict.pop('Olga')
print(my_dict)
print(a)
print(b)
my_dict = {'Ilay': 1984, 'Anna': 1984, 'Maria': 2017, 'Misha': 2021, 'Amalia': 2007 }
my_dict.update({'Pasha': 1990,
                'Daniil': 1993})
my_dict.update({'Vera': 1980,
                'Olga': 1993})
print(my_dict)






my_set = {'Apple','Apple','Apple',1,1,1,2,2,3,4,5,5,5,3.14,(9,8,7,6,5)}
print(my_set)
my_set.update({'a','b','c','d'})
print(my_set)
my_set.discard(1)
print(my_set)

