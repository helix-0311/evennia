"""
Contains commands for managing script parents.
"""
from src import scripthandler

def clear_cached_scripts(command):
    """
    Show the currently cached scripts.
    """
    session = command.session
    cache_dict = scripthandler.CACHED_SCRIPTS
    cache_size = len(cache_dict)
    cache_dict.clear()
    session.msg("Script parent cached cleared (%d previously in cache)." % 
                                                                cache_size)
    
def show_cached_scripts(command):
    """
    Clears the cached scripts by deleting their keys from the script cache
    dictionary. The next time an object needs the previously loaded scripts,
    they are loaded again.
    """
    session = command.session
    cache_dict = scripthandler.CACHED_SCRIPTS
    
    retval = "Currently Cached Script Parents\n"
    retval += "-" * 78
    for script in cache_dict.keys():
        retval += "\n " + script
    retval += "\n" + "-" * 78 + "\n"
    retval += "%d cached parents." % len(cache_dict)
    session.msg(retval)
    
def cmd_parent(command):
    """
    Figure out what form of the command the user is using and branch off
    accordingly.
    """
    if "showcache" in command.command_switches:
        show_cached_scripts(command)
        return
    
    if "clearcache" in command.command_switches:
        clear_cached_scripts(command)
        return