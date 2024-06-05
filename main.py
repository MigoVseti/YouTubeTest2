import time
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 7',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

            # ТЕСТ 1

    def testOne_shorts(self) -> None:
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Shorts")
        el3.click()

            # ТЕСТ 2

    def testTwo_navigation_to_trending(self) -> None:

        el5 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Explore Menu")
        el5.click()
        el6 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Trending")
        el6.click()

            # ТЕСТ 3

    def testThree_subscribe(self) -> None:
        el7 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().className(\"android.widget.ImageView\").instance(7)")
        el7.click()
        el8 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Subscribe to Ben Azelart.")
        el8.click()

            # ТЕСТ 4

    def testFour_view_description(self) -> None:
        el9 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().className(\"android.widget.ImageView\").instance(5)")
        el9.click()
        el10 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.view.ViewGroup\").instance(16)")
        el10.click()

            # ТЕСТ 5

    def test_search(self) -> None:
        el11 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el11.click()
        el12 = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.youtube:id/search_edit_text")
        el12.send_keys("hekko")
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(405, 252)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

if __name__ == '__main__':
    unittest.main()
