class ColorPicker:

  def __init__(self, primary_color, *args, **kwargs): # **kwargs makes a dictionary of arguments, *args is a list of arguments
    self.primary_color = primary_color
    for key, value in kwargs.items():
      setattr(self, key + "_color", value)

  def get_colors(self):
    # loops over a dictionary  of key/value pairs made on the fly if the string 'color' is in the key
    return {k: v for k, v in self.__dict__.items() if 'color' in k}
    