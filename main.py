#proje dosyasında istenildiği gibi bu aşama da gerekli kitaplıkları içeri aktardım
import csv
import datetime

#farklı kaynaklardan'da teyit ederek menü.txt', aşağıda ki gibi oluşturdum.

menu = open("Menu.txt", "w")
menu.write("Lütfen bir pizza tabanı Seçiniz:\n")
menu.write("1: Klasik\n")
menu.write("2: Margarita\n")
menu.write("3: Türk Pizzası\n")
menu.write("4: Sade Pizza\n")
menu.write("Seçebileceğiniz Soslar:\n")
menu.write("11: Zeytin\n")
menu.write("12: Mantarlar\n")
menu.write("13: Keçi Peyniri\n")
menu.write("14: Et\n")
menu.write("15: Soğan\n")
menu.write("16: Mısır\n")
menu.close()

#'pizza' üst sınıfını aşağıda ki gibi oluşturdum 
class pizza:
    def __init__(self, desciption, cost):
        self.description = desciption
        self.cost = cost

    def get_description(self):
        return self.description
    def get_cost(self):
        return self.cost

 #"Pizza" Alt sınıfı aşağıda ki gibi oluşturdum

class klasik_pizza(pizza):
        def __init__(self):
             super().__init__("Klasik Pizza", 30)

class margarita_pizza(pizza):
     def __init__(self) :
          super().__init__("Margarita Pizza", 60)

class Turk_pizza(pizza):
     def __init__(self):
          super().__init__("Türk Pizza", 90)

class sade_pizza(pizza):
     def __init__(self):
          super().__init__("Sade Piiza", 8)

#"Decarator" Üstü Sınıf örnekten yola çıkarak oluşturdum
class Decorator(pizza):
     def __init__(self, component):
          self.component = component

     def get_cost(self):
            return self.component.get_cost() + self.cost

     def get_description(self):
        return self.component.get_description() + ' ' + self.description

#sosları belirlemek için aşağıda ki kodları kullandım

class zeytin(Decorator):
      def __init__(self, component):
            super().__init__(component)
            self.desciption = "Zeytin"
            self.cost = 2

class mantar(Decorator):
      def __init__(self, component):
            super().__init__(component)
            self.description = "Mantarlar"
            self.cost = 3

class keci_peyniri(Decorator):
      def __init__(self, component):
            super().__init__(component)
            self.description = " Keçi Peyniri"
            self.cost = 4
class et(Decorator):
      def __init__(self, component):
            super().__init__(component)
            self.description = "Et"
class sogan(Decorator):
      def __init__(self, component):
            super().__init__(component)
            self.description = "Soğan"
class misir(Decorator):
      def __init__(self, component):
            super().__init__(component)
            self.description =" Mısır"

 #istenilen main fonksiyonunu oluşturdum

def main():
          #menüyü ekrana yazdırdım
          with open("Menu.txt", "r") as menu:
                print(menu.read())

          #Menüden müşteririden pizza ve sosu seçmesi istedim:
          #Müşteriden veri alacağım için input kullandım, girilen her bilgiyide int tipinde olmasını belirledim
          pizza_sec = int(input("Lütfen bir pizza seçiniz: "))
          sos_sec = int(input("Lütfen bir sos seçin: "))

          #Pizza seçimini oluşturmak için aşağıda ki koşulları kullandım

          if pizza_sec == 1:
                pizza = klasik_pizza()
          elif pizza_sec == 2:
               pizza = margarita_pizza()
          elif pizza_sec == 3:
                pizza = Turk_pizza()
          elif pizza_sec == 4:
               pizza == sade_pizza()
          else:
                print("Geçersiz Pizza Seçtiniz!")
                return
          #sos seçimini oluşturmak için aşağıda ki koşulları kullandım
          if sos_sec == 11:
                sos = zeytin(pizza)
          elif sos_sec == 12:
                sos = mantar(pizza)
          elif sos_sec == 13:
                sos = keci_peyniri(pizza)
          elif sos_sec == 14:
                sos = et(pizza)
          elif sos_sec == 15:
                sos = sogan(pizza)
          elif sos_sec == 16:
                sos = misir(pizza)
          else:
                print("Geçersiz Sos Seçtiniz!")
                return 

          #seçimler sonrası toplam fiyatın hesaplanması
          toplam_fiyat = sos.get_cost()
          print("Toplam Fiyat: ", toplam_fiyat)  

          #Müşterilerden kendi bilgilerini girmelerini istedim
          isim = input(" Lütfen İsminizi girin: ")
          soyisim = input("Lütfen Soyisminizi girin: ")
          tc_kimlik_no = input("Lütfen TC Kimlik Numaranızı girin: ")
          kredi_kart_no =input("Lütfen Kredi Kartı numaranızı girin: ")
          kredi_kart_sifre = input("Lütfen Kredi Kartı Şifrenizi girin: ")
          print("Siparişiniz alınmıştır. En Kısa Sürede Teslim Edilecektir! Afiyet Olsun:)") 

          #siparişlerin istenilen şekilde veritanbanına eklenmesini sağladım
          # tüm veriler sorunsuz şekilde Orders_Database.csv dosyasına kayıt edilmektedir
          with open ("Orders_Database.csv", "a", newline='') as database:
               writer = csv.writer(database)
               writer.writerow([isim, soyisim, tc_kimlik_no, kredi_kart_no, kredi_kart_sifre,
                    sos.get_description(), toplam_fiyat , datetime.datetime.now(), kredi_kart_sifre])
if __name__ == "__main__":
      main()       