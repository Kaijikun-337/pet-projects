from enum import Enum


class VendingMachine:
    IDLE = 0
    HAS_MONEY = 1
    
    def __init__(self):
        self.state = self.IDLE
    
    def handle_input(self, input):
        if input == "Insert Coin":
            self.state = self.HAS_MONEY
            pass
        elif input == "Select Soda" and self.state == 1:
            self.state = self.IDLE
            print('Dispensing Soda')
            pass
        else:
            print('Insert a coin first!')
            
vm = VendingMachine()
vm.handle_input("Select Soda") # Should fail
vm.handle_input("Insert Coin") # Should work
vm.handle_input("Select Soda") # Should dispense
           