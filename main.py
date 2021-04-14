import datetime
import Core_Algorithm
import Distance
import Packages

# Name: Tanner Brake   Student ID: 581136
if __name__ == '__main__':
    # Initializing values and populating distance/package id comparison table
    Distance.compare_addresses()
    total_distance = 0
    start_time_truck_1_2 = datetime.datetime(2021, datetime.datetime.now().month, datetime.datetime.now().day, hour=8,
                                             minute=0)
    # Deliver truck 1 and 2. Also get end times / distance
    truck_1_end_time = Core_Algorithm.deliver_packages(Packages.first_truck, start_time_truck_1_2)[0]
    truck_2_end_time = Core_Algorithm.deliver_packages(Packages.second_truck, start_time_truck_1_2)[0]
    truck_1_distance = Core_Algorithm.deliver_packages(Packages.first_truck, start_time_truck_1_2)[1]
    truck_2_distance = Core_Algorithm.deliver_packages(Packages.second_truck, start_time_truck_1_2)[1]
    # Truck 3 start time
    start_time_truck_3 = datetime.datetime(2021, datetime.datetime.now().month, datetime.datetime.now().day, hour=10,
                                           minute=30)
    # Deliver truck 3 and get distance
    truck_3_distance = Core_Algorithm.deliver_packages(Packages.third_truck, start_time_truck_3)[1]
    # Sum total distance
    total_distance += truck_1_distance + truck_2_distance + truck_3_distance
    # Checking if all deadlines are met
    Packages.packages_delivered_on_time()

    # Command line interface
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def menu():
        print("Menu options - enter number below")
        print("Type 'close application' to stop application")
        print("1 - Search packages by any criteria")
        print("2 - Search packages status by time")
        print("3 - Show total distance traveled")
        user_input = input("Type Here: ")
        while user_input != "close application":
            if user_input == "1":
                while user_input != "menu" or user_input != "close application":
                    print("Type 'menu' to return to main menu")
                    print("Type 'close application' to stop application")
                    user_input = input("Search for packages: ")
                    print("\n")
                    Packages.search_Packages(user_input)
                    print("\n")
                    if user_input == "menu":
                        menu()
                    if user_input == "close application":
                        break
            if user_input == "2":
                while user_input != "menu" or user_input != "close application":
                    print("Enter time to check status of all packages")
                    print("Input based on 24 hr clock")
                    user_input_hour = input("hour = ")
                    user_input_minute = input("minutes = ")
                    user_input = input("Type 'menu' here to return to the main menu or just press enter to get results: ")
                    if user_input_hour != "" and user_input_minute != "":
                        Packages.get_all_package_status(int(user_input_hour), int(user_input_minute))
                    if user_input == "menu":
                        menu()
                    if user_input == "close application":
                        break
            if user_input == "3":
                while user_input != "menu" or user_input != "close application":
                    print("Select an option.")
                    print("Type 'menu' to return to main menu")
                    print("Type 'close application' to stop application")
                    print("1 - Truck 1 distance traveled")
                    print("2 - Truck 2 distance traveled")
                    print("3 - Truck 3 distance traveled")
                    print("4 - Combined distance of all trucks")
                    user_input = input("Type option here: ")
                    if user_input == "1":
                        print("\n", "Truck 1 distance: ", truck_1_distance, " miles", "\n")
                    if user_input == "2":
                        print("\n", "Truck 2 distance: ", truck_2_distance, " miles", "\n")
                    if user_input == "3":
                        print("\n", "Truck 3 distance: ", truck_3_distance, " miles", "\n")
                    if user_input == "4":
                        print("\n", "Total distance by all trucks: ", total_distance, " miles", "\n")
                    if user_input == "menu":
                        menu()
                    if user_input == "close application":
                        break
            else:
                menu()

    # Calling start menu
    menu()
