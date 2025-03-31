import multiprocessing
import threading
import time
import codecs
from datetime import datetime


def process_a(input_queue, output_queue):
    """
    Процесс A: принимает сообщения из input_queue, преобразует их в нижний регистр,
    добавляет временную метку и отправляет в output_queue (одно сообщение раз в 5 секунд).
    """
    while True:
        # Получаем сообщение из очереди
        message = input_queue.get()
        if message is None:  # Сигнал завершения
            break

        # Преобразуем сообщение в нижний регистр
        processed_message = message.lower()

        # Добавляем временную метку
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        processed_message_with_time = f"[{timestamp}] {processed_message}"

        # Отправляем сообщение в очередь процесса B
        output_queue.put(processed_message_with_time)

        # Ждем 5 секунд перед отправкой следующего сообщения
        time.sleep(5)


def process_b(input_queue, output_queue):
    """
    Процесс B: принимает сообщения из input_queue, кодирует их через ROT13,
    печатает результат в stdout с временной меткой и отправляет в output_queue.
    """
    while True:
        # Получаем сообщение из очереди
        message = input_queue.get()
        if message is None:  # Сигнал завершения
            break

        # Кодируем сообщение через ROT13
        rot13_message = codecs.encode(message, 'rot_13')

        # Добавляем временную метку
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        encoded_message_with_time = f"[{timestamp}] {rot13_message}"

        # Печатаем результат в stdout
        print(f"Процесс B: закодированное сообщение - {encoded_message_with_time}")

        # Отправляем закодированное сообщение в главный процесс
        output_queue.put(encoded_message_with_time)


def main():
    """
    Главный процесс: отправляет сообщения в процесс A, получает закодированные
    сообщения от процесса B и выводит их в stdout с временной меткой.
    """
    # Создаем очереди для обмена данными
    queue_to_a = multiprocessing.Queue()
    queue_to_b = multiprocessing.Queue()
    queue_to_main = multiprocessing.Queue()

    # Создаем процессы A и B
    process_a_instance = multiprocessing.Process(target=process_a, args=(queue_to_a, queue_to_b))
    process_b_instance = multiprocessing.Process(target=process_b, args=(queue_to_b, queue_to_main))

    # Запускаем процессы
    process_a_instance.start()
    process_b_instance.start()

    try:
        while True:
            # Читаем сообщение из stdin
            user_input = input("Введите сообщение (или 'exit' для завершения): ")

            if user_input.lower() == 'exit':
                break

            # Добавляем временную метку
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message_with_time = f"[{timestamp}] {user_input}"

            # Отправляем сообщение в процесс A
            queue_to_a.put(message_with_time)

            # Проверяем, есть ли сообщения от процесса B
            if not queue_to_main.empty():
                encoded_message = queue_to_main.get()
                print(f"Главный процесс: полученное закодированное сообщение - {encoded_message}")

    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")

    finally:
        queue_to_a.put(None)
        queue_to_b.put(None)

        process_a_instance.join()
        process_b_instance.join()

        print("Все процессы завершены.")


if __name__ == "__main__":
    main()