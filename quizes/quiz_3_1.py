class Circular_Shape_3D:

    def __init__(self, radius=0):
        self.radius = radius
    
    def getRadius(self): return self.radius
    def setRadius(self, radius): self.radius = radius

    def print(self):
        print("Usr radius is:", self.radius)


class Cylinder(Circular_Shape_3D):

    def __init__(self, radius=0, height=0):
        Circular_Shape_3D.__init__(self, radius)
        self.height = height
    
    def getHeight(self): return self.height
    def setHeight(self): self.height = height

    def compute_s_area(self, height, radius):
        surface_area = (2 * 3.14 * radius * height) + (2 * 3.14 * radius * radius)
        return surface_area
    
    def compute_volume(self, radius, height):
        volume = (3.14 * radius * radius * height)
        return volume

    def print(self):
        print('The surface area of the cylinder is:', compute_s_area(self.height, self.radius))
        print('The surface area of the cylinder is:', compute_volume(self.height, self.raduius))
    

class Sphere(Circular_Shape_3D):
    def __init__(self, radius=0):
        Circular_Shape_3D.__init__(self, radius)
        
    def getRadius(self): return self.radius
    def setRadius(self): self.radius = radius

    def compute_s_area(self, radius):
        surface_area = (4 * 3.14 * radius * radius)
        return surface_area

    def volume(self, radius):
        volume = ((4/3) * 3.14 * radius * radius * radius)
        return volume
        def print(self):
            print('The volume of the sphere is:', compute_s_area(self.radius))
            print('The area of the spere is:', compute_volume(self.radius))
