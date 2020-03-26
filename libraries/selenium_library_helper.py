import allure
from robot.libraries.BuiltIn import BuiltIn


class SeleniumLibraryHelper(object):
    """Сохранение скриншотов в отчет allure"""
    ROBOT_LIBRARY_SCOPE = "TEST SUITE"
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self

    def _start_suite(self, name, attrs):
        BuiltIn().set_library_search_order('foreign_library_helper')

    def capture_page_screenshot(self):
        helper_library = BuiltIn().get_library_instance('SeleniumLibrary')
        path = helper_library.capture_page_screenshot()
        allure.attach.file(path, name="screenshot", attachment_type=allure.attachment_type.PNG)
        return path


foreign_library_helper = SeleniumLibraryHelper
