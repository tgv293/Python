# class Personal:
#     def __init__(self, name, age):
#         self.Name = name
#         self.Age = age
#         self.__Salary = None

#     def PrintInfo(self):
#         print(
#             "Name: {}, Age: {}, Salary: {}".format(self.Name, self.Age, self.__Salary)
#         )


# if __name__ == "__main__":
#     person1 = Personal("Nguyễn Văn Khánh Hòa", 21)
#     person1.PrintInfo()
#     print(person1.Name)
#     print(person1._Personal__Salary)


class Laptop:
    def __init__(self, model):
        self.Model = model
        self.Bat = self.Battery("LG", "BTR1234", "5000mAh")

    def PrintInfo(self):
        print(self.Model)
        self.Bat.PrintInfo()

    # Define the Battery class outside the Laptop class
    class Battery:
        def __init__(self, mnf, model, capacity):
            self.Manufacturer = mnf
            self.Model = model
            self.Capacity = capacity

        def PrintInfo(self):
            print(
                "Manufacturer: {}, Model: {}, Capacity: {}".format(
                    self.Manufacturer, self.Model, self.Capacity
                )
            )


if __name__ == "__main__":
    lap1 = Laptop("DELL")
    lap1.PrintInfo()
