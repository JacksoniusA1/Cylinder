import math
def get_float_value(prompt):
    run_again = True
    while (run_again):
        try:
            user_input = float(input(prompt))
            if(user_input <= 0):
                print("ERROR: Value must be greater than 0.\n")
                continue
        except:
            print("ERROR: Input must be a number.\n")
        else:
            run_again = False

    return user_input



rerun=True
while rerun:


    value_of_the_height=get_float_value ("what is the value of the height")
    value_of_the_radius=get_float_value ("what is the value of the radius ")

    #Calculation is equal to: r^2*pi*h
    total= math.pi*value_of_the_height*value_of_the_radius**2

    print(f"your cylinder area = {total:.2f}")

    do_again=input("would you like to perform another calculation (y/n)?")
    if do_again== "n":
        print("Good Bye") 
        rerun= False


