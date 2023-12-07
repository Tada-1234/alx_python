from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Function initiates and counts objects

        Args:
            self: Our Class
            width: the width of the rectangle
            height: height of the rectangle
            x: i dont know what this is
            y: i dont know what this is
            id: Number of Objects

        Returns:
            Nothing/error
        '''
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        '''
        Overrides __str__ method so that the print function prints something new

        Args:
            self: our class

        Returns:
            the new way of printing
        '''
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def area(self):
        '''
        Calculates the area of the Rectangle

        Args:
            self: Our class

        Returns:
            The area of the Rectangle
        '''
        return (self.__width * self.__height)
    
    def display(self):
        '''
        Prints Rectangle with #

        Args:
            self: Our class

        Returns:
            Nothing
        '''
        for n in range(self.__y):
            print()
        for n in range(self.__height):
            for m in range(self.__x):
                print(" ",end=(""))
            for m in range(self.__width):
                print("#", end=(""))
            print()
    
    def update(self, *args, **kwargs):
        '''
        This function updates the values of various attributes or leaves them as is if not updated

        Args:
            self: Our class
            *args: a variable number of arguments

        Returns:
            nothing
        '''
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, attr in zip(attributes, args): #zip attaches attribute names to corresponding args
                setattr(self, i, attr)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    @property
    def width(self):
        """
        function gets private/protected values

        Args:
            self: the class
        
        Returns:
            the private/protected value
        """
        return self.__width
    
    @property
    def height(self):
        """
        function gets private/protected values

        Args:
            self: the class
        
        Returns:
            the private/protected value
        """
        return self.__height
    
    @property
    def x(self):
        """
        function gets private/protected values

        Args:
            self: the class
        
        Returns:
            the private/protected value
        """
        return self.__x
    
    @property
    def y(self):
        """
        function gets private/protected values

        Args:
            self: the class
        
        Returns:
            the private/protected value
        """
        return self.__y
    
    @width.setter
    def width(self, width):
        """
        function sets private/protected values

        Args:
            self: the class
            width: width of the rectangle
        
        Returns:
            nothing
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """
        function sets private/protected values

        Args:
            self: the class
            height: the height of the rectangle
        
        Returns:
            nothing
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """
        function sets private/protected values

        Args:
            self: the class
            x: i still dont know
        
        Returns:
            nothing
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """
        function sets private/protected values

        Args:
            self: the class
            y: dont know
        
        Returns:
            nothing
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
