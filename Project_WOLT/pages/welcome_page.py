class WelcomePage():

    def __init__(self, page):
        self.page = page

    #def close_pop_up(self):



    def search_for_item(self,item:str):
        search_menu= self.page.locator("[id='_R_tdj_']")
        search_menu.click()
        search_menu.fill(item)
        #search_menu.click()
        self.page.keyboard.press("Enter")







        print ("asasas")






