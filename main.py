
class Transport:
    def __init__(self, tezlik, yonilg_iqt):
        # tezlik = km/h
        # yonilg_iqt = 100 km ga sarf (litrlarda)
        self.tezlik = tezlik
        self.yonilg_iqt = yonilg_iqt

 
    def tezlik_oshirish(self):
        raise NotImplementedError()

    def yoqilgi_sarfi(self, masofa):
        """
        masofa (km)
        yonilg_iqt = L/100km
        natija: sarflangan yoqilg'i miqdori
        """
        return (masofa / 100) * self.yonilg_iqt

    def sayohat_masofa(self, masofa):
        vaqt = masofa / self.tezlik        
        yoqilgi = self.yoqilgi_sarfi(masofa)
        return {
            "vaqt_soat": vaqt,
            "yoqilgi_litr": yoqilgi
        }


    def yuk_kotarish(self, yuk):
        return 0   



class Avtobus(Transport):
    def tezlik_oshirish(self):
        self.tezlik += 5
        return self.tezlik

    def yoqilgi_sarfi(self, masofa):
        return super().yoqilgi_sarfi(masofa)


class YukMashinasi(Transport):
    def tezlik_oshirish(self):
        self.tezlik += 3
        return self.tezlik

    def yoqilgi_sarfi(self, masofa):
        return super().yoqilgi_sarfi(masofa) * 1.3

    def yuk_kotarish(self, yuk):
        maksimal = 10_000  
        if yuk > maksimal:
            return f"Yuk og‘ir: maksimal {maksimal} kg!"
        return f"{yuk} kg yuk qabul qilindi."


class SportAvto(Transport):
    def tezlik_oshirish(self):
        self.tezlik += 15
        return self.tezlik

    def yoqilgi_sarfi(self, masofa):
        return super().yoqilgi_sarfi(masofa) * 1.2



park = [
    Avtobus(tezlik=80, yonilg_iqt=25),
    YukMashinasi(tezlik=70, yonilg_iqt=30),
    SportAvto(tezlik=150, yonilg_iqt=15)
]

masofa = 200 

for t in park:
    natija = t.sayohat_masofa(masofa)
    print(t.__class__.__name__, natija)


print(park[1].yuk_kotarish(6000))     
print(park[0].yuk_kotarish(6000))     
print(park[2].yuk_kotarish(6000))     

