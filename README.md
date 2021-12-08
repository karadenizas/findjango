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
#### Nasil olusturuldu?
- Database olarak PostgreSQL kullanildi.
- User modeli, Django'nun default user modeli yerine AbstractBaseUser sinifindan turetilmis daha kisisellestirilebilir bir user modeli uzerinden kurgulandi. 
- Payment processleri Braintree (paypal) uzerinden entegre edildi.
- Kur bilgileri [Frankfurter](https://www.frankfurter.app/) API uzerinden guncel olarak alinmaktadir. API bilgileri Avrupa Merkez Bankasindan alinmakta olup her gun UTC 15:00'da guncellenmektedir. Bundan 5 dakika sonra da FinDjango guncellenmektedir. Guncelleme esnasinda o gun tarihli tavsiyeler guncel kurla hesaplanip Result sekmesinde gosterilir. 
- Demo sitenin bos kalmamasi icin her gun guncellemeden sonra 10 yeni tavsiye olusturulur. Result'a gecen 10 tavsiye ve yeni olusturulan 10 tavsiye haricindeki tavsiyeler otomatik olarak silinir.  (*investment/task_result.py*)
- Frontend kisminda AJAX call yapabilmek icin jquery yerine [htmx](https://htmx.org/) kullanildi.
- Ve daha bir cok ozellik kullanildi...


#### Neler eksik? Hangi ozellikleri gelistirilebilir?
FinDjango **ornek** bir proje oldugu icin haliyle kapsamli bir uygulama degildir. 
- Daha cok backend amacli calisildigi icin, frontend kismina fazla ozen gosterilmedi. Bootstrap kullanildi ve responsive tasarim odakli calisilmadi.
- Iki para birimi arasindaki deger uzerinden kurgulanmasi gereksiz veya yetersiz olabilir. Bununla beraber kripto paralar ve borsa materyalleri sisteme entegre edilebilir, gelistirilebilir.
- Database kurgulari ve query performanslari gelistirilebilir/gelistirilmeli.
- Function Based Viewlar, Class Based View olarak yeniden kurgulanabilir.
- Uygulamaya dair bir cok gelistirme yapilabilir...
