def cal(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        logger.exception("Division by zero is not possible")
    else:
        return result