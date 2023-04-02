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

# Nykyinen tilanne

- Sovellukseen pystyy luomaan tilin ja siten kirjautua sisään
- Sovellus tarkistaa ovatko kirjautumistiedot oikeat
- Sovelluksessa voidaan nähdä sinne valmiiksi laitetetut ravintolat (ei voida vielä lisätä sovelluksen avulla)
- Näille ravintoloille voidaan joko jättää käyttäjällä arvostelu tai katsoa muiden arvosteluja
- Arvostelu tallentaa käyttäjän nimien, arvion (1-5), tekstin sekä julkaisu kohdan tietokantaan
- Sovelluksesta voidaan kirjautua ulos
# Käynnistysohjeet

## Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

DATABASE_URL=tietokannan-paikallinen-osoite
  
SECRET_KEY=salainen-avain

## Aktivoi seuraavaksi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komeinnoilla:

$ python3 -m venv venv
  
$ source venv/bin/activate
  
$ pip install -r ./requirements.txt

## Määritä tietokannan skeema komenolla:

$ psql < schema.sql

## Sovelluksen saa käynnistetty komennolla:

$ flask run
