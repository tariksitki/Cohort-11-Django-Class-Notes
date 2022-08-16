
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("--------------------------------------")
# def print_types(data):
#     for i in data:
#         print(i, type(i))

# test = [122, "victor", [1,2,3], (1,2,3), {1,2,3}, True, lambda x:x]

# print_types(test)


# class Person:
#     name = "victor"
#     age = 32


# person1 = Person()
# person2 = Person()

# print(person1.name)

# Person.job = "Fullstack developer"

# print(person2.job)
# classta yapılan değişiklikler o classtan üretilen instancelara da aktarılır.

#! class attributes vs instance attributes


# class Person:
#     name = "victor"
#     age = 32

# person1 = Person()
# person2 = Person()

# person1.location = "Turkey"
# print(person2.locaiton)
# bir instance a eklenen attribute diğerlerini değiştirmez
# person2.age = 18
# print(person2.age)
# print(person1.age)
#? İlk önce instance'a bakıyor. Orada yoksa class'a gidip bakıyor 👆

# class Person:
#     company = "clarusway"

#     def test(self):
#         print("test")

#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

#     @staticmethod
#     def salute():
#         print("Hi there!")


# person1 = Person()
# person2 = Person()

# person1.test()
# Person.test(person1)  python arkada bu şekle dönüştürüyor ve o yüzden üstteki çalışmıyor.(arguman gönderdin diyor) def tanımlamasına self ekleyerek sorunu çözebiliriz.
# person1.set_details("victor", 30)
# person1.get_details()

# person1.salute()

# #! special methods (init, str)

# class Person:
#     company = "clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

#     def __str__(self):    #  print(person1) yaparsak ve str yoksa bize adresini ve nereden türedildiğini döndürür ama str varsa buradakileri döndürür. arka planda print(person1.__str__) çalışıyor.
#         return f"{self.name} - {self.age}"

# person1 = Person("victor", 32)   # init methodu sayesinde arguman gönderip direk oluşturabiliriz.
# # person1.get_details()

# person2 = Person("selcuk", 22)
# # person2.get_details()
# print(person1)

# OOP Principies (4 pillars)

#* encapsulation => izinsiz girişleri ve değiştirmeleri engelleme (python da tam olarak uygulaması yoktur.)
#* abstraction   => kullanıcın bilmesinin gerek olmayanını gizleme
#* polymorhism   => overwriting = parent'tan gelen yapı ihtiyacımızı tam karşılamıyorsa update edebilmemiz.
# overloading = parent'tan gelen yapıyı farklı parametrelerle değiştirebilmemiz. veya methodu birden farklı tanımlayabilmemizdir. Verilen parametlere göre kendisi seçerek kullanır.
#* inheritance   => kalıtım. Parent'tan chield'a aktarılması


#? encapsulation and abstraction
# class Person:
#     company = "clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000   # bunu değiştirirsen sıkıntı çıkar dyoruz ama değiştirilebilir.
#         self.__id = 3000
#     def __str__(self):
#         return f"{self.name} - {self.age}"

#     def get_details(self):
#         print(self.name, self.age)

# person1 = Person("henry", 18)
# person1._id = 4000   # ulaşıp değiştirebildik
# print(person1._id)
# # print(person1.__id)   # çift çizgi olunca ulaşamıyoruz bu şekilde.
# print(person1._Person__id)  # bu şekilde ulaşabiliyoruz.
# person1._Person__id = 4000
# print(person1._Person__id)  # bu şekilde de değiştirebiliriz.


#? inheritance and polymorphism

class Person:
    company = "clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def get_details(self):
        print(self.name, self.age)


class Lang:
    def __init__(self, langs):
        self.langs = langs

    def display_langs(self):
        print(self.langs)

# birden fazla class'tan inheritance üretebiliriz.


class Employee(Person, Lang):
    def __init__(self, name, age, path, langs):
        # self.name = name   # böyle elle de yazabiliriz veya super ile alabiliriz.
        # self.age = age
        # super ilk sıraya yazılı olan Person'u tanımlıyor.
        super().__init__(name, age)
        # self.langs = langs
        self.path = path
        # super kullanamadığımız için bu şekilde yazmamız gerekiyor.
        Lang.__init__(self, langs)

    def get_details(self):    # overwrite yapmış olduk...
        print(self.name, self.age, self.path, self.langs)
        # super().get_details()  # parent'taki özellikleri de kullanmaya bu şekilde devam edebiliriz.
        # print(self.path)


emp1 = Employee("vic", 32, "FS", ["python", "JS"])
# print(emp1)
# Person class'ın daki method'ların ve atribute'ların hepsini Employee classında inherit alarak kullanmış olduk.
emp1.get_details()
emp1.display_langs()   # Lang classından miras aldı...


#? inner class

# from django.db import models

# class Article(models.Model):
#     name = models.CharField(max_length=50)
#     author = models.CharField(max_length=50)

#     class Meta:    # standart isim bu şekilde değişmez. Classın ayarlarını yapmış olduk. ordering ile isme göre sırala dedik...
#         ordering = ["name"]


# Output : [<class '__main__.Employee'>, <class '__main__.Person'>, <class '__main__.Lang'>, <class 'object'>]
print(Employee.mro())
# nereden geldi üredi ...

print(help(Employee))   # Output : class'ın herşeyini veriyor.


print("--------------------------------------")
