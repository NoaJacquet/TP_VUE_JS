# README - Application Vue pour Questionnaire

# Lien du git
https://github.com/NoaJacquet/TP_VUE_JS/

### Développeur 01
- Nom : MARIDAT
- Prénom : ETHAN
- Identifiant Github : [EthanMaridat](https://github.com/Ethan-Maridat)

### Développeur 02
- Nom : JACQUET
- Prénom : Noa
- Identifiant Github : [NoaJacquet](https://github.com/NoaJacquet)


Ce README fournit des instructions concernant le projet d'Architecture logicielle : une application en VueJS qui gère des questionnaires via un serveur REST. Le projet a été réalisé dans le cadre d'un travail de groupe.

## Instructions pour lancer l'application
- Cloner le dépôt : Commencez par cloner le dépôt contenant le code de l'application Vue ainsi que le serveur REST.

- Lancer le serveur REST 

```
cd quiz
flask run
```

- Lancer le'application

```
cd ../projettodos
npm run dev --host
```


## Explication des choix de modélisation
Les choix de modélisation ont été guidés par les besoins fonctionnels de l'application et par la structure des données fournies par le serveur REST. Voici quelques points clés :

- Organisation des composants Vue : Les composants ont été organisés de manière logique pour faciliter la maintenance et l'évolutivité de l'application. Par exemple, les composants liés à la gestion des questionnaires sont regroupés dans un répertoire distinct.

- Utilisation des méthodes HTTP : L'application utilise les méthodes HTTP appropriées (GET, POST, PUT, DELETE) pour interagir avec le serveur REST. Cela garantit une manipulation correcte des données côté client.

- Validation des données : La validation des données est effectuée à la fois côté client et côté serveur pour garantir l'intégrité des données et éviter les erreurs.

- Interface utilisateur conviviale : Une attention particulière a été portée à l'interface utilisateur pour assurer une expérience utilisateur fluide et intuitive lors de la gestion des questionnaires et des questions.
 