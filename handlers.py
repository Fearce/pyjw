import threading

import test
import settings
from helpers import log


def start_stop():
    #log("Pressed button")
    if settings.enabled:
        log("Bot disabled")
        change_var('start_stop_string', "Enable bot")
        settings.enabled = False
    else:
        log("Bot enabled")
        change_var('start_stop_string', "Disable bot")
        settings.enabled = True
        threading.stack_size(200000000)
        thread = threading.Thread(target=test.program)
        thread.start()


def change_var(var_name, new_string):
    var = settings.app.builder.get_variable(var_name)
    var.set(new_string)