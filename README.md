# FinDjango, Django Web Framework ile hazirlanan finans projesidir.
### Canli Uygulama
[**FinDjango**](https://findjango.herokuapp.com) - Heroku'ya deploy edilmis canli versiyonu.

## Hakkinda
#### Nedir?
Para birimleri birbirleri karisinda deger kazanir veya kaybederken yatirimci, elindeki paranin degerini korumak ister. Bunun sonucunda hangi birimin hangi birime karsi deger kazanacagi veya degerini koruyacagini bilip yatirimini o birime yapmak ister. **FinDjango**'daki un yapmis danismanlar da yatirimcilara tavsiyelerde bulunurlar. Yatirimci, aldigi tavsiye ile yatirimini belirtilen tarihe kadar danismanin soyledigi birimlerde tutar. Hedef tarih gelince yatirimci belirtilen hedef birime satisini yapar. Danisman hedef tarihten sonra olusan deger kaybi/kazanimi karsisinda sorumlu degildir, hedef tarih onemlidir.

### Nasil calisir?
Danisman bir yatirim tavsiyesi olusturur (Create Advice):
- Base Currency (paranin tutulacagi birim)
- Target Currency (paranin satilacagi birim)
- Description (kisa bilgi verilir, birimler hakkinda bilgi verilmez. tavsiyeyi satmak amaclanir.)
- Analysis (tavsiyeyi alan yatirimciya, tavsiye hakkinda yapilan analiz)
- Target Date (paranin satilacagi tarih, yatirimci bu tarihe kadar belirtilen birimde parasini tutar)
- Token (danisman, verdigi tavsiye icin token miktari belirler)

Her kullanici tavsiye alip verebilir. Get Token sekmesinden bir plan secilir ve odeme yapilir. 
