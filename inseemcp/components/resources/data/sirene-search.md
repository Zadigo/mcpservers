# Les services de l'API Sirene

## Recherche unitaire - Présentation du service

Le service de recherche unitaire sur Siren ou Siret permet d’interroger l'API Sirene selon deux optiques différentes :

* obtenir l’historique complet de l'unité légale ou de l'établissement correspondant
* obtenir la situation de l'unité légale ou de l'établissement correspondant à une date donnée

En effet, certaines variables du répertoire sont disponibles pour l'ensemble des valeurs successives qu'elles ont prises au cours de la vie de l'unité légale ou de l'établissement : elles sont dites historisées.

D'autres variables ne sont disponibles que dans leur valeur courante : elles sont dites non historisées.

Dans le cas d'une recherche sur un siren en doublon, l'API redirige vers l'unité légale doublonnée.

Dans le cas d'une recherche sur un siret associé à un siren en doublon, l'API redirige vers l'établissement siège de l'unité légale doublonnée.

## URL d'accès

Il s'agit d'un service web de type REST, qui s'appuie donc uniquement sur les protocoles et standards utilisés sur le web. L'invocation du service se fait par envoi d'une requête HTTPS (de type GET) sur une URL publique.

URL d'accès au service de recherche unitaire sur le Siren :

```text
https://api.insee.fr/api-sirene/3.11/siren/{siren}
```

URL d'accès au service de recherche unitaire sur le Siret :

```text
https://api.insee.fr/api-sirene/3.11/siret/{siret}
```

**En-tête de la requête**

L'authentification se fait en passant votre clé d'accès dans l'en-tête Authorization, accompagné du verbe « GET ». Cette clé est fournie par le portail des APIs de l'Insee.

Le seul format de données possible est le json : Accept = application/json.

Le contenu de la réponse peut être compressé afin de limiter sa taille. L'algorithme de compression utilisé est le gzip. Pour recevoir une réponse compressée, il faut ajouter dans l'en-tête HTTP le paramètre Accept-Encoding = gzip.

**Corps de la requête**

Les paramètres de la requête sont les suivants, le seul paramètre obligatoire étant le siren/siret :

**siren ou siret**

**date** (de la forme AAAA-MM-JJ) : voir chapitre Paramètres d'une requête > Recherche sur date
**champs** : voir chapitre Paramètres d'une requête > Sélection des champs
**masquerValeursNulles** : voir chapitre Paramètres d'une requête > Masquer les valeurs nulles

Dans la requête URL :

* le séparateur entre le siren/siret et un éventuel paramètre facultatif est le « ? »
* le séparateur entre deux paramètres facultatifs est le « & »

**Obtenir l'historique complet**

Il s'agit du mode d'interrogation par défaut. À partir d'un Siren ou Siret donné, le service permet de récupérer l'historique complet présent dans le répertoire pour l'unité légale ou l'établissement correspondant, jusqu'à la veille du jour d'interrogation.

**Obtenir la période qui englobe la date demandée**

La requête passée avec le paramètre facultatif date permet de récupérer uniquement la période de l'unité légale ou de l'établissement contenant la date passée en paramètre :

```text
https://api.insee.fr/api-sirene/3.11/siren/{siren}?date={date}

https://api.insee.fr/api-sirene/3.11/siret/{siret}?date={date}
```

Si la date renseignée dans le paramètre est antérieure à la première période, le service renvoie une erreur.
