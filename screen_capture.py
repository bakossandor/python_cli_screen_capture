import click
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--kiosk")
DRIVER = 'C:\PROJECTS\chromedriver\chromedriver'
driver = webdriver.Chrome(DRIVER, chrome_options=chrome_options)


def screen_it(website):
    driver.get(f'https://{website}')
    screenshot = driver.save_screenshot('./screenshots/my_screenshot.png')
    driver.quit()
    return True

@click.command()
@click.argument("website")
def cli(website):
    """
    This CLI python program, named 'screen capture', do perfectly screenshots on different sites. \n
    It uses the selenium chrome webdriver - so it is requirement to have the chrome webdriver and the chrome installed to the computer \n
    Before you use this make sure if the webdriver is configured to the right path. Search for the <DRIVER> variable. \n
    The program require one argument: - The searched website. \n
    After activating the virtualenv and installing the package - you can us the following command \n
    > screen www.google.com || screen google.com \n
    It saves the pictures to a predefined library

    """
    click.echo(f"The screenshot saved about the {website}") if screen_it(website) else click.echo(f"failed to make a screenshot about {website}")