from dataclasses import dataclass


@dataclass
class User:
    name: str
    id: str

    placeInLine = 0
    remainingTime = 0

    def renewTime(self):
        self.remainingTime = 1200  # saniye cinsinden kalan süre

    def decreaseTime(self):
        self.remainingTime = self.remainingTime - 1

        # TODO her 3 dakika da bir bütün kullanıcıları kontrol edip sürelerini azalt
