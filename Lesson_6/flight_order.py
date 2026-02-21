import time


class TestFlightOrder:

    def test_flight_order(self,setup_playwright):

        page = setup_playwright
        page.goto("https://demo.guru99.com/test/newtours/reservation.php")
        new_radio = page.get_by_role("radio", name="tripType", value="oneway")
        new_radio.click()




    #     drop_down = page.locator("[id='s0-1-20-4[0]-7[3]-_sacat']")
    #     time.sleep(3)
    #     drop_down.select_option("Art")
    #     drop_down.select_option(index=2)
    #     print ("Test end")
    #
    # def test_ebay_checkbox_example(self,setup_playwright):
    #     page = setup_playwright
    #     page.goto("https://www.ebay.com/")
    #     adv = page.get_by_role("link", name="Advanced")
    #     adv.click()
    #
    #     sold_checkbox = page.locator("[name='LH_Sold']")
    #     sold_checkbox.click()
    #     new_radio = page.get_by_role("radio", name="New")
    #     new_radio.click()
        print ("Test end")