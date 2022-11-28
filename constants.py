from src.config import CONFIG

"""
abstract methodu ile inputlar düzenlenecek.
https://www.sinanerdinc.com/python-abc-modulu-kullanimi
"""
#from abc import ABCMeta, abstractmethod

if CONFIG.TEST:
    class USERINFO:
        NAME = input("Lütfen isim soyad vererek giriş yapınız: ")
        DATE = input("Lütfen doğum tarihinizi giriniz (beklenen format GG.AA.YYYY): ")
        TIME = input("Lütfen doğum saatinizi giriniz: ")
        LOCATION = input("Lütfen doğduğunuz şehri giriniz: ")
        COUNTRYCODE = input("Lütfen doğduğunuz ülkenin kodunu giriniz(beklenen(Türkiye) TR): ")
        GENDER = input("Lütfen cinsiyetinizi giriniz(beklenen E/K): ")
else:
    class USERINFO:
        NAME = "Furkan Cetukkaya"
        DATE = "31.12.1993"
        TIME = "13.40"
        LOCATION = "istanbul"
        COUNTRYCODE = "TR"
        GENDER = "E"
