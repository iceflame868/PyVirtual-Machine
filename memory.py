import memory_errors


class Memory:

    def __init__(self, bit_amount):
        if 1 > bit_amount:
            # TODO make another exception class
            print("Memory cant be negative")
            raise OverflowError

        self.memory = [0] * bit_amount  # A list will store all of the data and be initialised to all 0's

        # Setters and getters will be used
        self._bit_amount = bit_amount

    @property
    def bit_amount(self):
        return len(self.memory)

    @bit_amount.setter
    def bit_amount(self, value):
        self.memory = self.__memory_list_adjust(self.memory, value)

    def read(self, address, amount):
        """
        Reads amount bits at location
        Returns the bits as an int
        :param address: the location in memory to read from, reads like from small to big, not sure what endia
        :param amount:
        :return: Returns the value read as an int
        """

        # Checks the parameters and calls any errors
        self.__memory_rw_check(address, amount, memory_errors.ReadViolation)

        # This grabs the offset
        memory_selected = self.memory[address: address + amount]

        # Converts the list into one string
        memory_string = ''.join(map(str, memory_selected))

        # This is because we are working with binary numbers
        return int(memory_string, 2)

    def write(self, address, value, amount = None):
        """
        Writes into self memory the information
        If amount is given
        returns a 0 or other value depending on what happened
        :param address: where to write the information
        :param value: what information to right
        :param amount:  The amount of information to write
        :return: Error / Success Code
        """

        # Checks the parameters
        self.__memory_rw_check(address, value, memory_errors.WriteViolation)

        # The length of the bits that is going to be writen
        value_bit_length = value.bit_length()

        '''
        This creates list, by converting the information into a string representation of a byte
        removes the 0b bit at the front, and then converts each element into a list
        '''
        binary_value_list = [int(bit) for bit in bin(value)[2:]]

        # If there is an amount specified, change the binary list else to nothing
        if amount is not None:
            self.__memory_rw_check(address, amount, memory_errors.WriteViolation)
            # This is for padding or removing if amount if supplied
            binary_value_list = self.__memory_list_adjust(binary_value_list, amount)

            # This is the true amount that we be write to memory
            value_bit_length = amount

        # This actually writes to the memory
        # This is a more rigid approach rather than just [location:]
        self.memory[address: address + value_bit_length] = binary_value_list
        return 0

    @staticmethod
    def __memory_list_adjust(value_list, wanted_amount):
        """
        If the values are the same, nothing happens
        Else the list will get trunc if the wanted amount if smaller than the list
        If the wanted amount is greater than the list it will be padded with int 0's
        :param value_list: The list that wants to be changed
        :param wanted_amount: The length that the list should be at
        :return: The changed list
        """
        list_len = len(value_list)

        # If they are the same value dont do anything
        if list_len == wanted_amount:
            return

        elif list_len != wanted_amount:
            # The difference that the values have within each other
            list_length_difference = abs(list_len - wanted_amount)

            # If we need to pad
            if wanted_amount > list_len:
                return value_list + [0] * list_length_difference
            # If we need to trunc
            elif list_len > wanted_amount:
                return value_list[:list_length_difference]

    def __memory_rw_check(self, address, amount, exception_handler):
        """
        This checks the two values, and sees if they can be used on the memory
        Calsl the exception handler if the comparisons dont work
        :param address:
        :param amount:
        :param exception_handler:
        :return:
        """
        if 0 > address:
            raise exception_handler(address, "Address is negative")
        elif address > 2 ** self.bit_amount:
            raise exception_handler(address, "Address is larger than memory can access")

        if 0 > amount:
            raise exception_handler(address, "Amount is negative")

        if address + amount > 2 ** self.bit_amount:
            raise exception_handler(address, "Attempting to access memory larger than max value")


    @staticmethod
    def overwrite():
        # Overwrites the memory
        pass

    @staticmethod
    def insert():
        # Inserts the memory, by pushing the other memory away
        pass

    @staticmethod
    def combine():
        # Combines the two memories
        pass

    def __str__(self):
        return str(self.memory)

    def __repr__(self):
        return str({"Memory": self.memory, "Memory Size": self.bit_amount})

    def __len__(self):
        """

        :return: How much memory was it currently has
        """
        return self.bit_amount

    # TODO change this methods so that they return a class or prehaps something
    def __mul__(self, other: int):
        """
        This just returns the
        :param other: The amount of multiply it by
        :return:
        """
        return self.memory * other

    def __add__(self, other):
        """
        Concats the two memories
        :param other: Needs to be of a memory object
        :return:
        """
        return self.memory + other.memory


if __name__ == "__main__":
    x = Memory(1024)
    print(str(x.read(0, 20)))