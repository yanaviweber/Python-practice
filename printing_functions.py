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