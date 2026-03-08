from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    BUTTON_COSTRUCTOR_LOCATOR = (By.CLASS_NAME, 'AppHeader_header__linkText__3q_va') #кнопка конструктор
    BUTTON_ORDER_FEED_LOCATOR = (By.CSS_SELECTOR, 'a.AppHeader_header__link__3D_hX[href="/feed"]') #кнопка лента заказов
    CROSS_INGREDIENT_DETAILS_LOCATOR = (By.CSS_SELECTOR, '.Modal_modal__close__TnseK') #крестик в окне детали ингредиента
    COUNTER_INGREDIENT_LOCATOR = (By.CSS_SELECTOR, '.counter_counter__num__3nue1') #счетчик ингредиента
    BASKET_LOCATOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]") #корзина
    
    INGREDIENT_COUNTER = (By.XPATH, ".//ancestor::a//p[contains(@class, 'counter_counter__num')]") # Локатор для контейнера с ингредиентами (для ожидания загрузки)
    # Локатор для модального окна (нужен для wait_modal_window и is_modal_open)
    INGREDIENT_DETAILS_LOCATOR = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
    # Название ингредиента в модальном окне
    INGREDIENT_NAME_IN_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]//p[contains(@class, 'text_type_main-medium')]")

    #локаторы для ингредиентов
    BUN_FLUORESCENT_LOCATOR = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']") #булка флюоресцентная
    BUN_CRATOR_LOCATOR = (By.XPATH, "//p[text()='Краторная булка N-200i']") #булка краторная 

    SPICY_SAUCE_LOCATOR = (By.XPATH, "//p[text()='Соус Spicy-X']") #соус спайси
    SIGNATURE_SAUCE_LOCATOR = (By.XPATH, "//p[text()='Соус фирменный Space Sauce']") #соус фирменный
    GALACTIK_SAUCE_LOCATOR = (By.XPATH, "//p[text()='Соус традиционный галактический']") #соус галактический
    SPIKED_SAUCE_LOCATOR = (By.XPATH, "//p[text()='Соус с шипами Антарианского плоскоходца']") #соус с шипами

    SHELLFISH_MEAT_LOCATOR = (By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']") #Мясо моллюсков
    BEEF_METEORITE_LOCATOR = (By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']") #Говяжий метеорит
    BIO_CUTLET_LOCATOR = (By.XPATH, "//p[text()='Биокотлета из марсианской Магнолии']") #Биокотлета
    FILLET_LOCATOR = (By.XPATH, "//p[text()='Филе Люминесцентного тетраодонтимформа']") #Филе
    MINERAL_RINGS_LOCATOR = (By.XPATH, "//p[text()='Хрустящие минеральные кольца']") #минеральные кольца
    FRUITS_OF_THE_TREE_LOCATOR = (By.XPATH, "//p[text()='Плоды Фалленианского дерева']") #Плоды
    CRYSTALS_LOCATOR = (By.XPATH, "//p[text()='Кристаллы марсианских альфа-сахаридов']") #Кристаллы
    MINI_SALAD_LOCATOR = (By.XPATH, "//p[text()='Мини-салат Экзо-Плантаго']") #Мини-салат
    CHEESE_LOCATOR = (By.XPATH, "//p[text()='Сыр с астероидной плесенью']") #сыр

    INGREDIENT_DATA = [
        (BUN_FLUORESCENT_LOCATOR, "Флюоресцентная булка R2-D3"),
        (BUN_CRATOR_LOCATOR, "Краторная булка N-200i"),
        (SPICY_SAUCE_LOCATOR, "Соус Spicy-X"),
        (SIGNATURE_SAUCE_LOCATOR,"Соус фирменный Space Sauce"),
        (GALACTIK_SAUCE_LOCATOR, "Соус традиционный галактический"),
        (SPIKED_SAUCE_LOCATOR, "Соус с шипами Антарианского плоскоходца"),
        (SHELLFISH_MEAT_LOCATOR, "Мясо бессмертных моллюсков Protostomia"),
        (BEEF_METEORITE_LOCATOR, "Говяжий метеорит (отбивная)"),
        (BIO_CUTLET_LOCATOR, "Биокотлета из марсианской Магнолии"),
        (FILLET_LOCATOR, "Филе Люминесцентного тетраодонтимформа"),
        (MINERAL_RINGS_LOCATOR, "Хрустящие минеральные кольца"),
        (FRUITS_OF_THE_TREE_LOCATOR, "Плоды Фалленианского дерева"),
        (CRYSTALS_LOCATOR, "Кристаллы марсианских альфа-сахаридов"),
        (MINI_SALAD_LOCATOR, "Мини-салат Экзо-Плантаго"),
        (CHEESE_LOCATOR, "Сыр с астероидной плесенью")
    ]

    INGREDIENT_WITH_INCREMENT = [
        (BUN_FLUORESCENT_LOCATOR, 2),
        (BUN_CRATOR_LOCATOR, 2),
        (SPICY_SAUCE_LOCATOR, 1),
        (SIGNATURE_SAUCE_LOCATOR, 1),
        (GALACTIK_SAUCE_LOCATOR, 1),
        (SPIKED_SAUCE_LOCATOR, 1),
        (SHELLFISH_MEAT_LOCATOR, 1),
        (BEEF_METEORITE_LOCATOR, 1),
        (BIO_CUTLET_LOCATOR, 1),
        (FILLET_LOCATOR, 1),
        (MINERAL_RINGS_LOCATOR, 1),
        (FRUITS_OF_THE_TREE_LOCATOR, 1),
        (MINI_SALAD_LOCATOR, 1),
    ]