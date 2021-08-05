# -*- coding: utf-8 -*-

from demolib.demotestbase import DemoTestBase
from demolib.demoapp import DemoApp
from demolib.login import LoginPanel
from panel.GuidePanel import Guide

class HelloTest(DemoTestBase):
    '''示例登录测试用例
    '''
    owner = "Administrator"
    timeout = 5
    priority = DemoTestBase.EnumPriority.High
    status = DemoTestBase.EnumStatus.Ready
    
    def run_test(self):
        #--------------------------
        self.start_step('1、登录Android demo')
        #--------------------------
        acc = "17067989781"
        pwd = "fudao666"
        device = self.acquire_device()
        app = DemoApp(device)

        login = LoginPanel(app)
        #初始化
        login.appInit()

        #手机号登录
        login.login(acc, pwd)

        #选择年级
        #guide = Guide(app)
        #guide.click_grade()










        #print("current_activity: {}".format(app.device.current_activity))
        #self.wait_for_equal(self, "没有进入guide界面", app.device, 'current_activity', "com.tencent.k12.module.guide.GuideActivity", timeout=10, interval=0.5)

if __name__ == '__main__':
    HelloTest().debug_run()

