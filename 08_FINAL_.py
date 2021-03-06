
# Functions go here

# Not blank functions

print("***** Welcome to my RECIPE COST CALCULATOR *****")

def not_blank_name(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        # if name is not blank, program continues

        if response.isalpha():
            print("That is a pretty name!")
            print("----------------------")
            return response
        else:
            print(error_message)


def not_blank_recipe(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        #  if name is not blank, program continues

        if response != "":
            print("Yum, that sounds delicious !")
            print("----------------------")
            return response

        else:
            print(error_message)


#  Serving size of recipe
def serving_recipe(question, low_num, high_num):
    error = "Please enter a whole number between 1 and 10 "

    valid = False
    while not valid:

        #  Ask user the number and check that it is inbetween 1 - 50
        try:
            response = int(input(question))
            print("----------------------")

            if low_num <= response <= high_num:
                return response
            else:
                print(error)

        # If a number in not entered then an error message will print
        except ValueError:
            print(error)


#  Ask the user for the ingredients name in a loop and store in a list

def ingredient_names(question, error_msg, recipe_name, serving_size):
    recipe_complete = False
    price_ing_section = False
    list_ing = []
    list_quant = []
    list_price = []
    list_quanity_4price = []
    count = 0
    valid = False
    quanity_ing = False
    idx = 0
    quanity_idx = 0
    price_idx = 0
    displaying_value_list = []
    comp_recipe = False

    ################################################################################################
    ### Asking Number of ingredients in recipe and recipe name

    ##    while valid == False:
    ##        recipe_name = input("What is the name of the recipe?\n")
    ##
    ##        comparing_var_rep = recipe_name.replace(" ", "")
    ##        if comparing_var_rep.isalpha():
    ##            valid = True  # if user enters a number the next part will run, asking for the ingredients
    ##        else:
    ##            print("Sorry this can't be a number, please enter your recipe name\n\n")

    valid = False

    while valid == False:
        number_ing = input(question)
        print("----------------------")

        if number_ing.isnumeric():
            valid = True  # if user enters a number the next part will run, asking for the ingredients
        else:
            print("Invalid answer, please enter an integer")

    ################################################################################################
    ### Asking for ingredients

    while recipe_complete == False:
        ing_number = False
        adding_ing_number = False
        yes_or_no_entered = False

        while ing_number == False:
            ing = input("What is ingredient {}?:\n".format(count + 1))
            test_ing = ing.replace(" ", "")
            if test_ing.isalpha():
                list_ing.append(ing)
                count += 1
                ing_number = True

            else:
                print("This must be an ingredient name")

        print("Updated list {}\n\n".format(list_ing))  # prints the ingredients entered so far

        if int(number_ing) == int(count):
            while yes_or_no_entered == False:
                correct_ing = input("Is this all the ingredients for the recipe?: (yes or no)\n {} \n".format(list_ing))

                if correct_ing == "yes" or correct_ing == "yup":
                    print("Thanks for entering the ingredients\n")
                    recipe_complete = True
                    yes_or_no_entered = True

                if correct_ing == "no" or correct_ing == "nah":
                    while adding_ing_number == False:
                        add_no_ing = input("How many more ingredients are there?:\n")

                        if add_no_ing.isnumeric():
                            number_ing = int(number_ing) + int(add_no_ing)
                            yes_or_no_entered = True

                            # This lets the user enter how many more ingredients to add
                            adding_ing_number = True

                        else:
                            print("This must be a number of ingredients")
                        # if user forgets ingredients at the start they can add more

                if correct_ing == "no" or correct_ing == "nah" or correct_ing == "yes" or correct_ing == "yup":
                    print()
                else:
                    print("Must be a 'yes' or 'no'")

    ################################################################################################
    ### Asking for price of ingredients, and the quantity for that price

    while price_ing_section == False:
        displaying_price_list = []
        ing_price = False
        quanity_price = False

        while ing_price == False:
            price = input("What is ingredient {}'s price? (in $):".format(list_ing[price_idx]))  ####quanity_idx

            test_price = price.replace(".", "")

            if test_price.isnumeric() or test_price.isdecimal() and not test_price.isalpha():
                numberver_price = float(price)  # use "numberver_price" in any calculations
                list_price.append(numberver_price)
                price_idx += 1
                ing_price = True

            else:
                print("This must be a price for the ingredient")

        ##################################################################################
        ##### when using any price from the list, use it by making it = to a varible #####
        var_4_math = (list_price[0])
        maths_stuff = (var_4_math + 1)
        ##################################################################################

        displaying_price_list.append("$" + str(list_price[price_idx - 1]))
        displaying_price_list.append(list_ing[price_idx - 1])

        print("Updated list {}\n".format(displaying_price_list))  # prints the prices for ingredients entered so far

        if int(price_idx) == len(list_ing):
            while quanity_price == False:

                if int(quanity_idx) < len(list_ing):
                    quanity_ing_price = input(
                        "What quantity in grams does ${}".format(list_price[quanity_idx]) + " of {} get?:".format(
                            list_ing[quanity_idx]))

                    test_quanity_ing_price = quanity_ing_price.replace(".", "")

                    if test_quanity_ing_price.isnumeric():
                        list_quanity_4price.append(quanity_ing_price)

                        displaying_price_list = []
                        displaying_price_list.append("$" + str(list_price[quanity_idx - 1]))
                        displaying_price_list.append(list_ing[quanity_idx - 1])
                        displaying_price_list.append(quanity_ing_price + "g")
                        print("Updated list {}\n\n".format(displaying_price_list))

                        quanity_idx += 1
                    else:
                        print("This must be a number value\n")

                else:
                    print("Thanks for entering the quantity of price for ingredients\n")
                    quanity_price = True
                    price_ing_section = True

    ################################################################################################
    ### Asking for quantity of ingredients

    while quanity_ing == False:
        number_check = False

        while number_check == False:
            value = input("How many grams of {} is required? :".format(list_ing[idx]))

            test_value = value.replace(".", "")

            if test_value.isnumeric() or test_value.isdecimal() and not test_value.isalpha():
                list_quant.append(value)

                displaying_value_list.append(list_ing[idx])  # adding the ing name and value to a temporary list
                displaying_value_list.append(list_quant[idx] + "g")  # ^
                # displaying the ing with the value next to it
                print("Updated Value list: {}\n".format(displaying_value_list))

                if idx + 1 < len(list_ing):
                    idx += 1
                else:
                    print("Thank you for entering the values for the ingredients\n")
                    # this list "list_quant" is the list with the values
                    # This is where you can add the next function
                    number_check = True
                    quanity_ing = True

                    calcuations(list_ing, list_price, list_quanity_4price,
                                list_quant, recipe_name, serving_size)

            else:
                print("This must be a number value\n")
                number_check = True


#  Calculations

def calcuations(list_ing, list_price, list_quanity_4price, list_quant, recipe_name, serving_size):
    print("----------------------")
    print("Recipe name:", recipe_name)
    print("----------------------")
    print("Ingredients in recipe:", list_ing)
    print("----------------------")
    print("Ingredients prices that the user has bought: $", list_price)
    print("----------------------")
    print("Ingredients quantity that the user has bought: grams", list_quanity_4price)
    print("----------------------")
    print("Ingredients quantity needed for in: ", recipe_name, list_quant)
    print("----------------------")
    print("Serving size wanted:", serving_size)
    print("----------------------")
    print("\n ")

    calcuations_comp = False
    comp_recipe = False
    idx = 0
    total_cost = 0

    while calcuations_comp == False:
        if idx < len(list_ing):
            list_quant_var = list_quant[idx]
            list_quanity_4price_var = list_quanity_4price[idx]
            list_price_var = list_price[idx]

            exact_cost = ((float(list_quant_var) / float(list_quanity_4price_var)) * float(list_price_var))
            # print(exact_cost)
            total_cost += exact_cost

            print("The exact cost for {}".format(list_ing[idx]) + " is ${}\n".format(round(exact_cost, 2)))

            idx += 1

        else:
            calcuations_comp = True

    print("The exact total cost for {}".format(recipe_name) + " is ${}\n\n".format(round(total_cost, 2)))

    ss_total_cost = total_cost / serving_size
    print(
        "The cost for the {}".format(serving_size) + " servings of {}".format(recipe_name) + " is: ${} each\n\n".format(
            round(ss_total_cost, 2)))

    while comp_recipe == False:
        save_question = input("Would you like to save this recipe to use in the future? (yes or no)\n")

        if save_question == "yes" or save_question == "yup":
            print("Thanks for saving the recipe\n")
            print("Enjoy your day")
            comp_recipe = True
            total_cost = round(total_cost, 2)
            save_recipe(recipe_name, list_ing, list_price, list_quanity_4price, list_quant, total_cost)

        if save_question == "no" or save_question == "nah":
            print("Okay this reipce hasn't been saved")
            comp_recipe = True


def save_recipe(recipe_name, list_ing, list_price, list_quanity_4price, list_quant, total_cost):
    list_idx = 0
    lists = []

    lists.append("")
    lists.append(list_ing)
    lists.append(list_price)
    lists.append(list_quanity_4price)
    lists.append(list_quant)

    try:
        recipe_file = open("Saved_recipes.txt", 'r')

    except:
        recipe_file = open("Saved_recipes.txt", 'w')
        recipe_file.write("0")

    recipe_file = open("Saved_recipes.txt", 'w')

    total_cost = str(total_cost)
    recipe_file.write(recipe_name + "\n")
    recipe_file.write(total_cost + "\n")

    print("list_idx", list_idx)
    print("len(list_ing)", len(list_ing))

    print("lists", lists)
    while list_idx < len(list_ing):

        # opens txt file in write mode
        with open("Saved_recipes.txt", 'w') as txt:
            for item in lists:
                # write each item on a new line
                txt.write("%s\n" % item)
            print('Done')

        list_idx += 1


# ----- MAIN ROUTINE -----

#  Calculate cost per serving

# ----- FINISH MAIN ROUTINE -----
name = not_blank_name("What is your name?: ", "Sorry this is an invalid answer, "
                                              "please enter your name")

recipe = not_blank_recipe("What is your recipe called?", "This can't be blank sorry, please enter your recipe name")

ser_rec = serving_recipe("How many servings are in {}?:".format(recipe), 1, 10)

ingredient_names("How many ingredient are there in {}?:".format(recipe),
                 "Invalid answer , please enter valid answer", recipe, ser_rec)
