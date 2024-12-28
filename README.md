# DockerProjekti
Pilvipalvelut -kurssin tehtävä.

Projekti on jaettu kolmeen osaan, mitkä ovat frontend, palvelin ja tietokanta. Frontendin kautta saadaan yhteys palvelimelle ja tämän kautta tietokantaan. Käyttäjä voi tallentaa palvelimelle tekstiä.

Avatessaan frontendin tämä tarkistaa saadaanko palvelimeen yhteys. Jos saadaan, niin käyttäjä voi lähettää tekstiä palvelimelle. Lähetetyt tekstit näkyvät etusivulla. Kun palvelimeen ei saada yhteyttä ilmoittaa frontend siitä käyttäjälle, eikä tällöin voida lähettää tekstiä.

Palvelin vastaanottaa käyttäjän tekstin, sekä lähettää käyttäjälle jo tallennetut tekstit. Tietokanta on yhteydessä palvelimeen, minne tallennetaan tekstit.


Tehtävä:          

Tehtävänä on muodostaa mikropalvelukäytänteen mukainen ympäristö, jonka käyttötarkoituksena on esitellä Docker osaamistanne. Ajatuksena on luoda muutama webbisivu, joissa läpikäydään ryhmän oman osaamisen kautta docker, docker compose ja muita kurssin aikana läpikäytyjä tekniikoita ja ominaisuuksia. Tehtävän lopputuloksena tulisi syntyä ajettava ympäristö, jonka voi ottaa käyttöön kurssin aikana käytetyn kaltaisessa ympäristössä tai julkisessa pilvipalvelurakenteessa. Toteutetun ympäristön tulisi olla laajennettavissa myös kuvitteellisen käyttäjän omille muistiinpanoille.

Palauta:          

Palauta vähintään alustan määrittelytiedot sekä sisältö. Kuvaa projekti word tiedostona tai vastaavana. Voit halutessasi palauttaa myös github jakelun.

Arviointi:         

Tehtävä arvioidaan muutamassa erillisessä osassa. Tehtävästä ryhmä voi saada maksimissaan 50 pistettä. Näistä 20 tulee rakenteesta (toteutus dockerilla) sekä 20 dokumentoinnista. Viimeiset 10 pistettä tulevat rakenteen soveltuvuudesta sekä sisällöstä palvelussa.

Opetus:            

Tehtävän tarkoituksena on opettaa ryhmässä tehtävän mikropalvelun suunnittelua, dokumentointia ja jakelua. 