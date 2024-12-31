# DockerProjekti
### Tietoa
Pilvipalvelut -kurssin Docker tehtävä.

Projektin sisältö on jaettu kahteen osaan, mitkä ovat etusivu eli frontend, sekä palvelin eli backend. Kummastakin etusivusta ja palvelimesta tehdään kontit, mitkä voivat olla yhteydessä toisiinsa. Etusivun kautta saadaan yhteys palvelimelle. Käyttäjä voi tallentaa palvelimelle tekstiä mikä näkyy etusivulla. Avatessaan etusivun tämä tarkistaa saadaanko palvelimeen yhteys. Jos saadaan, niin käyttäjä voi lähettää tekstiä palvelimelle. Lähetetyt tekstit näkyvät etusivulla ja ne voidaan myös poistaa. Kun palvelimeen ei saada yhteyttä ilmoittaa frontend siitä käyttäjälle, eikä tällöin voida lähettää tekstiä.

### Käyttöönotto
Palvelun saa käyttöön osoitteeseen http://localhost ajamalla DockerProjekti -kansiossa Docker Composella komennon
```
docker-compose up
```
Tämä muodostaa backend kansiosta kuvan **DockerProjekti/backend** ja frontend kansiosta kuvan **DockerProjekti/frontend**.

### Etusivu - frontend
Etusivun peruskuvana on **Nginx** -palvelimen versio **stable-alpine3.20-perl**. Tälle on avattuna portit 80:80 joiden kautta siihen voidaan olla yhteydessä. Sivu http://localhost yrittää ottaa yhteyttä palvelimen osoitteeseen http://localhost:5000 ja tekee sinne POST ja GET pyyntöjä. Tämä sivu lähettää seuraavia pyyntöjä palvelimelle tarpeen mukaan.

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
            "message": ""
        },
        {
            "message": "viesti"
        },
        ...
    ]
}
```

Palvelimelle on muodostettu volume nimeltä **dockerprojekti_message_data** mikä jakaa tiedoston **data/messages.json** käyttäjälle tallennettavaksi.