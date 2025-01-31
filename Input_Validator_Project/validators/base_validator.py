from abc import ABC, abstractmethod


class BaseValidator(ABC):

    @abstractmethod
    def validate(self, value: any) -> bool:
        pass
