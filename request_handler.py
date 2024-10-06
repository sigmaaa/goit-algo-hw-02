from queue import Queue


queue = Queue()
request_counter = 0

# Функція generate_request():
#     Створити нову заявку
#     Додати заявку до черги

# Функція process_request():
#     Якщо черга не пуста:
#         Видалити заявку з черги
#         Обробити заявку
#     Інакше:
#         Вивести повідомлення, що черга пуста

# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок


def generate_request():
    global request_counter
    request_id = request_counter
    request_counter += 1
    queue.put(request_id)


def process_request():
    if not queue.empty():
        request_id = queue.get()
        print(f"request with id {request_id} processed")
    else:
        print("request's queue is empty")


if __name__ == '__main__':
    while (input("Press enter to continue. Type \"exit\" to finish")
           != "exit"):
        generate_request()
        process_request()
