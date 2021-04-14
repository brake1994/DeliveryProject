import csv
import datetime
from HashTable import ChainingHashTable

# Read Package file and parse data
# O(N)
with open('./Data/WGUPS_Package_File.csv') as csv_file:
    read_file = csv.reader(csv_file, delimiter=',')

    packages = ChainingHashTable()
    package_ids = []
    pack_addresses = []
    first_truck = [2, 40, 20, 21, 19, 16, 15, 14, 13, 1, 33, 7, 6, 25, 31, 34]
    second_truck = [3, 10, 18, 36, 38, 27, 35, 39, 8, 30, 5, 37, 23, 11, 29]
    third_truck = [9, 26, 28, 22, 24, 32, 17, 4, 12]

    for row in read_file:
        packageID = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zipCode = row[4]
        deadline = row[5]
        weight = row[6]
        notes = row[7]
        delivery_status = "At the hub"
        start_time = datetime.datetime(2021, datetime.datetime.now().month, datetime.datetime.now().day, hour=0,
                                       minute=0)
        delivery_timestamp = datetime.datetime(2021, datetime.datetime.now().month, datetime.datetime.now().day, hour=0,
                                               minute=0)
        pack_addresses.append(address)

        package_ids.append(packageID)
        values = [packageID, address, city, state, zipCode, deadline, weight, notes, delivery_status, start_time,
                  delivery_timestamp]
        packages.insert(packageID, values)

    # Search for packages based on any string entry
    # Id should also be entered as a string if using this function
    # O(N)
    def search_Packages(search_entry):
        results_found = []
        for i in range(41):
            result = str(packages.search_key(i))
            if result.__contains__(search_entry):
                results_found.append(packages.search_key(i))
        if len(results_found) > 0:
            print("\n".join(map(convert_to_string, results_found)))
        else:
            print("No packages found.")

    # Used to convert all elements of array of arrays to string
    # Needed to display datetime in a readable format for search function
    # O(N)
    def convert_to_string(array):
        t = [array]
        for s in t:
            return ", ".join(map(str, s))

    # Set delivery time for package object
    # O(1)
    def set_delivery_timestamp(package_id, time):
        packages.search_key(package_id)[10] = time

    # Set delivery start time for package object
    # O(1)
    def set_start_time(package_id, time):
        packages.search_key(package_id)[9] = time

    # Display all package statuses at certain time
    # O(N)
    def get_all_package_status(hour, minutes):
        status_list = []
        time_checked = datetime.datetime(2021, datetime.datetime.now().month, datetime.datetime.now().day, hour=hour,
                                         minute=minutes)
        for p in packages.get_values():
            if p[9] < time_checked < p[10] or time_checked == p[9]:
                p[8] = "En route"
            elif time_checked < p[9]:
                p[8] = "At the hub"
            elif p[10] < time_checked or time_checked == p[10]:
                p[8] = "Delivered"
            status_list.append((p[0], p[8]))

        status_list.sort()
        print("All package statuses at ", time_checked)
        print("Package ID  -  Status ")
        for i, e in enumerate(status_list):
            if (i + 1) % 4 == 0:
                print(e)
            else:
                print(e, end='   ')

    # Function to check if all package deadlines are met.
    # O(N)
    def packages_delivered_on_time():
        t = datetime.datetime(2021, datetime.datetime.now().month, datetime.datetime.now().day)
        day = str(t.day)
        month = str(t.month)
        year = str(t.year)
        dt = day + " " + month + " " + year + " "
        late_packages = []
        for p in packages.get_values():
            time = "".join(p[5])
            package_id = p[0]
            if time != "EOD":
                t = t.strptime(str(dt + time), "%d %m %Y %I:%M %p")
                if t < p[10]:
                    print(t, p[10])
                    late_packages.append(package_id)
        if len(late_packages) > 0:
            print("Packages with id: %s are late.", late_packages)
        else:
            print("All packages delivered on time.")

