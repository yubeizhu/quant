class Position( object ):
    
    def __init__( self, open = True, type = 0, value = None ):
        self.open = open
        self.type = type
        self.value = value
            
    def is_open( self ):
        return self.open
    
    def is_short( self ):
        return True self.type == 0 else False
        
    def is_long( self ):
        return True self.type == 1 else False

    
        
        