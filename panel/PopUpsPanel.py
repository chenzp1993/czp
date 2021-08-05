from qt4a.andrcontrols import Window, Button, EditText
from qt4a.qpath import QPath


class ClosePopUps(Window):

    Activity = 'com.tencent.k12.kernel.login.activity.SplashActivity'  # 登录界面

    def __init__(self, app):
        super(ClosePopUps, self).__init__(app)
        self.update_locator({'同意': {'type': EditText, 'root': self, 'locator': QPath('/Id="agreeTv"')},
                             '已满14岁': {'type': EditText, 'root': self, 'locator': QPath('/Id="dialog_right_btn"')},
                             '登录': {'type': Button, 'root': self, 'locator': QPath('/Id="btnLogin"')},
                             })

    def agree_protocol(self):

        self.wait_for_exist()
        try:
            self.Controls["同意"].click()
        except:
            pass

    def check_age(self):
        self.wait_for_exist()
        try:
            self.Controls["已满14岁"].click()
        except:
            pass