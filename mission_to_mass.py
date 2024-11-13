distance_in_km = float(input('Enter the distance from Earth to Mars in kilometers: '))
speed_in_km_per_hour = float(input('Enter the speed of the spaceship in kilometers per hour: '))
fuel_in_litres = float(input('Enter the total fuel available in liters: '))
x_coordinate = float(input('Enter the x-coordinate of the landing site: '))
y_coordinate = float(input('Enter the y-coordinate of the landing site: '))




print('\n--- Star Voyager\'s Mission to Mars Report ---\n')

distance_in_miles = distance_in_km * 0.621371
print(f'The distance from Earth to Mars is {distance_in_km} kilometres or {distance_in_miles} miles')

speed_in_metres_per_second = speed_in_km_per_hour * (1000 / 3600)
print(f'The speed of the spaceship is {speed_in_km_per_hour} kilometres per hour or {speed_in_metres_per_second} miles per second')

time_in_hours = distance_in_km / speed_in_km_per_hour
time_in_days = time_in_hours / 24
print(f'The time to reach Mars is {time_in_hours} hours or {time_in_days} days')

total_fuel_used = distance_in_km * 0.05
print(f'You will use a total of {total_fuel_used} litres of fuel for the entire trip')

center_x = 0
center_y =0

# Distance from centre (0, 0)
distance_from_centre = ((x_coordinate - center_x) ** 2 + (y_coordinate - center_y) ** 2) ** 0.5

print(f'The distance to the landing site on Mars from the central point is: {distance_from_centre} units\n')






