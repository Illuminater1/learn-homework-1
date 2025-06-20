"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def hello_user():
    try:
        while True:
            user_message = input("Как дела?\n")
            if user_message == "Хорошо":
                break
            else:
                continue
    except KeyboardInterrupt:
        print("Пока")

if __name__ == "__main__":
    hello_user()
