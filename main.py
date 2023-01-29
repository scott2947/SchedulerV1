import sys

sys.path.insert(0, "./Specific/WelcomeMessage")
from welcomeMessage import WelcomeMessage

sys.path.insert(0, "./Specific/RootMenu")
from rootMenu import RootMenu

blockLength = WelcomeMessage()
RootMenu(blockLength)