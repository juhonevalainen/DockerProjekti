# DockerProjekti
### Tietoa
Pilvipalvelut -kurssin tehtävä.

Projektin sisältö on jaettu kahteen osaan, mitkä ovat etusivu eli frontend, sekä palvelin eli backend. Kummastakin etusivusta ja palvelimesta tehdään kontit, mitkä voivat olla yhteydessä toisiinsa. Etusivun kautta saadaan yhteys palvelimelle. Käyttäjä voi tallentaa palvelimelle tekstiä mikä näkyy etusivulla. Avatessaan etusivun tämä tarkistaa saadaanko palvelimeen yhteys. Jos saadaan, niin käyttäjä voi lähettää tekstiä palvelimelle. Lähetetyt tekstit näkyvät etusivulla ja ne voidaan myös poistaa. Kun palvelimeen ei saada yhteyttä ilmoittaa frontend siitä käyttäjälle, eikä tällöin voida lähettää tekstiä.

### Käyttöönotto
Palvelun saa käyttöön osoitteeseen http://localhost ajamalla Docker Composella komennon
```
docker-compose up
```

### Etusivu - frontend
Etusivu käyttää peruskuvana on **Nginx** -palvelimen versio **stable-alpine3.20-perl**. Tälle on avattuna portit 80:80 joiden kautta siihen voidaan olla yhteydessä. Sivu http://localhost yrittää ottaa yhteyttä palvelimen osoitteeseen http://localhost:5000 ja tekee sinne POST ja GET pyyntöjä. Sivulla on kolme funktiota jotka ovat seuraavat.

Kaikki tallennetut viestit pyydetään GET pyynnöllä osoitteesta
```
http://localhost:5000/findmessage
``` 
Uusi viesti lähetetään POST pyynnöllä osoitteeseen
```
http://localhost:5000/newmessage
```
Viestien poistoa pyydetään POST pyynnöllä osoitteesta
```
http://localhost:5000/removemessage
```

### Palvelin - backend
Palvelin käyttää peruskuvanaan **Pythonin** versiota **3.14.0a3-alpine3.21**. Kontille varmistetaan, että **pip** on asennettu ja tämän kautta asennetaan **Flask** palvelu, sekä **flask-cors**, jotta projektia voi ajaa samalla tietokoneella. Kontille on avattu portit 5000:5000 Saadessaan pyynnön osoitteeseen http://localhost:5000/newmessage viesti tallennetaan tiedostoon **data/messages.json**. Tästä samasta tiedostosta myös noudetaan tai poistetaan kaikki viestit. 

Viestit on tallennettu json-muodossa käyttäen muotoa 
```
{
    "allMessages": [
        {
            "message": "Viesti"
        },
        {
            "message": Toinen viesti
        },
        ...
    ]
}
```

Palvelimelle on muodostettu volume nimeltä **message_data** mikä jakaa tiedoston **data/messages.json** käyttäjälle tallennettavaksi.

/findmessage


Tehtävä:          

Tehtävänä on muodostaa mikropalvelukäytänteen mukainen ympäristö, jonka käyttötarkoituksena on esitellä Docker osaamistanne. Ajatuksena on luoda muutama webbisivu, joissa läpikäydään ryhmän oman osaamisen kautta docker, docker compose ja muita kurssin aikana läpikäytyjä tekniikoita ja ominaisuuksia. Tehtävän lopputuloksena tulisi syntyä ajettava ympäristö, jonka voi ottaa käyttöön kurssin aikana käytetyn kaltaisessa ympäristössä tai julkisessa pilvipalvelurakenteessa. Toteutetun ympäristön tulisi olla laajennettavissa myös kuvitteellisen käyttäjän omille muistiinpanoille.

Palauta:          

Palauta vähintään alustan määrittelytiedot sekä sisältö. Kuvaa projekti word tiedostona tai vastaavana. Voit halutessasi palauttaa myös github jakelun.

Arviointi:         

Tehtävä arvioidaan muutamassa erillisessä osassa. Tehtävästä ryhmä voi saada maksimissaan 50 pistettä. Näistä 20 tulee rakenteesta (toteutus dockerilla) sekä 20 dokumentoinnista. Viimeiset 10 pistettä tulevat rakenteen soveltuvuudesta sekä sisällöstä palvelussa.

Opetus:            

Tehtävän tarkoituksena on opettaa ryhmässä tehtävän mikropalvelun suunnittelua, dokumentointia ja jakelua. 