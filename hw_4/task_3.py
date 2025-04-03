import multiprocessing
import threading
import time
import codecs
from datetime import datetime


def process_a(input_queue, output_queue):
    
    while True:
        
        message = input_queue.get()
        if message is None:  
            break

        
        processed_message = message.lower()

        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        processed_message_with_time = f"[{timestamp}] {processed_message}"

        output_queue.put(processed_message_with_time)

        time.sleep(5)


def process_b(input_queue, output_queue):
    while True:

        message = input_queue.get()
        if message is None:  
            break

        rot13_message = codecs.encode(message, 'rot_13')

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        encoded_message_with_time = f"[{timestamp}] {rot13_message}"

        print(f"Процесс B: закодированное сообщение - {encoded_message_with_time}")

        output_queue.put(encoded_message_with_time)


def main():
    queue_to_a = multiprocessing.Queue()
    queue_to_b = multiprocessing.Queue()
    queue_to_main = multiprocessing.Queue()

    process_a_instance = multiprocessing.Process(target=process_a, args=(queue_to_a, queue_to_b))
    process_b_instance = multiprocessing.Process(target=process_b, args=(queue_to_b, queue_to_main))

    process_a_instance.start()
    process_b_instance.start()

    try:
        while True:
            user_input = input("Введите сообщение (или 'exit' для завершения): ")

            if user_input.lower() == 'exit':
                break

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message_with_time = f"[{timestamp}] {user_input}"

            queue_to_a.put(message_with_time)

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