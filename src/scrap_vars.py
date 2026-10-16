from selenium.webdriver.common.by import By

# Web scrap variables

# Login
EMAIL_FIELD = (By.XPATH, '//*[@id="session_key"]')
PASSWORD_FIELD = (By.XPATH, '//*[@id="session_password"]')
LOGIN_BTN = (By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')

# Captcha
CAPTCHA = (By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')

# Job search
JOB_SEARCH_INPUT = (By.XPATH, '//*[@id="_r_3_"]')

## Filters
ALL_FILTERS = (By.XPATH, '//*[@id="JobsSearchFilters"]/nav/div/div/button/span')
SHOW_RESULTS = (By.XPATH, "//span[normalize-space()='Show results']")

## Date posted filter
DATE_POSTED = (
    By.XPATH,
    '//*[@id="JobsSearchFilters"]/nav/div/div/div[2]/div/div/label',
)
PAST_24 = (By.XPATH, "//span[normalize-space()='Past 24 hours']")

# Job element pattern
JOB_ELEMENT = (By.ID, "company-accent-4")

# Apply button
APPLY = (
    By.XPATH,
    '//*[@id="workspace"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/div[1]/a',
)
