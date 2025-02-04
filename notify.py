import time
from plyer import notification

if __name__=="__main__":
    for i in range(4):
            notification.notify(
                title = "Follow",
                message="Hit the follow button 👍" ,
                app_name = "gitHub",
                app_icon = "[copy path of icon- github.ico]",
            
                timeout=2
            )
