import visa

# Define the resource manager


class CommunicationInterface:
    def __init__(self):
        self.rm = visa.ResourceManager()
        '''
         Get Connected Resource
            resources       ---> Hold all available resources
            my_instrument   ---> Instrument Driver
        '''
        self.resources = self.rm.list_resources()
        self.my_instrument = self.rm.open_resource(self.resources[0])
        '''
         Return the serial number of instrument held by my_instrument
        '''
    def device_identification(self):
        return self.my_instrument.query('*IDN?')

    def write_to_device(self,command):
        self.my_instrument.write(command)

    def query_from_device(self,command):
        return self.my_instrument.query(command)




