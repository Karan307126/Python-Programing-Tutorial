class Remote:
    def isRightpressed(self):
        pass
    def isLeftpressed(self):
        pass
    def isToppressed(self):
        pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass

remote1=Remote()
player1=Player()
if(remote1.isLeftpressed()):
    player1.moveLeft()