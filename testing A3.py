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


# Keep this main function
def main():
    # Asks for the price of gas
    gas_price = float(input('What is the price of gas?'))
    # Asks for the price of electricity
    electric_price = float(input('What is the price of electricity?'))
    # Set miles per gallon values to vehicle
    car_mpg = 25
    truck_mpg = 15
    electric_mpg = 4

    # Calculates the total cost
    for distance in range(50, 501, 50):
        total_cost_car = (calculate_gas_vehicle_trip_cost(distance, car_mpg, gas_price))
        total_cost_truck = (calculate_gas_vehicle_trip_cost(distance, truck_mpg, gas_price))
        total_cost_electric = (calculate_electric_vehicle_trip_cost(distance, electric_mpg, electric_price))
        # prints the total cost of the three vehicles
        print('For a trip of', distance, 'miles, the cost are truck: $'+str(round(total_cost_truck))+',', 'car: $'+str(round(total_cost_car))+',', 'electric: $'+str(round(total_cost_electric)))


# Keep these lines. It helps Python run the program correctly.
if __name__ == "__main__":
    main()
