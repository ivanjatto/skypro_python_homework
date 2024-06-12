
from Address import Address
from Mailing import Mailing


to_address = Address("123456", "Москва", "Пушкина", "10", "25")


from_address = Address("654321", "Санкт-Петербург", "Ленина", "5", "12")


mail = Mailing(to_address, from_address, 1000, "123456789")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, "
      f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, "
      f"{mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")