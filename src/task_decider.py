# do make a class for tasks
# do not make a class for get_prefered_option

# wash dishes > cook dinner
# cook dinner > clean windows
# clean windows > wash dishes


# def get_preferred_option(task1,task2):
#     options = [task1,task2] 
#     if "Wash Dishes" and "Cook Dinner" in options:
#         return "Wash Dishes"
#     elif "Cook Dinner" and "Clean Windows" in options:
#         return "Cook Dinner"
#     elif "Clean Windows" and "Wash Dishes" in options:
#         return "Clean Windows"
#     else:
#         return "be serious fam"


def get_preferred_option(task1,task2):
    #key will always take preference over value
    preferences = {
        "Wash Dishes":["Cook Dinner"],
        "Cook Dinner":["Clean Windows", "Do Ironing"],
        "Clean Windows":["Wash Dishes", "Do Ironing"],
        "Do Ironing" : ["Wash Clothes, Wash Dishes"],
        "Wash Clothes": ["Cook Dinner", "Clean Windows"]
        }
    
    for key in preferences:
        if task1 == key and task2 in preferences[key]:
            return(key)
        if task2 == key and task1 in preferences[key]:
            return(key)
    return "you having a laugh"


get_preferred_option("Wash Dishes","Wash Dishes")