import pickle
from argparse import ArgumentParser
from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, owner_name: str, balance: int):
        self.owner_name = owner_name
        self._balance = balance

    def add(self, amount: int):
        self._balance += amount
    
    def sub(self, amount: int):
        self._balance -= amount
    
    @abstractmethod
    def transfer(self, other: "BankAccount", amount: int):
        pass

    @staticmethod
    def to_rial(amount: int):
        return amount * 10

    def __repr__(self) -> str:
        dictionary = vars(self)
        dictionary["rial"] = self.to_rial(self._balance)
        return str(dictionary)
    
    def __str__(self) -> str:
        return f"{self.owner_name} : {self._balance:,}"


class AyandehBankAccount(BankAccount):
    
    __MINIMUM = 10_000
    __accounts = []

    def __init__(self, owner_name: str, balance: int):
        super().__init__(owner_name, balance) 
        type(self).__accounts.append(self)

    def add(self, amount: int):
        if self._balance + amount < self.__MINIMUM:
            raise ValueError("Invalid Balance")

        return super().add(amount)

    def sub(self, amount: int):
        if self._balance - amount < self.__MINIMUM:
            raise ValueError("Invalid Balance")

        return super().sub(amount)
    
    def transfer(self, other: "BankAccount", amount: int):
        self.sub(amount + 600)
        other.add(amount)
    
    @classmethod
    def maximum(cls) -> int:
        return max(
            [account._balance for account in cls.__accounts]
        )

    @classmethod
    def save(cls):
        with open("account.pickle", "wb") as file:
            pickle.dump(cls.__accounts, file)

    @classmethod
    def load(cls):
        with open("account.pickle", "rb") as file:
            cls.__accounts.extend(pickle.load(file))




def main():
    # print(AyandehBankAccount.mro())

    # parser = ArgumentParser(description="Bank Account Manager")
    # parser.add_argument("-f", "--fist", metavar="FIRST", required=True, type=int)
    # parser.add_argument("-s", "--second", metavar="Second", default=50_000, type=int)
    # parser.add_argument("-a", "--amount", metavar="AMOUNT", type=int, help="Value")
    # if __name__ == "__main__":
    #     args = parser.parse_args()
    #     account1 = AyandehBankAccount('pouriya', args.first)
    #     account2 = AyandehBankAccount('kimiya', args.second)
    #     t = args.amount
    #     account1.transfer(account2, t)
    #     print(account1._balance)
    #     print(account2._balance)
        
    # account1 = AyandehBankAccount('pouriya', 5_000_000)
    # account2 = AyandehBankAccount('amir', 3_000_000)
    # AyandehBankAccount.save()

    account3 = AyandehBankAccount('simon', 1_500_000)
    print(AyandehBankAccount._AyandehBankAccount__accounts)
    AyandehBankAccount.load()
    print(AyandehBankAccount._AyandehBankAccount__accounts)
    print(AyandehBankAccount._AyandehBankAccount__accounts[0].balance)
    print(AyandehBankAccount._AyandehBankAccount__accounts[1].balance)
    print(AyandehBankAccount._AyandehBankAccount__accounts[2].balance)


if __name__ == "__main__":
    main()