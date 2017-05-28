import visa

# Define the resource manager


class CommunicationInterface:

    def __init__(self, ):
        self.rm = visa.ResourceManager()
        self.my_instrument = None
        '''
         Get Connected Resource
            resources       ---> Hold all available resources
            my_instrument   ---> Instrument Driver
        '''
        self.resources = self.rm.list_resources()

    def set_current_device(self, ip_address = None):
        if not IP_address:
            self.my_instrument = self.rm.open_resource(self.resources[0])
        else:
            self.my_instrument = self.rm.open_resource('TCPIP::'+ip_address)
        return self.my_instrument.query('*IDN?')

    def write_to_device(self,command):
        self.my_instrument.write(command)

    def query_from_device(self,command):
        return self.my_instrument.query(command)




