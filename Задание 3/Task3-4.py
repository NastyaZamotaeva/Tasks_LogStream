# 1)Напишите класс “кошелек”, у которого есть следующие атрибуты: 
# баланс, валюта и имя кошелька. 
# Напишите атрибут класса “платежная система”. 
# Создайте методы: пополнение баланса, оплата, 
# вывод инфо о количестве средств на балансе и удаление счета. 
# Сделайте проверку, что списание с баланса возможно 
# (средств хватает на операцию).

#2)*Создайте класс “крипто-кошелек”, наследуемый от класса “кошелек”. 
# Создайте в этом классе атрибут “коин”, 
# остальные атрибуты должны идти с родительского класса. 
# Измените метод информации о средствах на балансе, 
# который покажет количество коинов на балансе. 
# Добавьте метод информации о средствах на балансе в долларах, 
# который переводит коины в доллары. 
# К примеру, можно использовать 2 коина: 1 BTC = 72000 USD, 1 ETH = 3500 USD.

class Wallet:
    payment_system = "Payment system"
    def __init__(self, currency: str, name_wallet: str):
        if currency not in ("USD", "EUR", "RUB"):  # Проверка валюты
            raise ValueError("Валюта должна быть одной из: USD, EUR, RUB.")
        self._balance = 0.0  # Защищенный атрибут баланса
        self.currency = currency
        self.name_wallet = name_wallet

    # Пополнение баланса
    def replenishment_balance(self) -> None:
        sum_balance = float(input("Введите сумму пополнения:\n"))
        if sum_balance <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self._balance += sum_balance
        print(f"Баланс пополнен на {sum_balance} {self.currency}. Текущий баланс: {self._balance} {self.currency}.")

    # Оплата
    def payment(self) -> None:
        pay = float(input("Введите сумму оплаты:\n"))
        if self._balance < pay:
            print("Средств не хватает на операцию!")
        else:
            self._balance -= pay
            print(f"Оплачено {pay} {self.currency}. Текущий баланс: {self._balance} {self.currency}.")

    # Вывод информации о количестве средств на балансе
    def info_balance(self) -> None:
        print(f"Средства оставшиеся на балансе: {self._balance} {self.currency}.")

    # Удаление счета
    def del_account(self) -> None:
        self._balance = 0
        print("Счет закрыт.")


class CryptoWallet(Wallet):
    def __init__(self, currency: str, name_wallet: str, coin: str) -> None:
        super().__init__(currency, name_wallet)
        self.coin = coin  
        self.coin_translation = {
            "BTC": 72000, 
            "ETH": 3500
        }
        if coin not in self.coin_translation:
            raise ValueError("Коин должен быть одним из: BTC, ETH.")

    def info_balance(self) -> None:
        """Вывод информации о количестве коинов на балансе"""
        coins = self._balance 
        print(f"Количество коинов на балансе: {coins:.4f} {self.coin}.")

    def info_balance_usd(self) -> None:
        """Вывод информации о количестве средств на балансе в долларах"""
        dollar_balance = self._balance
        print(f"Средства на балансе в долларах: {dollar_balance:.2f} USD.")


# Создание кошелька
wallet = Wallet("USD", "Мой Кошелек")
wallet.replenishment_balance()  # Ввод суммы пополнения
wallet.payment()  # Ввод суммы для оплаты
wallet.info_balance()  # Вывод баланса
wallet.del_account()  # Удаление счета

# Создание крипто-кошелька
crypto_wallet = CryptoWallet("USD", "Мой КриптоКошелек", "BTC")
crypto_wallet.replenishment_balance()  # Ввод суммы пополнения
crypto_wallet.info_balance()  # Вывод информации о коинов
crypto_wallet.info_balance_usd()  # Вывод информации о балансе в долларах