import os
from datetime import datetime



def take_screenshot(driver):
    folder = "screenshots"
    os.makedirs(folder,exist_ok=True)
    file_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
    path = os.path.join(folder,file_name)
    driver.save_screenshot(path)

    return path