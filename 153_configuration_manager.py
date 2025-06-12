# 2 configuration manager

CONFIG = {"env":"dev"}
def set_config(key, value):
    global CONFIG
    CONFIG[key] = value
def get_config(key):
    return CONFIG.get(key, "Not Found")

set_config("env", "prod")
print(get_config("env")) # prod

# manages global configuration settings, like a flask app's settings

