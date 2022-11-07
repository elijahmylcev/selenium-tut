def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

to_pay_in_html = '1,465.00 RUB'
words_list = to_pay_in_html.split()
print(words_list)
for num in words_list:
    number = num.replace(",", "")
    if is_number(number):
        to_pay = float(number)
        print(f'to_pay: {to_pay}')
