from .core import Context

class Strategy( object ):

    def __init__( self, **params ):
        self.init_context( params )
    
    def init_context( self, **params ):
        context = Context()
        context.add_params( **params )
        self.context = context
        return context
        
    def before_trading( self ):
        pass

    def after_trading( self ):
        pass
        
    def init_trading( self ):
        pass
        
    def handle_bar( self, bar ):
        pass
        
    def run( self ):
        pass
        
    