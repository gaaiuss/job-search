from selenium.webdriver.common.by import By

# Web scrap variables

# Login
EMAIL_FIELD = (By.XPATH, '//*[@id="session_key"]')
PASSWORD_FIELD = (By.XPATH, '//*[@id="session_password"]')
LOGIN_BTN = (
    By.XPATH,
    '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button',
)

# Job search
JOB_SEARCH_INPUT = (By.XPATH, '//*[@id="_r_3_"]')

# Filters
ALL_FILTERS = (By.XPATH, '//*[@id="JobsSearchFilters"]/nav/div/div/button/span')
SHOW_RESULTS = (By.XPATH, "/html/body/div[4]/div/div/div[2]/a/span")

## Date posted filter
DATE_POSTED = (
    By.XPATH,
    "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div/nav/div/div/div[2]/div/div/label",
)
PAST_24 = (
    By.XPATH,
    '//*[@id="auto-component-68cece49-be56-43ee-89ed-a59b91d6fa50"]/div/div[2]/div[2]/div[3]/div/div[2]/p/span',
)

# Apply BTN
APPLY = (
    By.XPATH,
    "/html/body/div[1]/div[1]/div[2]/div[2]/main/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/div[1]/a/span",
)
