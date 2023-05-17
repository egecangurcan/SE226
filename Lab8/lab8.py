from abc import ABC, abstractmethod
import string


class AbstractClass(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(AbstractClass):
    def calculateFreqs(self):
        with open(self.address, 'r') as file:
            text = file.read().lower()
            result = []
            for letter in string.ascii_lowercase:
                count = text.count(letter)
                if count > 0:
                    result.append(f"{letter} = {count}")
            print("ListCount")
            for res in result:
                print(res)


class DictCount(AbstractClass):
    def calculateFreqs(self):
        result = {char: 0 for char in string.ascii_lowercase}
        with open(self.address, 'r') as file:
            for line in file:
                for char in line.lower():
                    if char in result:
                        result[char] += 1
                print("DictCount")
            for key, value in result.items():
                if value > 0:
                    print(f"'{key}' {value}")


file_path = "weirdWords.txt"

list_counter = ListCount(file_path)
list_counter.calculateFreqs()

dict_counter = DictCount(file_path)
dict_counter.calculateFreqs()
