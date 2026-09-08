# Recherche multicritère

## Recherche de tous les établissement dont le siren commence par 3

```
https://api.insee.fr/api-sirene/3.11/siret?q=siren:3*&champs=siret,denominationUniteLegale&curseur=*
```

```JSON

{
    "header": {
    "statut": 200,
    "message": "OK",
    "total": 8770580,
    "debut": 0,
    "nombre": 20,
    "curseur": "*",
    "curseurSuivant": "AoEuMzAwMDAwMzUzMDAwMTU="
}
```

```
siret,denominationUniteLegale
30000001500010,
30000002300014,
30000004900019,
30000007200029,
30000008000014,
30000009800032,
30000009800040
```

## Variables non historisées

### Recherche de tous les établissements du Siren `775672272` :

```
https://api.insee.fr/api-sirene/3.11/siret?q=siren:775672272
```

### Recherche de toutes les unités purgées

```
https://api.insee.fr/api-sirene/3.11/siren?q=unitePurgeeUniteLegale:tru
```

### Recherche de tous les établissements des unités purgées

```
https://api.insee.fr/api-sirene/3.11/siret?q=unitePurgeeUniteLegale:true
```

### Recherche de tous les établissements de la commune de Malakoff (code commune=92046)

```
https://api.insee.fr/api-sirene/3.11/siret?q=codeCommuneEtablissement:92046
```

## Variables historisées

### Recherche de toutes les UL dont la dénomination contient ou a contenu le mot GAZ :

```
https://api.insee.fr/api-sirene/3.11/siren?q=periode(denominationUniteLegale:GAZ)
```

### Recherche de toutes les UL qui ont été cessées :

```
https://api.insee.fr/api-sirene/3.11/siren?q=periode(etatAdministratifUniteLegale:C)
```

### Recherche de tous les établissements dont le code de l'activité principale a été (ou est*) 33.01 :

```
https://api.insee.fr/api-sirene/3.11/siret?q=periode(activitePrincipaleEtablissement:33.01)
```

> [!WARNING]
> (*) 33.01 appartenant à une ancienne nomenclature, une unité légale (resp. un établissement) ne peut pas avoir ce code en valeur courante si elle est active.

## Elimination

### Recherche de tous les établissements dont l'unité légale est considérée comme une personne morale :

```
https://api.insee.fr/api-sirene/3.11/siret?q=-categorieJuridiqueUniteLegale:1000
```

### Recherche de tous les établissements qui n'ont jamais été fermés :

```
https://api.insee.fr/api-sirene/3.11/siret?q=-periode(etatAdministratifEtablissement:F)
```

## Connecteurs `AND` et `OR`

### Recherche de toutes les entreprises dont l'activité principale est 84.23Z ou 86.21Z, ou l'a été par le passé :

```
https://api.insee.fr/api-sirene/3.11/siren?q=periode(activitePrincipaleUniteLegale:84.23Z OR activitePrincipaleUniteLegale:86.21Z)
```

### Recherche de tous les établissements relevant des catégories juridiques 5510 et 5520 :

```
https://api.insee.fr/api-sirene/3.11/siret?q=categorieJuridiqueUniteLegale:5510 OR categorieJuridiqueUniteLegale:5520
```

### Recherche de tous les établissements qui ont au moins une période où leur état est « actif » et leur activité principale est 84.23Z :

```
https://api.insee.fr/api-sirene/3.11/siret?q=periode(activitePrincipaleEtablissement:84.23Z AND etatAdministratifEtablissement:A)
```

### Recherche de tous les établissements qui ont moins une période dont l'activitePrincipaleEtablissement est 84.23Z et qui n'ont jamais été fermés :

```
https://api.insee.fr/api-sirene/3.11/siret?q=periode(activitePrincipaleEtablissement:84.23Z) AND -periode(etatAdministratifEtablissement:F)
```

### Recherche de tous les établissements de Malakoff dont la dernière catégorie juridique est 9220 :

```
https://api.insee.fr/api-sirene/3.11/siret?q=codeCommuneEtablissement:92046 AND categorieJuridiqueUniteLegale:9220
```

### Recherche de toutes les entreprises exerçant l'activité « marchand de biens » et appartenant à la catégorie PME (Cf. supra : combinaison de variables historisées et non-historisées, paramètre date) :

```
https://api.insee.fr/api-sirene/3.11/siren?q=periode(activitePrincipaleUniteLegale:68.10Z) AND categorieEntreprise:PME&date=2030-12-31
```

## Format date

### Recherche de toutes les UL dont la date de création est au 01/01/2014 :

```
https://api.insee.fr/api-sirene/3.11/siren?q=dateCreationUniteLegale:2014-01-01
```

### Recherche de toutes les UL dont l'année de création est entre 1980 et 2003 :

```
https://api.insee.fr/api-sirene/3.11/siren?q=dateCreationUniteLegale:[1980 TO 2003]
```

### Recherche de tous les établissements mis à jour au mois de février 2018 et non mis à jour depuis :

```
https://api.insee.fr/api-sirene/3.11/siret?q=dateDernierTraitementEtablissement:2018-02
```

### Recherche de toutes les UL qui ont eu un changement de dénomination l'année 2017 :

```
https://api.insee.fr/api-sirene/3.11/siren?q=periode(changementDenominationUniteLegale:true AND dateDebut:2017)
```

### Plage de valeur

### Recherche de tous les etablissements d'UL dont le nom d'usage va de DUPONT à DURAND, y compris DUPONT et DURAND :

```
https://api.insee.fr/api-sirene/3.11/siret?q=nomUsageUniteLegale:[DUPONT TO DURAND]
```

### Recherche de tous les etablissements d'UL dont le nom d'usage va de DUPONT à DURAND, non compris DUPONT et DURAND :

```
https://api.insee.fr/api-sirene/3.11/siret?q=nomUsageUniteLegale:%7BDUPONT TO DURAND%7D
```

### Recherche de tous les etablissements d'UL dont le nom d'usage va de DUPONT à DURAND, Y compris DUPONT et non compris DURAND :

```
https://api.insee.fr/api-sirene/3.11/siret?q=nomUsageUniteLegale:[DUPONT TO DURAND%7D
```

### Recherche de tous les établissements de médecins généralistes dont le nombre de périodes va de 12 à 20 (inclus) :

```
https://api.insee.fr/api-sirene/3.11/siret?q=categorieJuridiqueUniteLegale:1000 AND activitePrincipaleUniteLegale:86.21Z AND nombrePeriodesEtablissement:[12 TO 20]&champs=siret,nombrePeriodesEtablissement
```

```
siret,nombrePeriodesEtablissement
31334539900023,15
32859956800016,12
32882929600032,12
35204040600022,12
39333255600025,13
41797549700013,13
41998955300021,14
```

## Recherche exacte

### Recherche de toutes les unités légales dont la dénomination contient exactement le terme "LE TIMBRE" :

```
https://api.insee.fr/api-sirene/3.11/siren?q=periode(denominationUniteLegale:"LE TIMBRE")
```

## Caractère `*`

### Recherche de tous les établissements des unités légales dont l'activité principale commence par 8

```
https://api.insee.fr/api-sirene/3.11/siret?q=activitePrincipaleUniteLegale:8*
```

### Recherche de tous les établissements des unités légales dont le sigle n'est pas rempli :

```
https://api.insee.fr/api-sirene/3.11/siret?q=-sigleUniteLegale:*
```

### Recherche de toutes les unités légales dont le siren ne commence ni par 1 ni par 2 (Etat et collectivités)

```
https://api.insee.fr/api-sirene/3.11/siren?q=-siren:1* AND -siren:2*
```

### Recherche de toutes les unités légales dont la date de création est renseignée

```
https://api.insee.fr/api-sirene/3.11/siren?q=dateCreationUniteLegale:*&champs=siren,dateCreationUniteLegale
```

### Recherche de toutes les unités légales dont la date de création n'est pas renseignée

```
https://api.insee.fr/api-sirene/3.11/siren?q=-dateCreationUniteLegale:*&champs=siren
```

### Recherche de tous les établissements des unités légales dont la dénomination commence par "LAMI"

```
https://api.insee.fr/api-sirene/3.11/siret?q=denominationUniteLegale:lami*&champs=denominationUniteLegale
```

denominationUniteLegale retournées :

```
HERMITE STE LAMIRAND SCI
SYND.COPR. 5 7 IMP LAMIER P 11 REP PAR
MR BOURBON F MLE DURAND I MR LAMINIE
LAMINOIRS DU DAUPHINE - ETS BONMARTIN
TREFILERIES LAMINOIRS DE LA MEDITERRANEE
BOSSARD LAMICHE ET CIE SA
COMMUNE DE LAY LAMIDOU
COMMUNE DE LAMILLARIE
LAMIS
LAMISSE
```

> [!NOTE]
> Lorsque la dénomination ne comprend qu'un seul mot, il commence par la chaîne de caractères "LAMI" ; quand elle en comprend plusieurs, au moins un d'entre eux commence par la chaîne de caractères "LAMI".

## Caractère `?`

### Recherche de tous les établissements dont l'unité légale a un sigle sur 3 positions

```
https://api.insee.fr/api-sirene/3.11/siret?q=sigleUniteLegale:???
```

### Recherche de tous les établissements dont l'unité légale a un sigle qui commence par FC et est sur 3 positions exactement

```
https://api.insee.fr/api-sirene/3.11/siret?q=sigleUniteLegale:FC?
```

## Caractère `~`

### Recherche de tous les établissements dont l'unité légale a comme prenom1UniteLegale MICKAEL à deux caractères près, mais pas MICKAEL exactement :

```
https://api.insee.fr/api-sirene/3.11/siret?q=prenom1UniteLegale:MICKAEL~ AND -prenom1UniteLegale:MICKAEL
```

### Recherche de tous les établissements dont l'unité légale a pour sigle PAUL à une erreur près

```
https://api.insee.fr/api-sirene/3.11/siret?q=sigleUniteLegale:PAUL~1
```

### Recherche de tous les établissements dont l'unité légale a une dénomination sociale comprenant "BLEU LE"

**Sans le ~ (recherche exacte) :**

```
https://api.insee.fr/api-sirene/3.11/siret?q=denominationUniteLegale:"bleu le"&nombre=20&champs=denominationUniteLegale
```

`denominationUniteLegale` retournée :

```
PRINTEMPS BLEU LE CHOIX DE LA SANTE
```

**Avec ~2 (recherche approximative)**

```
https://api.insee.fr/api-sirene/3.11/siret?q=denominationUniteLegale:"bleu le"~2&nombre=100&champs=denominationUniteLegale
```

`denominationUniteLegale` retournées :

```
extLE BLEU DU CIEL VOYAGES
L'ENERGIE RENOUVELABLE - BLEU COMME LE CIEL
LE BLEU DES ILES
SCI S LE BLEU
PRINTEMPS BLEU LE CHOIX DE LA SANTE
LE BLEU MARINE
```

**Recherche approximative sur plusieurs termes**

```
https://api.insee.fr/api-sirene/3.11/siret?q=denominationUniteLegale:yst~ AND denominationUniteLegale:anotwer~ AND denominationUniteLegale:copany~&champs=denominationUniteLegale&nombre=1000
```

`denominationUniteLegale` retournée :

```
Yet another company
```

## References

### Python

```python
import httpx2
from urllib.parse import urlencode

headers = {
    'Accept': 'application/json',
    'X-INSEE-Api-Key-Integration': 'YOUR_API_KEY'
}

query = {'q': 'siren:775672272'}
response = httpx2.get("https://api.insee.fr/api-sirene/3.11/siret?" + urlencode(query), headers=headers)
```

## Golang

```go
package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "net/url"
)

func main() {
    baseURL := "https://api.insee.fr/api-sirene/3.11/siret"
    params := url.Values{}
    params.Add("q", "siren:775672272")

    req, err := http.NewRequest("GET", baseURL+"?"+params.Encode(), nil)
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Accept", "application/json")
    req.Header.Set("X-INSEE-Api-Key-Integration", "YOUR_API_KEY")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error making request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println(string(body))
}
```
