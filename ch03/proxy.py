from selenium import webdriver
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.http', 'proxy_url')
profile.set_preference('network.proxy.http_port', 3128)
profile.set_preference('network.proxy.ssl', 'proxy_url')
profile.set_preference('network.proxy.ssl_port', 3128)
profile.update_preferences()
driver = webdriver.Firefox(profile)