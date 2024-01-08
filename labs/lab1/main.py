def gamer_type(hours_played):
    """ 
    This simple program calculates what kind of gamer are you based on 
    the number of hours of game you have played.  

    input: number of hours played
    
    output: a label for the kind of gamer
    
    Modify the following so that the cutoff for "pro" is anything > 90 hours
    and instead of "newbie", return "novice"
    """
    
    if hours_played < 100:
        return "newbie"
    else:
        return "pro"

