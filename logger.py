from datetime import datetime

current_date = datetime.now()
timestamp_format = '%Y-%m-%d %H:%M:%S'


def log_message(message: str) -> str:
    '''
        Returns a formatted message accompanying it with when that message
        was created
    '''
    message_to_log = current_date.strftime(
        timestamp_format) + "," + message + '\n'
    try:
        with open("log.txt", "a") as logger_file:
            logger_file.write(message_to_log)
    except IOError as error:
        print(error)


if __name__ == "__main__":

    print(log_message("How are you?"))
    print(log_message("Looks nice"))
