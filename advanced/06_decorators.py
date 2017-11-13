@positive_result
def discriminant(a, b, c):
    return (b**2) - 4*a*c


def positive_result(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        assert result >= 0, f.__name__ + '() result is not >= 0'
        return result

    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper

# Cleaner:
def positive_result(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        assert result >= 0, f.__name__ + '() result is not >= 0'
        return result
    return wrapper


@bounded(0, 100)
def percent(amount, total):
    return 100 * amount/total

def bounded(minimum, maximum):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if result < minimum:
                return minimum
            elif result > maximum:
                return maximum

            return result
        return wrapper
    return decorator


@logged
def discounted_price(price, percentage, make_int=False):
    result = price * ((100 - percentage) / 100)
    if not (0 < result <= price):
        raise ValueError('invalid_price')
    return result if not make_int else int(round(result))

# logs message to /tmp/logged.log every time called
# To set up the logging:

if __debug__:
    logger = logging.getLogger('Logger')
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(os.path.join(tempfile.gettempdir(),
                                               'logged.log'))
    logger.addHandler(handler)

    def logged(f):
        @functoole.wraps(f)
        def wrapper(*args, **kwargs):
            log = 'called:' + f.__name__  + '('
            log += ','.join(
                ['{0!r}'.format(a) for a in args] +
                ['{0!s}'='{1!r}'.format(k, v) for k, v in kwargs.items()])
            result = exception = None

            try:
                result = f(*args, **kwargs)
                return result
            except Exception as e:
                exception = e
            finally:
                log += ((') -> ' + str(result)) if exception is None
                        else '){0}: {1}'.format(type(exception), exception))
                logger.debug(log)

            if exception is not None:
                raise exception
        return wrapper
else:
    def logged(f):
        return f

    
            
