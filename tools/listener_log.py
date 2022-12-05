"""" Settings for collecting browser logs """

import logging
from selenium.webdriver.support.events import AbstractEventListener


class LogListener(AbstractEventListener):
    """ Settings for collecting browser logs """

    def __init__(self, request):
        logging.basicConfig(filename=request.config.getoption("--log_file"),
                            level=request.config.getoption("--log_level"))

    def after_navigate_to(self, url: str, driver):
        logging.info('Driver navigate to %s', url)

    def after_find(self, by, value, driver):
        logging.info('Driver found %s with %s', value, by)

    def after_click(self, element, driver):
        logging.info('Driver clicked on %s', element)

    def after_execute_script(self, script, driver):
        logging.info('Driver executed %s', script)

    def on_exception(self, exception, driver):
        logging.info('Exception: %s', exception)
        driver.get_screnshot_as_file(f'logs/{exception}.png')
