# -------- This code which in the top but WITHOUT using functions ----------

# The list of models which we have to print
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# The loop which prints every model to end list
# Each model switches in the list completed_models after print procedure
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Show all printed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
print("\n")
# -------- This code which in the top but WITH using functions ----------

def print_models_other_example(my_unprinted_designs, my_completed_models):
    """
    Supports printing of the models, while the list will not empty.
    Each model switches in the list completed_models after print procedure.
    """

    while my_unprinted_designs:
        my_current_design = my_unprinted_designs.pop()
        print(f"Printing model: {my_current_design}")
        my_completed_models.append(my_current_design)

def show_completed_models_other_example(my_completed_models):
    """ Show all info about all printed models """

    print("\nThe following models have been printed:")
    for my_completed_model in my_completed_models:
        print(my_completed_model)

my_unprinted_designs = ['iPhone Max', 'PC chair', 'Cat Marsik']
my_completed_models = []

print_models_other_example(my_unprinted_designs, my_completed_models)

# other variant for save the source list and work only with copy version pf the source list unprinted_designs
# print_models_other_example(my_unprinted_designs[:], my_completed_models)

show_completed_models_other_example(my_completed_models)
