class Context( object ):

    def __setattr__( self, name, value ):
        object.__setattr__( self, name, value )

    def __getattr__( self, name ):
        try:
            return object.__getattribute__( name )
        except:
            return None
    
    def add_params( self, **params ):
        if not params:
            return self
            
        for key in params:
            setattr( self, key, params[ key ] )
            
        
        
        
    