# -*- coding: utf-8 -*-

from qt4a.andrcontrols import Window, Button, EditText
from qt4a.qpath import QPath
from panel.PopUpsPanel import ClosePopUps

class LoginPanel(Window):
    '''登录界面
    '''
    Activity = 'com.tencent.k12.kernel.login.activity.LoginActivity'  # 登录界面

    def __init__(self, app):
        self.app = app
        super(LoginPanel, self).__init__(app)
        self.update_locator({'密码登录': {'type': Button, 'root': self, 'locator': QPath('/Id="login_mobile_passward_text"')},
                            '登录即同意': {'type': Button, 'root': self, 'locator': QPath('/Id="icon_agree"')},
                            '手机号': {'type': EditText, 'root': self, 'locator': QPath('/Id="login_phone_edit_text"')},
                            '密码': {'type': EditText, 'root': self, 'locator': QPath('/Id="login_password_edit_text"')},
                            '登录': {'type': Button, 'root': self, 'locator': QPath('/Id="login_mobile_btn"')},
                      
                            })

    def appInit(self):
        closePopUps = ClosePopUps(self.app)
        closePopUps.agree_protocol()
        closePopUps.check_age()

    def login(self, acc, pwd):
        '''登录界面
        '''
        self.wait_for_exist()
        self.Controls["密码登录"].click()
        self.Controls["登录即同意"].click()
        self.Controls["手机号"].text = acc
        self.Controls["密码"].text = pwd
        self.Controls["登录"].click()



