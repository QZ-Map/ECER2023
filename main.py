def setup():
    # starts shutdown timer
    # calibrations???
    wait4light()
    KIPR.shut_down_in(180)
    return

def wait4light():
    """ only continuies when starting light has been aktivated
    """
    port = 7 ## random port
    KIPR.wait_for_light(port)
    # light = False #check 4 lght pls
    # while not light:
    #     light = False
    # return

setup()
