import abc

# abc --abstract base class
# abc.ABC --> Abstract base class
# @abc.abstractmethod --> when we need to make a method abstract


class Car(abc.ABC):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

# --------------------------------------

class HondaCity(Car):
    def start(self):
        print("Start of Honda City")

    def stop(self):
            print("Stop of Honda City")


h=HondaCity()