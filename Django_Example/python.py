class Car:
    def __init__(self):
        self._color = ""
        self._model = ""

    def drive(self):
        print("Bruuuuuuu")

    @property
    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    @property
    def getModel(self):
        return self.model

    def setmodel(self, model):
        self.model = model

    def showDetail(self):
        print("This is %s color %s" % (self.model, self.color))


def main():
    bmw = Car()
    bmw.setColor("red")
    bmw.setmodel("X4")
    bmw.drive()
    bmw.showDetail()


main()
