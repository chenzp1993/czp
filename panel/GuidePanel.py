# -*- coding: utf-8 -*-
from adapter import util
from adapter.OEDWindow import OEDXWindow
from testbase import logger

class Guide(OEDXWindow):
    """
    选择年级的引导页
    """
    Activity = 'com.tencent.k12.module.guide.GuideActivity'

    def __init__(self, k12app):
        super(Guide, self).__init__(k12app)
        locator = util.inflate(self, "GuidePanel.xml")
        self.updateLocator(locator)

    def click_grade(self, grade="初一"):
        self.wait_for_exist()
        try:
            logger.info("选择年级，点击初一")
            self.click_control(grade)
        except:
            logger.info("不需要选择年级")



