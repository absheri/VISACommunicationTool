import visa

# Define the resource manager
rm = visa.ResourceManager()


class CommunicationInterface:
    def __init__(self):
        self.rm = visa.ResourceManager()
        '''
         Get Connected Resource
            resources       ---> Hold all available resources
            my_instrument   ---> Instrument Driver
        '''
        self.resources = rm.list_resources()
        self.my_instrument = self.rm.open_resource(self.resources[0])
        '''
         Return the serial number of instrument held by my_instrument
        '''
    def device_identification(self):
        return self.my_instrument.query('*IDN?')

    def test(self):
        return self.my_instrument.write('DISplay:CLOCk ON')


