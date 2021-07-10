class Vehicle:
    """
    Attributes
    ----------
    _make : str
        vehicle manufacturer name
    _model : str
        variant of vehicle make
    _year : int
        manufacturing year of vehicle
    _color : str
        color of vehicle
    _mileage : int
        mileage of vehicle
    _price : str
        price of vehicle(20L)
    customer : str
        first name of customer
    logger : object
        logger object
    Methods
    -------
    add_vehicle():
        Adding attributes of vehicle
        returns : True (if successfully added vehicle record)
                : False (fails in adding vehicle record)
    """
    def __init__(self, logger):
        """
        :param logger: logger object
        """
        self._make = ''
        self._model = ''
        self._year = 0
        self._color = ''
        self._mileage = ''
        self._price = 0
        self.customer = '-'
        self.logger = logger

    def __str__(self):
        """
        :return: object details in readable format
        """
        return "\t".join(str(x) for x in [self._make, self._model, self._year, self._color, self._mileage, self._price, self.customer])

    def add_vehicle(self):
        """
        Adding attributes of vehicle
        returns : True (if succesfully added vehicle record)
                : False (fails in adding vehicle record)
        """
        try:
            self.logger.info("Adding/Updating Vehicle record... ")
            self._make = input('Enter vehicle make: ')
            self._model = input('Enter vehicle model: ')
            self._year = int(input('Enter vehicle year: '))
            self._color = input('Enter vehicle color: ')
            self._mileage = int(input('Enter vehicle mileage: '))
            self._price = input('Enter vehicle price: ')
            self.logger.info("Added vehicle record :: {}".format(self.__str__()))
            return True
        except ValueError:
            self.logger.error("Year and Mileage value is not whole number")
            print('Enter valid details for year and mileage')
            return False