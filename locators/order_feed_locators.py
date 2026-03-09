from selenium.webdriver.common.by import By


class OrderFeedLocators:
    
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p") #счетчик «Выполнено за всё время» 
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p") #счетчик «Выполнено за сегодня»
    ORDERS_IN_PROGRESS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul") # Раздел "В работе"
    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul/li") # Номер заказа в разделе "В работе"
