import time
from selenium import webdriver
from login import ClickupLogin
from scrapy_xlsx import ScrapyXlsx


if __name__ == '__main__':
    # Instancie o driver uma única vez na main
    driver = webdriver.Edge()

    # Define edge_options
    edge_options = webdriver.EdgeOptions()

    # Defina o diretório de download
    prefs = {"download.default_directory" : r"data\clickup_sheet_negocios"}
    edge_options.add_experimental_option("prefs", prefs)
    
    # Defina a resolução do navegador para 800x600
    driver.set_window_size(1300, 900)

    # Instancie a classe ClickupLoginScrapy, passando o driver instanciado
    credentials = ClickupLogin(driver, 'vinicius.reis@tahto.com.br', '1a2b3c4dT!')
    scrapy = ScrapyXlsx(driver)
    # Execute o login
    credentials.login()
    time.sleep(4)
    scrapy.go_to_extract()
    time.sleep(4)
    # Verifique a presença do elemento
    print(
        credentials.check_element(
            '//*[@id="app-root"]/cu-app-shell/cu-manager/div[1]/div/div/main/cu-dashboard/div/cu-views-bar-container/cu2-views-bar/cu-location-header-lazy-wrapper/cu-location-header/div/div[2]/cu-automation-button/span/button/cu-automation-count-label'
        )
    )

    # Aguarde um tempo suficiente antes de fechar o navegador
    time.sleep(200)  # 10 segundos de espera

    # Feche o navegador
    driver.quit()
