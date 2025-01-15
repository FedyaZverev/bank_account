from functools import wraps


def log(filename=None):
    """
    log, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs: {tuple(args)}, {kwargs}"
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_message + "\n")
                return error_message

        return wrapper

    return my_decorator


@log()
def my_function(x, y):
    return x + y


print(my_function(2, 2))
