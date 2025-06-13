# 5 nested function logger

# logger with nonlocal scope

def create_logger():
    log = []
    def add_log(message):
        nonlocal log
        log.append(message)
        return log
    return add_log

logger = create_logger()
logger("Error occurred")
print(logger("Info logged"))

# ['Error occurred', 'Info logged']
# uses nonlocal to maintain a log list, useful for debugging web apps.