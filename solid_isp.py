from abc import abstractmethod

# Invalid because of:
# child model may not support fax/scan functions but still will be able to call
class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

class Printer:
    @abstractmethod
    def print(self, document):
        pass 

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass 


class MultiFunctionMachine(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass 

    @abstractmethod
    def scan(self, document):
        pass 

class PrinScanner(MultiFunctionMachine):
    def print(self, document):
        '''do something exact'''
        
    def scan(self, document):
        '''do something exact '''