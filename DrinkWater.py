import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify (
            title = "PLEASE DRINK WATER",
            message = "Its been an hour",
            app_icon = r"C:\Users\Ananth\Pictures\Camera Roll\arrays\recursion\icon.ico",
            timeout = 3
    )   
        time.sleep(60*60)