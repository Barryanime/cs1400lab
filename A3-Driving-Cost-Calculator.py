# CS1400 Assignment 3: Driving Cost Calculator by Barry Lin
# Add the functions for the assignment below here.
# Calculates the total cost of gas vehicle
def calculate_gas_vehicle_trip_cost(miles, mpg, gas_cost):
    gallons = miles / mpg
    cost_of_car = gallons * gas_cost
    return cost_of_car


# Calculates the total cost of electric vehicle
def calculate_electric_vehicle_trip_cost(miles, mpk, electric_cost):
    kwh = miles / mpk
    cost_of_electric = kwh * electric_cost
    return cost_of_electric


# Making a table for every 50 miles
def print_trip_cost_table(gas_price, electric_price, truck_mpg, car_mpg, electric_mpkwh):
    # Make a loop for the distance adding 50 miles each time
    for distance in range(50, 501, 50):
        # Calculates the total cost of the 3 vehicles
        total_cost_car = (calculate_gas_vehicle_trip_cost(distance, car_mpg, gas_price))
        total_cost_truck = (calculate_gas_vehicle_trip_cost(distance, truck_mpg, gas_price))
        total_cost_electric = (calculate_electric_vehicle_trip_cost(distance, electric_mpkwh, electric_price))
        # Prints the total cost of the three vehicles
        print('For a trip of', distance, 'miles, the cost are truck: $'+str(round(total_cost_truck))+',', 'car: $'+str(round(total_cost_car))+',', 'electric: $'+str(round(total_cost_electric)))


# Keep this main function
def main():
    # Asks for the price of gas
    gas_price = float(input('What is the price of gas per gallon?'))
    # Asks for the price of electricity
    electric_price = float(input('What is the price of electricity per kilowatt-hour?'))
    # Set miles per gallon or kilowatt-hour values to vehicle
    car_mpg = 25
    truck_mpg = 15
    electric_mpkwh = 4
    # Prints the table of the function
    print_trip_cost_table(gas_price, electric_price, truck_mpg, car_mpg, electric_mpkwh)


# Keep these lines. It helps Python run the program correctly.
if __name__ == "__main__":
    main()
