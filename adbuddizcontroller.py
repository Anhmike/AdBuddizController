# -*- coding: utf-8 -*-

# AdBuddizController library for managing
# AdBuddiz Android advertisements inside Kivy apps
# by rafalo1333

# Pyjnius autoclass and JavaException modules import

try:
    from jnius import autoclass
except:
    print 'Error in importing proper modules'

# Accessing Kivy's PythonActivity and AdBuddiz classes

try:
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    AdBuddiz = autoclass('com.purplebrain.adbuddiz.sdk.AdBuddiz')
    AdBuddizLogLevel =  autoclass('com.purplebrain.adbuddiz.sdk.AdBuddizLogLevel')
except:
    print 'AdBuddizController ERROR. Error in accessing proper Java classes.'
    
# Main AdBuddizController class defining SDK control methods

class AdBuddizController(object):
    
    def __init__(self, publisher_key, **kwargs):
        # AdBuddizController instance initialisation
        # You need to pass your PUBLISHER_KEY as argument
        super(AdBuddizController, self).__init__(**kwargs)
        self.initialise(publisher_key)
        
    def initialise(self, publisher_key):
        # AdBuddiz initialisation with the given PUBLISHER_KEY
        # and caching ads for display
        try:
            AdBuddiz.setPublisherKey(publisher_key)
            AdBuddiz.cacheAds(PythonActivity.mActivity)
        except:
            print 'AdBuddizController ERROR. Error in initialising AdBuddiz SDK.'
            
    def is_ready(self):
        # Method that checks if AdBuddiz SDK is ready to show advertisements
        try:
            if AdBuddiz.isReadyToShowAd(PythonActivity.mActivity):
                return True
            else:
                return False
        except:
            print 'AdBuddizController ERROR. Error in accessing AdBuddiz class. SDK is not ready.'
            return False
    
    def show_ad(self):
        # Method that shows the advertisement
        try:
            if self.is_ready():
                AdBuddiz.showAd(PythonActivity.mActivity)
                AdBuddiz.cacheAds(PythonActivity.mActivity)
        except:
            print 'AdBuddizController ERROR. Error in showing AdBuddiz advertisement'
            
    def set_testmode(self):
        # Method for setting the TEST mode for AdBuddiz SDK
        # Use it only for testing, remove from your App before publishing!
        try:
            AdBuddiz.setTestModeActive()
        except:
            print 'AdBuddizController ERROR. Error in setting TEST_MODE on.'
            
    def set_loglevel(self, level):
        # Method for setting logging level for AdBuddiz SDK
        # You can pass one of the following options: info, error or silent (no logs in console)
        try:
            if level.lower() == 'info':
                AdBuddiz.setLogLevel(AdBuddizLogLevel.Info)
            elif level.lower() == 'error':
                AdBuddiz.setLogLevel(AdBuddizLogLevel.Error)
            elif level.lower() == 'silent':
                AdBuddiz.setLogLevel(AdBuddizLogLevel.Silent)
            else:
                print 'AdBuddizController: you should pass one of the three arguments: info, error or silent!'
        except:
            print 'AdBuddizController ERROR. Error in setting proper LOG_LEVEL.'
