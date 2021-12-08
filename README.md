# FinDjango, Django Web Framework ile hazirlanan finans projesidir.
### Canli Uygulama
[**FinDjango**](https://findjango.herokuapp.com) - Heroku'ya deploy edilmis canli versiyonu.

## Uygulama Hakkinda
#### Nedir?
Para birimleri birbirleri karisinda deger kazanir veya kaybederken yatirimci, elindeki paranin degerini korumak ister. Bunun sonucunda hangi birimin hangi birime karsi deger kazanacagi veya degerini koruyacagini bilip yatirimini o birime yapmak ister. **FinDjango**'daki un yapmis danismanlar da yatirimcilara tavsiyelerde bulunurlar. Yatirimci, aldigi tavsiye ile yatirimini belirtilen tarihe kadar danismanin soyledigi birimlerde tutar. Hedef tarih gelince yatirimci belirtilen hedef birime satisini yapar. Danisman hedef tarihten sonra olusan deger kaybi/kazanimi karsisinda sorumlu degildir, hedef tarih onemlidir.

#### Nasil calisir?
Uye olan kullanici siteye giris yapar. **Get Token** sekmesinden istedigi paketi secerek odeme sayfasina gelir. Paypal'in sundugu Braintree altyapisini kullanarak odemesini yapar ve odeme basarili olursa token hesabina yuklenir.

#### Tavsiye alma:
Anasayfada gordugu **Latest Advices** kismindan en son tavsiyeleri, **Popular Advices** kismindan en cok satin alinan tavsiyelerden birini secer. **Buy this advice** butonuna basarak tavsiyeyi satin alir. Tavsiyenin analizini ve hangi birimlerde oldugunu gorur.

#### Tavsiye verme:
Danisman bir yatirim tavsiyesi olusturur (Create Advice):
- Base Currency (paranin tutulacagi birim)
- Target Currency (paranin satilacagi birim)
- Description (kisa bilgi verilir, birimler hakkinda bilgi verilmez. tavsiyeyi satmak amaclanir.)
- Analysis (tavsiyeyi alan yatirimciya, tavsiye hakkinda yapilan analiz)
- Target Date (paranin satilacagi tarih, yatirimci bu tarihe kadar belirtilen birimde parasini tutar)
- Token (danisman, verdigi tavsiye icin token miktari belirler)

Her gun UTC 15:05'de sonuclar aciklanir ve **Result** sekmesi altinda listelenir. **Profile** sekmesi altinda kullanici aldigi veya verdigi tavsiyeleri gorebilir. Diger kullanicilarin da verdigi veya daha once verdigi tavsiyelerine kullanici ismine basarak ulasilabilir. 
Sag ustteki kullanici butonu altinda **Settings**'e basilarak profil ayarlari veya parola degisikligi islemleri yapilabilir.

## Proje Hakkinda



#### Neler eksik?
FinDjango **ornek** bir proje oldugu icin haliyle kapsamli bir uygulama degildir. 
