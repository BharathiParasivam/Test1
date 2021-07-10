from vehicle import Vehicle

class Inventory:
    """
    Attributes
    ----------
    vehicles : list
        list of vehicle record objects
    logger : object
        logger object
    Methods
    -------
    add_vehicle():
        Adding attributes of vehicle

    view_vehicles():
        To fetch vehicle details in inventory
        :return: True (if vehicle record found)
                 False (if no vehicle record found)

    delete_vehicle():
        To delete selected vehicle record

    update_vehicle():
        To update vehicle details of selected record

    book_vehicle():
        To book vehicle by customer
    """
    def __init__(self, logger):
        """
        :param logger: logger object
        """
        self.vehicles =[]
        self.logger = logger

    def add_vehicle(self):
        """
        Adding attributes of vehicle
        :return: None
        """
        vehicle = Vehicle(self.logger)
        if vehicle.add_vehicle():
            self.logger.info('Adding vehicle details in progress...')
            self.vehicles.append(vehicle)
            self.logger.info("Total number of vehicle records - {}".format(len(self.vehicles)))
            print("Successfully added vehicle details!!!")
        else:
            self.logger.error("Adding vehicle to inventory Failed!!!")
            print("Adding vehicle to inventory Failed!!!")

    def view_vehicles(self):
        """
        To fetch vehicle details in inventory
        :return: True (if vehicle record found)
                 False (if no vehicle record found)
        """
        if self.vehicles:
            self.logger.info("Fetching vehicle records...")
            print("\t\t\t\tOur Inventory Vehicle details\t\t\t\t")
            print('\t'.join(['Serial', 'Make', 'Model', 'Year', 'Color', 'Mileage', 'Price', 'Booked for Customer']))
            self.logger.info('\t'.join(['Serial', 'Make', 'Model', 'Year', 'Color', 'Mileage', 'Price', 'Booked for Customer']))
            for serial, vehicle in enumerate(self.vehicles):
                print(serial + 1, end='\t')
                print(vehicle)
                self.logger.info('\t\t'.join([str(serial + 1),str(vehicle)]))
            return True
        else:
            self.logger.warning("No vehicle records found in Inventory!!!")
            print("No vehicle records found in Inventory!!!")
            return False

    def delete_vehicle(self):
        """
        To delete selected vehicle record
        :return: none
        """
        if self.view_vehicles():
            item = int(input('Select the number associated with vehicle record to be deleted: '))
            self.logger.info('Selected vehicle record id for deletion:: {}'.format(item))
            if 0 < item <= len(self.vehicles):
                self.logger.info('Deleting vehicle record in progress...')
                self.logger.info("Vehicle record to be deleted :: {} ".format(self.vehicles[item-1]))
                self.vehicles.pop(item-1)
                print("Successfully deleted Vehicle record", end='\n')
                print("Updated Inventory details as below::")
                self.view_vehicles()
            else:
                self.logger.error("Selected vehicle record number is not valid")
                print("Enter a Valid number!!!")

    def update_vehicle(self):
        """
        To update vehicle details of selected record
        :return: None
        """
        if self.view_vehicles():
            item = int(input('Select the number associated with vehicle record to be updated: '))
            self.logger.info('Selected vehicle record id for update :: {}'.format(item))
            if 0 < item <= len(self.vehicles):
                self.logger.info('Updating vehicle details in progress...')
                self.logger.info("Before update :: {} ".format(str(self.vehicles[item - 1])))
                self.vehicles[item - 1].add_vehicle()
                self.logger.info("After update :: {} ".format(str(self.vehicles[item - 1])))
                print("Successfully updated Vehicle record", end='\n')
                print("Updated Inventory details as below::")
                self.view_vehicles()
            else:
                self.logger.error("Selected vehicle record number is not valid")
                print("Enter a Valid number!!!")

    def book_vehicle(self):
        """
        To book vehicle by customer
        :return: None
        """
        if self.view_vehicles():
            item = int(input('Select the number associated with vehicle record to be Booked: '))
            self.logger.info('Selected vehicle record id for Booking :: {}'.format(item))
            if 0 < item <= len(self.vehicles):
                self.logger.info('Booking vehicle in progress...')
                if self.vehicles[item - 1].customer == '-':
                    self.vehicles[item - 1].customer = input("Please enter your name for booking selected vehicle:")
                    print("Successfully Booked Vehicle", end='\n')
                    self.logger.info("Customer {} successfully booked Vehicle :: {}".format(self.vehicles[item - 1].customer, str(self.vehicles[item - 1])))
                    print('\t'.join(['Make', 'Model', 'Year', 'Color', 'Mileage', 'Price', 'Booked for Customer']))
                    print(self.vehicles[item - 1])
                else:
                    self.logger.error("Booking failed as selected vehicle is already booked.")
                    print("Selected vehicle is already booked...Please visit us again")
            else:
                self.logger.error("Selected vehicle record number is not valid")
                print("Enter a Valid number!!!")
        else:
            self.logger.error("Booking failed as no vehicle found")
            print("Please visit us again!!!")
