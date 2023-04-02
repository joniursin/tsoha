# tsoha
Ravintolasovellus

Sovelluksella voidaan, joko etsiä hakusanalla tai tarkastella kartasta lähellä olevia ravintoloita ja niiden arvosteluita. Sovellusta voidaan käyttää joko normaalina käyttäjänä tai ylläpitäjänä.

- Sovelluksella näkee tietoja ravintoloista ja niihin jätetyistä arvosteluista.
- Sovellukseen pystyy luomaan tunnuksen.
- Kirjautuminen mahdollistaa omien arvosteluiden jättämisen.
- Arvostelussa on mahdollista antaa arvosana (1-5) ja jättää kommentti.
- Arvosteluissa myös näkyy milloin ne on julkaistu.
- Muiden arvosteluista voidaan tykätä, jolloin ne nousevat ylemmäksi.
- Sovelluksessa on myös ylläpitäjä rooli, jolla voidaan poistaa epäsopivia arvosteluja.
- Ylläpitäjä myös pitää huolen uusien ravintoloiden lisää- ja poistamisesta.

# Käynnistysohjeet

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>

Aktivoi seuraavaksi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komeinnoilla:

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt

Määritä tietokannan skeema komenolla:

$ psql < schema.sql

Sovelluksen saa käynnistetty komennolla:

$ flask run
