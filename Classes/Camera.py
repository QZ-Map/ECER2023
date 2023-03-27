class Camera:
    def __init__(self):
        pass
        
    def camera_open(self):
        """ Opens the default system camera for use at LOW_RES (160x120).
        Returns: 1 on success, 0 on failure  """
        return KIPR.camera_open()    
    
    def camera_close(self):
        """ Cleanup the current camera instance.  """
        KIPR.camera_close()
    
    def camera_open_black(self):
        """ Opens the default system camera for use at LOW_RES (160x120). This will improve frame rates for the black Logitech camera
        Returns: 1 on success, 0 on failure  """
        return KIPR.camera_open_black()
    
    def camera_open_at_res(self, res):
        """ Opens the default system camera for use at a given resolution.
            Parameters
                res	The resolution the camera should operate at. This can be:
                    LOW_RES (160x120)
                    MED_RES (320x240)
                    HIGH_RES (640x480)
            Warning: Only LOW_RES is currently supported. The function will fail for other resolutions. 
            Returns: 1 on success, 0 on failure  """
        return KIPR.camera_open_at_res(res)
    
    def camera_open_device(self, number, res):
        return KIPR.camera_open_device(number, res)
    
    def camera_open_device_model_at_res(self, number, model, res):
        return KIPR.camera_open_device_model_at_res(number, model, res)
    
    def camera_load_config(self, configName):
        """ Loads the config file specified by name. The system will look for the config in the base path.
        Parameters
            name	The configuration to load. Configuration file names are case sensitive.
        Do NOT include the config file extension ".conf" in the name parameter. 
        Returns: 1 on success, 0 on failure.  """
        return KIPR.camera_load_config(configName)
    
    def set_camera_width(self, width):
        KIPR.set_camera_width(width)
    
    def set_camera_height(self, height):
        KIPR.set_camera_height(height)
    
    def get_camera_width(self):
        return KIPR.get_camera_width()
    
    def get_camera_height(self):
        return KIPR.get_camera_height()
    
    def camera_update(self):
        """ Pulls a new image from the camera for processing.
        Returns: 1 on success, 0 on failure. """
        return KIPR.camera_update()
    
    def get_camera_pixel(self, p):
        """ Gets the color of a pixel.
        Parameters: p	The point at which the pixel lies.
        Returns: The rgb value of the pixel located at point p. 
        Note: A (r, g, b) value of (-1, -1, -1) will be returned for points that are out of range. """
        return KIPR.get_camera_pixel(p)
    
    def get_channel_count(self):
        """ Returns: Number of channels in the current configuration.  """
        return KIPR.get_channel_count()
    
    def get_object_count(self, channel):
        """ Parameters: channel	The channel to scan for objects.
        Note: Objects are sorted by area, largest first. 
        Returns: Number of objects in the given channel, -1 if channel doesn't exist.  """
        return KIPR.get_object_count(channel)
    
    def get_object_data(self, channel, object):
        """ Returns: The string data associated with a given object on a given channel. If there is no data associated, 0 is returned. 
        Note: 
            This data is not guaranteed to be null terminated. 
            This string pointer will be invalid after a call to camera_update()  """
        return KIPR.get_object_data(channel, object)
    
    def get_object_data_length(self, channel, object):
        return KIPR.get_object_data_length(channel, object)
    
    def get_object_confidence(self, channel, object):
        """ Returns: The confidence, between 0.0 and 1.0, that given object on the given channel is significant. If the channel or object doesn't exist, 0.0 is returned. """
        return KIPR.get_object_confidence(channel, object)
    
    def get_object_area(self, channel, object):
        """ Returns: The object's bounding box area. -1 is returned if the channel or object doesn't exist. """
        return KIPR.get_object_area(channel, object)
    
    def get_object_bbox(self, channel, object):
        return KIPR.get_object_bbox(channel, object)
    
    def get_object_centroid(self, channel, object):
        return KIPR.get_object_centroid(channel, object)
    
    def get_object_center(self, channel, object):
        """ Returns: The (x, y) center of the given object on the given channel. """
        return KIPR.get_object_center(channel, object)
    
    def set_camera_config_base_path(self, path):
        KIPR.set_camera_config_base_path(path)
    
    def get_camera_frame(self):
        """ Retrieves the current camera frame as a BGR (BGR888) array. The returned pointer is invalid after camera_update() is called again.
        Returns: the current BGR888 camera frame. """
        return KIPR.get_camera_frame()
    
    def get_camera_frame_row(self, row):
        """ Retrieves the current camera frame row as a BGR (BGR888) array. The returned pointer is invalid after camera_update() is called again.
        Returns: the current BGR888 camera frame row. """
        return KIPR.get_camera_frame_row(row)
