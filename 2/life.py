                        # LIVES

import arcade

class Life ( arcade.Sprite ) :

    def __init__ ( self , x ) :
        super().__init__ ( "2\image heart.png" )
        self.width = 22
        self.height = 22
        self.center_x = x
        self.center_y = 20

# resources:images/space_shooter/playerLife1_orange.png