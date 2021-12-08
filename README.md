# **Turkish**
## FinDjango, Django Web Framework ile hazirlanan finans uygulamasidir.
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
- Heroku, static dosyalari barindirmadigi icin profil fotograflari gorunmemekte.
- Uygulamaya dair bir cok gelistirme yapilabilir...

# English
## FinDjango is a finance application built with Django Web Framework.
### Live App
[**FinDjango**](https://findjango.herokuapp.com) - Live version deployed to Heroku.

## About the App
#### What's FinDjango?
While currencies gain or lose value against each other, the investor wants to protect the value of the money in his hand. As a result, he knows which unit will gain or maintain its value against which unit, and he wants to invest in that unit. The well-known consultants at **FinDjango** also advise investors. The investor, with the advice he receives, keeps his investment in the units mentioned by the consultant until the specified date. When the target date comes, the investor makes the sale to the specified target unit. The consultant is not responsible for any loss/gain in value after the target date, the target date is important.

#### How does it work?
The registered user logs in to the site. By selecting the desired package from the **Get Token** tab, he comes to the payment page. He makes the payment using the Braintree infrastructure offered by Paypal, and if the payment is successful, the token is loaded into his account.

#### Getting advice:
It selects the most recent advices from the **Latest Advices** section on the homepage, and one of the most purchased advices from the **Popular Advices** section. Click the **Buy this advice** button to buy the advice. Sees the analysis of the advice and in which units it is.

#### Giving advice:
The consultant creates an investment advice (Create Advice):
- Base Currency (unit to hold money)
- Target Currency (the unit in which the money will be sold)
- Description (short information is given, no information about units. It is intended to sell the advice.)
- Analysis (analysis of the advice to the investor who received the advice)
- Target Date (the date the money will be sold, the investor keeps his money in the specified unit until this date)
- Token (the consultant determines the amount of tokens for his advice)

Every day at 15:05 UTC, the results are announced and listed under the **Result** tab. Under the **Profile** tab, the user can see the advices he has received or given. The advices that other users have given or have given before can be accessed by pressing the user name.
Profile settings or password changes can be made by clicking **Settings** under the user button at the top right.

## About the project
#### How was it created?
- PostgreSQL was used as database.
- The User model is built on a more customizable user model derived from the AbstractBaseUser class instead of Django's default user model.
- Payment processes are integrated via Braintree (paypal).
- Rate information is updated via the [Frankfurter](https://www.frankfurter.app/) API. API information is obtained from the European Central Bank and is updated daily at 15:00 UTC. After 5 minutes, FinDjango is updated. During the update, advice dated that day are calculated with the current exchange rate and displayed in the Result tab.
- In order for the demo site not to be empty, 10 new advices are created after each update. Advices excluding 10 advices passed to the Result and 10 newly created advices are automatically deleted. (*investment/task_result.py*)
- [htmx](https://htmx.org/) is used instead of jquery to make AJAX calls in the frontend.
- And many more features were used...


#### What's missing? What features can be improved?
Since FinDjango is an **example** project, it is not a comprehensive application.
- Since it is mostly used for backend purposes, not much attention has been paid to the frontend part. Bootstrap was used and it was not focused on responsive design.
- It may be unnecessary or insufficient to build on the value between two currencies. In addition, cryptocurrencies and stock market materials can be integrated into the system and developed.
- Database setups and query performances can/should be improved.
- Function Based Views can be reconfigured as Class Based Views.
- Profile photos are not visible because Heroku does not host static files.
- Many improvements can be made on the application...
