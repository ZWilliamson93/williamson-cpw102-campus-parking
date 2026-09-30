# Named constant
#using 2.0 as it's value, automatically makes it a float
COST_PER_HOUR = 2.0

# Processing of program
def calculate_parking_cost(parked_hours):
    estimated_cost = parked_hours * COST_PER_HOUR
    return estimated_cost


# define the main logic of my program
def main():

    # create a variable in which I will store user-entered parked hours
    # a varibele is a named space in memory
    parked_hours = float(input ("How many hours will you be/ have been parked?")) 
    
    # Call Function
    cost = calculate_parking_cost(parked_hours)

    # Output
    print(cost) 
    
    # call my main function and execute the logic of program
main()
