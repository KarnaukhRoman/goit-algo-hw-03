
from datetime import datetime as dtdt
import random
import re
import datetime as dt

def get_days_from_today(date_str):
    """The function accepts the date value in "'YYYY-MM-DD'" format and
    returns the number of days between the current date and the entered date.
    """
    current_date = dtdt.today()
    #використовуєм метод toordinal(), який повертає порядковий номер дня, 
    #враховуючи кількість днів з 1 січня року 1 нашої ери.
    return current_date.toordinal() - date_str.toordinal()
    


def hw_first():
    # використовуємо цикл для того, щоб не запускати ПЗ після помилки вводу користувача
    flag = True
    while flag: 
    # Вмикаєм контроль над невірно введеними даними 
        try:
            # Очукуэм від користувача введення даних в форматі РРРР-ММ-ДД
            date_str = input('Enter date in the format YYYY-MM-DD: ')
            #Перетворюємо тип стринг в датетайм
            date_object = dtdt.strptime(date_str, '%Y-%m-%d').date()
            # При коректному введені дати, скидаєм флаг, щоб вийти з циклу
            flag = False
        except Exception as e:
            print(f"ERROR: {e}\n")
    print(f"The number of days between the specified date and the current date: {get_days_from_today(date_object)}")

hw_first() #зстартуємо перше завдання

#Завдання 2 ***************************************************************************
def get_numbers_ticket(min, max, quantity):
    '''The function returns a random set of numbers within the specified parameters, 
    and all random numbers in the set are unique.
    '''
    lot = []
    if (min<1 or 1>min>=1000): # Перевіряєм щоб змінна min не виходила за край інтервалу 1>min>1000
        print(f"Number 'min: '{min} out of range") 
    elif (max<1 or max>1000): # Перевіряєм щоб змінна max не виходила за край інтервалу 1>max>1000
        print(f"Number 'max: '{max} out of range: ")
    elif min>=max: # # Перевіряєм щоб змінна min не була більша або дорівнювала max
        print(f"Number min: {min}  cannot be greater or equal than number max: {max} ")
    elif quantity>max: # Перевіряєм щоб змінна quantity не була більша за max 
        print(f"Number quantity: {quantity}  cannot be greater than number max: {max} ")
    else: # Якщо помилок не занайдено     
        # в циклі наповнюємо список заданою кількістю випадкових значень, описаних змінною 'quantity'
        while len(lot)<quantity:
            #методом randint, отримуєм випадкові зачення в диапазоні min, max
            a=random.randint(min,max)
            #якщо значення, які додаються і знаходяться в списку, не повторюється, то додаєм до списка
            if a not in lot: 
                lot.append(a)
        #сортуємо список в порядку зростання та повертаєм результат роботи функції      
    return sorted(lot)


#print(f'Your lottery numbers {get_numbers_ticket(1, 36, 5)}')

# Завдання 3 *************************************************************************
def normalize_phone(num):
    """The feature normalizes phone numbers to a standard format. """
    #за допомогою методу findall() регулярного виразу, шукаємо в рядку символ "+" та усі цифри.
    #так, як результат роботи методу findall() повертає список знайдених символів, з'еднуємо в строку. 
    num_str = ''.join((re.findall(r'\+|\d+', num)))
    #Перевіряємо строку на повноту заповнення
    match len(num_str):
        case 13:# так як номер складається з 12 цифр та символу "+" (всього 13), вважаєм що номер заповнений повністю
            return num_str
        case 12:# вважаєм, що відсутній символ "+"
            return '+' + num_str
        case 10:# вважаем що номер записан в скороченому форматі (050 або 067), ддодаєм код країни "+38"
            return '+38' + num_str
        
#*************
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)      

# Завдання 4 **************************************************************************************        
                         
def get_upcoming_birthdays(users):
    '''The function returns a list of dictionaries, 
    where each dictionary contains information about the user (name key) and 
    the date of congratulation (congratulation_date key, whose data is in the format of the string 'year.month.date').
    '''
    curent_date = dtdt.today().date() # беремо поточну дату
    birthdays=[] # створюємо список для повернення результатів
    for user in users:
        # отримуємо дату народження людини у вигляді рядка та змінюємо рік на поточний
        birthday_date=str(curent_date.year)+ user["birthday"][4:]  
        birthday_date=dtdt.strptime(birthday_date, "%Y.%m.%d").date() # перетворюємо дату народження в об’єкт date
        week_day_bdate=birthday_date.isoweekday() # Отримуємо день тижня (1-7)
        days_between=(birthday_date-curent_date).days # рахуємо різницю між поточною датою та днем народження цьогоріч у днях
        if 0<=days_between<7: # якщо день народження протягом 7 днів від сьогодні
            match week_day_bdate:
                case 6: #якщо день народження в суботу, додаєм 2 дні та додаєм запис в словник
                    birthdays.append({'name':user['name'], 'congratulation_date':(birthday_date+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
                case 7: #якщо день народження в суботу, додаєм 1 дні та додаєм запис в словник
                    birthdays.append({'name':user['name'], 'congratulation_date':(birthday_date+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                case _: #якщо день народження не в суботу та не в неділю, додаєм запис в словник без змін
                    birthdays.append({'name':user['name'], 'congratulation_date':birthday_date.strftime("%Y.%m.%d")}) 
       
    return birthdays                  

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.26"},
    {"name": "Kamal Fikri", "birthday": "1990.01.28"},
    {"name": "Adrian Barra", "birthday": "1995.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

