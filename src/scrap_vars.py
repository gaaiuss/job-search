from selenium.webdriver.common.by import By

# Web scrap variables

# Login
EMAIL_FIELD = (By.XPATH, '//*[@id="_R_63pptiejj35656j6_"]')
PASSWORD_FIELD = (By.XPATH, '//*[@id="_R_lpptiejj35656j6_"]')
LOGIN_BTN = (
    By.XPATH,
    "/html/body/div[1]/div/div/div/div/main/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/button",
)

# Job search
JOB_TAB_BTN = (
    By.XPATH,
    "/html/body/div/div[1]/div[2]/div[1]/header/div/div/div/div[3]/div/div[2]/div/div/nav/ul/li[3]/a/span[1]/svg/path",
)
JOB_SEARCH_INPUT = (By.ID, "_r_e_")

# Filters
SHOW_RESULTS = (By.XPATH, "/html/body/div[4]/div/div/div[2]/a/span")

## Date posted filter
DATE_POSTED = (
    By.XPATH,
    "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div/nav/div/div/div[2]/div/div/label",
)
PAST_24 = (By.XPATH, "/html/body/div[4]/div/div/div[1]/div/div[3]/div/div[1]/label")

# Apply BTN
APPLY = (
    By.XPATH,
    "/html/body/div[1]/div[1]/div[2]/div[2]/main/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/div[1]/a/span",
)
