#set cars equal to 100
cars = 100

#set spaces in car to 4.0
space_in_a_car = 4

#set drivers  equal to 30
drivers = 30

#set passengers equal to 90
passengers = 90

#set the numbers of cars not drive to te numbers of
#cars minus the number of drivers
cars_not_driven = cars - drivers

cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven

print "There are" , cars, "cars available."
print "There are only" , drivers, "drivers available."
print "There will be" , cars_not_driven, "empty cars today"
print "We can transport" , carpool_capacity, "people today."
print "We have" , passengers, "to carpool today."
print "We need to put about" , average_passengers_per_car, "in each car."

#study drill
print cars * space_in_a_car
