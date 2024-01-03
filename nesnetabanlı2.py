class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def bilgi_ver(self):
        return f"{self.isim}, {self.yas} yaşındadır."


hayvan1 = Hayvan("Kedi", 3)
print(hayvan1.bilgi_ver())
