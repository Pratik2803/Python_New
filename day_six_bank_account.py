from typing import Union


class BankAccount:
    """
    Class representing a bank account with deposit, withdraw, 
    and bank name change functionalities.
    """

    bank_name = "Savings Bank"  # Class-level attribute

    @staticmethod
    def _validate_transaction_amount(amount: Union[int, float]) -> None:
        if not isinstance(amount, (int, float)) or not amount > 0:
            raise ValueError("Amount must be a positive number.")

    @staticmethod
    def _validate_balance(balance: Union[int, float]) -> None:
        if not isinstance(balance, (int, float)):
            raise ValueError(
                "Balance must be a numeric value.")

    @staticmethod
    def _validate_input_string(input_string: str) -> None:
        if not isinstance(input_string, str) or not input_string.strip():
            raise ValueError("Must be a non-empty string.")

    def __init__(self, owner: str, balance: Union[int, float] = 0.0) -> None:
        """
        Initialize a BankAccount instance.

        :param owner: The name of the account owner (must be a non-empty string).
        :param balance: Initial balance (must be numeric).
        :raises ValueError: If balance is not a valid numeric type.
        """
        self._validate_input_string(owner)
        self.owner = owner.strip()

        self._validate_balance(balance)
        self.balance = float(balance)  # Ensure Balance is always float

    @classmethod
    def change_bank(cls, new_bank_name: str) -> None:
        """
        Change the bank name at the class level.

        :param new_bank_name: The new bank name.
        """

        cls._validate_input_string(new_bank_name)
        cls.bank_name = new_bank_name.strip()

    def deposit(self, money: Union[int, float]) -> None:
        """
        Deposit money into the account.

        :param amount: The amount to deposit.
        :raises ValueError: If amount is not valid.
        """
        self._validate_transaction_amount(money)

        self.balance += money
        print(f"Deposited {money}. New balance: {self.balance}")

    def withdraw(self, money):
        """
        Withdraw money from the account.

        :param amount: The amount to withdraw.
        :raises ValueError: If amount is not valid or exceeds the balance.
        """

        self._validate_transaction_amount(money)

        if self.balance < money:
            print(
                f"Insufficent money you can withdraw maximum {self.balance}")
        else:
            self.balance -= money
            print(
                f"Successful money withdrawal {self.balance}")


my_account = BankAccount("Pratik", 123)
my_account.deposit("abc")
my_account.deposit(1000)
# my_account.withdraw("abc")
my_account.withdraw(100000)
my_account.withdraw(100)
