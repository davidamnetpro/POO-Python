from car import Car
from account import Account
from payment import Payment
from route import Route

if __name__ == "__main__":
    #Utilizando clase car
    #Dato 1
    car = Car()
    car.license = "AMS234"
    car.driver = "Andres Herrera"
    print(vars(car))
    #Dato 2
    car2 = Car()
    car2.license = "QWE567"
    car2.driver = "Matha"
    print(vars(car2))

    #Utilizando clase account
    #Dato1
    Conductor1 = Account()
    Conductor1.id = 1015434879
    Conductor1.document = "CC"
    Conductor1.name = "Jose Gonzales"
    Conductor1.password == "123jgonzales"
    print(vars(Conductor1))

    #Utilizando clase payment
    #Dato1
    pago1 = Payment()
    pago1.id = 486840646452 
    print(vars(pago1))

    #Utilizando clase route
    #Dato1
    ruta1 = Route()
    ruta1.id = 1
    ruta1.start = "Prados del sur"
    ruta1.id = "Sauces"
    print(vars(ruta1))