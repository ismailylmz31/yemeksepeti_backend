Yemeksepeti Benzeri Web Uygulaması Backend Dokümantasyonu
Giriş
Bu proje, Yemeksepeti benzeri bir yemek siparişi uygulaması için geliştirilmiş bir backend API'sidir.
Django Rest Framework ve SQLite kullanılarak geliştirilmiştir. Bu dokümantasyon, 
projenin nasıl çalıştığını ve API endpointlerinin nasıl kullanılacağını açıklamaktadır.

Kurulum
Gereksinimler
Python 3.6+
Django 3.2+
Django Rest Framework 3.12+
Kurulum Adımları
Proje dosyalarını klonlayın:   
git clone https://github.com/username/yemeksepeti_backend.git
cd yemeksepeti_backend


Sanal ortam oluşturun ve bağımlılıkları yükleyin:
python -m venv venv
source  venv\Scripts\activate
pip install -r requirements.txt


Veritabanını migrate edin:
python manage.py migrate


Süper kullanıcı oluşturun:
python manage.py createsuperuser


Sunucuyu başlatın:
python manage.py runserver


Kullanıcı Yönetimi
Kullanıcı Kayıt
Endpoint: POST api/users/register/

Request Body:
json
{
    "username": "string",
    "email": "string",
    "password": "string"
}

Response:
json

{
    "id": "integer",
    "username": "string",
    "email": "string"
}




Kullanıcı Girişi
Endpoint: POST api/users/login/
Request Body:
json
{
    "username": "string",
    "password": "string"
}
Response:

json
{
    "token": "string"
}




Kullanıcı Profili
Endpoint: GET api/profiles/

Authorization: Token <token>
Response:

json
{
    "id": "integer",
    "username": "string",
    "email": "string"
}




Restoran Yönetimi
Restoran Listesi ve Ekleme
Endpoint: GET api/restaurants/
Authorization: Token <token>

Response:
json
[
    {
        "id": "integer",
        "name": "string",
        "address": "string",
        "description": "string",
        "rating": "decimal"
    }
]

Endpoint: POST api/restaurants/
Authorization: Token <token>
Request Body:

json
{
    "name": "string",
    "address": "string",
    "description": "string",
    "rating": "decimal"
}

Response:
json
{
    "id": "integer",
    "name": "string",
    "address": "string",
    "description": "string",
    "rating": "decimal"
}



Restoran Detayı, Güncelleme ve Silme
Endpoint: GET /restaurants/<id>/
Authorization: Token <token>
Response:

json
{
    "id": "integer",
    "name": "string",
    "address": "string",
    "description": "string",
    "rating": "decimal"
}


Endpoint: PUT api/restaurants/<id>/
Authorization: Token <token>
Request Body:

json
Kodu kopyala
{
    "name": "string",
    "address": "string",
    "description": "string",
    "rating": "decimal"
}


Response:
json
{
    "id": "integer",
    "name": "string",
    "address": "string",
    "description": "string",
    "rating": "decimal"
}




Endpoint: DELETE api/restaurants/<id>/
Authorization: Token <token>
Response:
204 No Content




Ürün ve Kategori Yönetimi
Kategori Listesi ve Ekleme
Endpoint: GET api/products/categories/

Authorization: Token <token>
Response:

json
[
    {
        "id": "integer",
        "name": "string"
    }
]





Endpoint: POST api/products/categories/
Authorization: Token <token>
Request Body:
json

{
    "name": "string"
}


Response:
json
{
    "id": "integer",
    "name": "string"
}



Kategori Detayı, Güncelleme ve Silme
Endpoint: GET api/products/categories/<id>/
Authorization: Token <token>
Response:
json

{
    "id": "integer",
    "name": "string"
}


Endpoint: PUT api/products/categories/<id>/
Authorization: Token <token>
Request Body:
json
{
    "name": "string"
}


Response:
json
{
    "id": "integer",
    "name": "string"
}



Endpoint: DELETE api/products/categories/<id>/
Authorization: Token <token>
Response:
204 No Content




Ürün Listesi ve Ekleme
Endpoint: GET /products/
Authorization: Token <token>
Response:
json
[
    {
        "id": "integer",
        "restaurant": "integer",
        "category": "integer",
        "name": "string",
        "description": "string",
        "price": "decimal"
    }
]




Endpoint: POST /products/
Authorization: Token <token>
Request Body:
json
{
    "restaurant": "integer",
    "category": "integer",
    "name": "string",
    "description": "string",
    "price": "decimal"
}


Response:
json
{
    "id": "integer",
    "restaurant": "integer",
    "category": "integer",
    "name": "string",
    "description": "string",
    "price": "decimal"
}





Ürün Detayı, Güncelleme ve Silme
Endpoint: GET api/products/<id>/
Authorization: Token <token>
Response:
json
{
    "id": "integer",
    "restaurant": "integer",
    "category": "integer",
    "name": "string",
    "description": "string",
    "price": "decimal"
}




Endpoint: PUT api/products/<id>/
Authorization: Token <token>
Request Body:
json
{
    "restaurant": "integer",
    "category": "integer",
    "name": "string",
    "description": "string",
    "price": "decimal"
}


Response:
json
{
    "id": "integer",
    "restaurant": "integer",
    "category": "integer",
    "name": "string",
    "description": "string",
    "price": "decimal"
}




Endpoint: DELETE api/products/<id>/
Authorization: Token <token>
Response:
204 No Content





Sipariş Yönetimi
Sipariş Listesi ve Ekleme
Endpoint: GET /orders/
Authorization: Token <token>

Response:
json
[
    {
        "id": "integer",
        "user": "integer",
        "restaurant": "integer",
        "status": "string",
        "total_price": "decimal",
        "created_at": "datetime"
    }
]




Endpoint: POST api/orders/
Authorization: Token <token>
Request Body:
json
{
    "restaurant": "integer",
    "status": "string",
    "total_price": "decimal"
}


Response:
json
{
    "id": "integer",
    "user": "integer",
    "restaurant": "integer",
    "status": "string",
    "total_price": "decimal",
    "created_at": "datetime"
}






Sipariş Detayı, Güncelleme ve Silme
Endpoint: GET api/orders/<id>/
Authorization: Token <token>

Response:
json
{
    "id": "integer",
    "user": "integer",
    "restaurant": "integer",
    "status": "string",
    "total_price": "decimal",
    "created_at": "datetime"
}





Endpoint: PUT api/orders/<id>/
Authorization: Token <token>
Request Body:
json
{
    "restaurant": "integer",
    "status": "string",
    "total_price": "decimal"
}


Response:
json
{
    "id": "integer",
    "user": "integer",
    "restaurant": "integer",
    "status": "string",
    "total_price": "decimal",
    "created_at": "datetime"
}




Endpoint: DELETE api/orders/<id>/
Authorization: Token <token>
Response:
204 No Content








Yorum ve Değerlendirme
Yorum Listesi ve Ekleme
Endpoint: GET /reviews/
Authorization: Token <token>
Response:
json
[
    {
        "id": "integer",
        "restaurant": "integer",
        "user": "integer",
        "rating": "integer",
        "comment": "string",
        "created_at": "datetime"
    }
]



Endpoint: POST  api/reviews/
Authorization: Token <token>
Request Body:
json
{
    "restaurant": "integer",
    "rating": "integer",
    "comment": "string"
}


Response:
json
{
    "id": "integer",
    "restaurant": "integer",
    "user": "integer",
    "rating": "integer",
    "comment": "string",
    "created_at": "datetime"
}





Yorum Detayı, Güncelleme ve Silme
Endpoint: GET api/reviews/<id>/
Authorization: Token <token>
Response:
json
{
    "id": "integer",
    "restaurant": "integer",
    "user": "integer",
    "rating": "integer",
    "comment": "string",
    "created_at": "datetime"
}




Endpoint: PUT api/reviews/<id>/
Authorization: Token <token>
Request Body:
json
{
    "restaurant": "integer",
    "rating": "integer",
    "comment": "string"
}

Response:
json
{
    "id": "integer",
    "restaurant": "integer",
    "user": "integer",
    "rating": "integer",
    "comment": "string",
    "created_at": "datetime"
}







Endpoint: DELETE api/reviews/<id>/
Authorization: Token <token>
Response:
204 No Content






Arama ve Filtreleme
Restoran Arama ve Filtreleme
Endpoint: GET api/restaurants/
Authorization: Token <token>

Query Params:
search: Restoran adı, adresi veya açıklaması ile arama
ordering: Restoran adı veya derecesine göre sıralama (örn: name, rating)

Response:
json
[
    {
        "id": "integer",
        "name": "string",
        "address": "string",
        "description": "string",
        "rating": "decimal"
    }
]




Ürün Arama ve Filtreleme
Endpoint: GET  api/products/
Authorization: Token <token>

Query Params:
search: Ürün adı, açıklaması veya kategori adı ile arama
ordering: Ürün adı veya fiyatına göre sıralama (örn: name, price)

Response:
json
[
    {
        "id": "integer",
        "restaurant": "integer",
        "category": "integer",
        "name": "string",
        "description": "string",
        "price": "decimal"
    }
]



EK OLARAK:
Restorana ait ürünleri görmek için:

api/menus/restaurant/(restoran id)

api/products/restaurant/(restoran id)



Restorana ait yorumları göörmek için:

api/reviews/restaurant/(restoran id)



Restorana ait kampanyalar için:

api/restaurants/offer/(restoran id)


Proje içerikleri:
-Restoran
-kampanyalar
-yorumlar
-profil oluşturma
-kategori
-ürünler
-sipariş
-menü oluşturma

Detaylı ilişkiler için superuser oluşturup admin panelinden denetimleri yapabilirsiniz.
İncelediğiniz için teşekkür ediyorum. uygulamaya ait bazı postman ve admin ekran görüntülerine aşağıdaki fotoğraflardan erişebilirsiniz.





![admin panel](https://github.com/user-attachments/assets/6d2a081d-67bd-4176-b2b8-4c3b4cc0a303)
![yorumlar](https://github.com/user-attachments/assets/2932ce46-6d89-4403-b44a-f35deac55195)
![ürünler2](https://github.com/user-attachments/assets/cd421da9-37e2-4163-93a0-a591d4ca3a26)
![ürünler](https://github.com/user-attachments/assets/391a1586-6a9c-494d-9db6-3cfed6f7a1aa)
![siparişler](https://github.com/user-attachments/assets/b60e1780-72a4-400d-bf2e-2f2bb38f4492)
![restoranlar](https://github.com/user-attachments/assets/4cb62422-7754-44a0-aaa2-f3d6072c43bb)
![restoranaaitmenüler](https://github.com/user-attachments/assets/261e52b6-1723-4112-999c-15fc61bfa302)
![restaurants](https://github.com/user-attachments/assets/f8f17947-ec61-4381-b145-496e81944418)
![order-orderitem](https://github.com/user-attachments/assets/72126344-b0e9-4781-9aad-2821eb231c5a)
![orderitem](https://github.com/user-attachments/assets/bc21cb31-3490-4fa5-a1c9-7e9338153eac)
![order status](https://github.com/user-attachments/assets/4b0bd7a0-f80f-48f5-8377-1e6ce99bd2e2)
![offer](https://github.com/user-attachments/assets/349f2931-415e-497b-9ccf-a6d161ca232a)
![menü-menüitem](https://github.com/user-attachments/assets/17d9d337-2575-43ca-b7c7-fe5a3bb317ca)
![menüler](https://github.com/user-attachments/assets/1397ef66-ae9d-4591-bfbf-f4ac6bb0cf50)






