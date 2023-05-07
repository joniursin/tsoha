# Ravintolasovellus

Sovelluksella voidaan, tarkastella ravintoloita ja niiden arvosteluita. Sovellusta voidaan käyttää joko normaalina käyttäjänä tai ylläpitäjänä.

- Sovelluksella näkee tietoja ravintoloista ja niihin jätetyistä arvosteluista.
- Sovellukseen pystyy luomaan tunnuksen.
- Kirjautuminen mahdollistaa omien arvosteluiden jättämisen.
- Arvostelussa on mahdollista antaa arvosana (1-5) ja jättää kommentti.
- Arvosteluissa myös näkyy milloin ne on julkaistu.
- Muiden arvosteluista voidaan tykätä, jolloin ne nousevat ylemmäksi.
- Sovelluksessa on myös ylläpitäjä rooli, jolla voidaan poistaa epäsopivia arvosteluja.
- Ylläpitäjä myös pitää huolen uusien ravintoloiden lisää- ja poistamisesta.

# Lopullinen tilanne

### Kirjautuminen

- Sovellukseen voidaan luoda tunnus, jonka avulla siihen voidaan kirjautua sisään
- On myös mahdollista kirjautua ylläpitäjä käyttäjällä, joka mahdollistaa enemmän ominaisuuksia kuin perus käyttäjällä

### Käyttäminen (perus käyttäjä)

- Käyttäjä näkee kaikki tietokantaa lisätyt ravintolat ja voi antaa niille joko arvostelun tai katsoa kaikki ravintolan arvostelut
- Käyttäjä voi tykätä jokaisesta arvostelusta kerran, jolloin se nousee tykkäysten perusteella ylemmäksi
- Käyttäjä voi myös poistaa tykkäyksensä
- Käyttäjä voi myös katsoa ylläpitäjän tekemiä ravintola ryhmiä ja katsoa mitkä ravintolat niihin kuuluu

### Ylläpitäjä oiminaisuudet

- Ylläpitäjä voi lisätä sovelluksesta uusia ravintoloita, sekä tehdä näistä ryhmiä
- Ylläpitäjä voi poistaa ravintoloita, jolloin ne eivät näe sovelluksessa.
- Ylläpitä voi poistaa epäsopivia arvosteluita

# Käynnistysohjeet

## Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

```bash
DATABASE_URL=tietokannan-paikallinen-osoite
```

```bash
SECRET_KEY=salainen-avain
```

## Aktivoi seuraavaksi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komeinnoilla:

```bash
$ python3 -m venv venv
```

```bash
$ source venv/bin/activate
```

```bash
$ pip install -r ./requirements.txt
```

## Määritä tietokannan skeema komenolla:

```bash
$ psql < schema.sql
```

## Sovelluksen saa käynnistetty komennolla:

```bash
$ flask run
```

# Testaaminen

Ylläpitäjä roolia voidaan testata käyttäen seuraavia tunnuksia

Käyttäjänimi: admin

Salasana: admin
