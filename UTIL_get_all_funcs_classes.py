import inspect
import random


def get_all_classes(module):
    """
    Get all classes from a module.
    
    Args:
    module (module): The module from which to extract classes.
    
    Returns:
    list: A list of class objects.
    """
    classes = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            classes.append(obj)
    return classes

def get_all_methods(Class):
    # Create an instance of the class
    # Þetta þarf þá að vera sá klassinn sem vill sjá method-in úr. (Gera function sem skilar öllum klössum frá modula?)
    my_instance = Class()

    # Get a list of all attributes of the class
    all_attributes = dir(my_instance)

    # Filter out only the methods
    methods = [attr for attr in all_attributes if inspect.ismethod(getattr(my_instance, attr))]

    # Print the names of the methods
    for method in methods:
        print(method)

def get_all_functions(module):
    """Þetta skilar öllum functions frá gefna modulanum"""
    # Get a list of all attributes of the module
    all_attributes = dir(module)

    # Filter out only the functions
    functions = [attr for attr in all_attributes if inspect.isfunction(getattr(random, attr))]

    for function in functions:
        print(function)



