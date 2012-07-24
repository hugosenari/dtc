from plugnplay import Interface

class MainLoop(Interface):
    '''
    Interface for mainloop
    looks like stater interface
    '''
    
    def run(self):
        '''
        Run your application
        '''
        pass

    def quit(self):
        '''
        Quit your mainloop
        '''
    
    @property
    def running(self):
        '''
        If your mainloop is running return True
        '''
        return False