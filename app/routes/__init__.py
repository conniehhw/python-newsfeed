from .home import bp as home
from .dashboard import bp as dashboard
# .home syntax directs the program to find the module called 'home' in the current directory
                                    # next, import the 'bp' object, but we rename it home as part of import process
                                    # now can import 'home' directly from the 'routes' package b/c __init__.py file imported & renamed the blue print
                                    
from .api import bp as api