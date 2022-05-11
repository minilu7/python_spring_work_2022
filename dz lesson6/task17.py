# todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
# Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
# Цены хранятся в словаре:
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}
def compute_bill(prices):
  x=0
  chek = dict()
  for key in prices:
    print(key)
    chek[key] = float (input("введите количество: ")) * prices[key]
    x += chek[key]
  return x

print(compute_bill(prices))