import pizza

# -------------- import the some concretic functions -------------
# from pizza import make_my_pizza

# -------------- using an alias as name of the importing function ----------------
# from pizza import make_pizza as mp
# mp(16,'blue_cheese')
# mp(12,'tomatoes', 'salami', 'parma')

# -------------- using an alias as name of the importing module ----------------
# import pizza as p
# p.make_my_pizza(16,'blue_cheese')
# p.make_my_pizza(12,'tomatoes', 'salami', 'parma')

# -------------- import all functions of the selected module  ----------------
# from pizza im[ort *
# make_my_pizza(16,'blue_cheese')
# make_my_pizza(12,'tomatoes', 'salami', 'parma')

pizza.make_my_pizza(16,'blue_cheese')
pizza.make_my_pizza(12,'tomatoes', 'salami', 'parma')


