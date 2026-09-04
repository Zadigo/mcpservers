
# Établissement

## siret

---

Numéro siret de l'établissement.
C'est le numéro unique d'identification attribué à chaque établissement par l'Insee.
Ce numéro est un simple numéro d'ordre, composé de 14 chiffres non significatifs : les neuf premiers correspondent au numéro Siren de l'entreprise dont l'établissement dépend et les cinq derniers à un numéro interne de classement (Nic).

Une entreprise est constituée d'autant d'établissements qu'il y a de lieux différents où elle exerce son activité. L'établissement est fermé quand l'activité cesse dans l'établissement concerné ou lorsque l'établissement change d'adresse.

**Type**

Non-historisé. Texte numérique de longueur 14.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | oui                                  |

## activitePrincipaleEtablissement

---

Lors de son inscription au répertoire, l’Insee attribue à tout établissement un code dit « **APET** » (**A**ctivité **P**rincipale de l'**ET**ablissement) sur la base de la description de l’activité principale faite par le déclarant.
Ce code est modifiable au cours de la vie de l’établissement en fonction des déclarations de l’exploitant.
Pour chaque établissement, il existe à un instant donné un seul code APET.

La variable nomenclatureActivitePrincipaleEtablissement indique à quelle nomenclature d'activité appartient le code.
Tous les établissements actifs ont un code d'activité principale appartenant à la nomenclature la plus récente.
Les établissements fermés ont un code d'activité principale appartenant à la nomenclature en vigueur à la date de prise en compte de leur fermeture.

Les personnes morales ont la possibilité de s'immatriculer sans activité (elles déclarent alors leur commencement d'activité dans un second temps, dans les 12 mois suivant la création) : dans ce cas, l'Insee attribue à l'établissement (unique) le code APET 00.00Z jusqu'à la prise d'activité.
L'APE peut être à *null* (cas des unités purgées, première date de début de l'APE postérieure à la première date de début d'une autre variable historisée).

**Historique**

Le code APE est historisé depuis le 01/01/2005.

La règle d’historisation des données d’activité est la suivante :

* Pour les établissements fermés avant 31/12/2004, seul le dernier code activité connu figure, dans la nomenclature en vigueur à la date de fermeture.
* Pour les établissements ouverts après le 01/01/2005 et fermés avant le 31/12/2007, l'historique des codes attribués sur la période est disponible.
* Pour les établissements ouverts après le 01/01/2005 et toujours ouverts le 01/01/2008, l'historique intègre le changement de nomenclature.
* Pour les établissements ouverts après le 01/01/2008, l'historique comprend les modifications apportées au cours de la vie de l'établissement.

**Type**

Historisé. Liste de codes de longueur 6, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | oui                                  |

## activitePrincipaleNAF25Etablissement

---

Cette variable contient le code APE de l'établissement en nomenclature NAF25.
Elle est renseignée pour les établissements actifs, ou récemment fermés.
Elle est présente à titre d'information, et disparaîtra lorsque la NAF25 deviendra la nomenclature officielle, donc au 01/01/2027. A partir de cette date, on pourra alors retrouver le code NAF25 dans la variable  *activitePrincipaleEtablissement* .
Les personnes qui souhaitent demander une correction de leur code NAF25 peuvent le faire via un site de rectification du code APE.

**Type**

Non-historisé. Liste de codes de longueur 6, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## activitePrincipaleRegistreMetiersEtablissement

---

Activité principale de l'établissement au Registre des Métiers.
Cette variable, complémentaire à l'activité principale de l'établissement, ne concerne que les établissements relevant de l'artisanat (artisans, artisans-commerçants et sociétés artisanales).
Elle caractérise l'activité selon la Nomenclature d'Activités Française de l'Artisanat (NAFA).
La variable n'est pas disponible au niveau unité légale.

**Type**

Non-historisé. Liste de codes, de longueur 6, 4 chiffres et 1 lettre (sans point) correspondant au code APET, suivis d'une lettre spécifique à la NAFA, ou  *null* . Lien vers la Nomenclature d'Activités Française de l'Artisanat [ici](https://data.artisanat.fr/nafa/).

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## anneeEffectifsEtablissement

---

Année de validité de la tranche d'effectif salarié de l'établissement.
La mise à jour des tranches d'effectifs est annuelle (automne).
Pour les établissements dont la tranche d’effectifs est renseignée, l’année de validité correspondante est l’année millésime N (voir trancheEffectifsEtablissement).
Il n'y a jamais plus d’un seul millésime présent dans la base Sirene.

**Type**

Non-historisé. Date, de longueur 4, format AAAA, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## caractereEmployeurEtablissement

---

Caractère employeur de l'établissement.
Lors de sa formalité d'ouverture, le déclarant indique si l'établissement aura ou non des salariés au démarrage de l'activité. Par la suite, il peut déclarer alternativement des prises d'emploi (première embauche ou réembauche de salariés) et des fins d'emploi (départ du dernier salarié).
Ces déclarations se font auprès de l’URSSAF qui transmet l’information à l’Insee. Les données ne peuvent être corrigées qu’à cette condition. Dès réception, l’Insee, bascule immédiatement l’établissement en « Employeur », en cas de prise d’emploi, ou en « Non employeur » en cas de fin d’emploi.
À noter : lors de la fermeture de l'établissement, la variable caractereEmployeurEtablissement n'est pas mise à jour et conserve la dernière valeur connue.

**Type**

Historisé. Liste de codes de longueur 1, ou *null* :

* O : établissement employeur
* N : établissement non employeur

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | oui                                  |

## codeCedexEtablissement

---

Code cedex de l'établissement.
Cette variable facultative est un élément constitutif de l'adresse.

**Type**

Texte de longueur 4. La variable n'est plus gérée, toujours  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## codeCedex2Etablissement

---

Code cedex de l'adresse secondaire de l'établissement.
Dans le cas où l'établissement dispose d'une entrée secondaire, codeCedex2Etablissement est un élément constitutif de l'adresse secondaire.
Cette variable est facultative.

**Type**

Texte de longueur 4. La variable n'est plus gérée, toujours  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## codeCommuneEtablissement

---

Cette variable désigne le code géographique de la commune de localisation de l'établissement, hors adresse à l'étranger.
Le code commune est celui défini par la Base Adresse Nationale (BAN), au moment du traitement de la formalité la plus récente liée à une modification d’adresse.
Pour les établissements localisés à l'étranger, la variable codeCommuneEtablissement est à  *null* .

**Type**

Non-historisé. Liste de codes de longueur 5, ou  *null* . Lien vers le [code officiel géographique](https://www.insee.fr/fr/information/2560452).

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## codeCommune2Etablissement

---

Code commune de l'adresse secondaire de l'établissement.
Dans le cas où l'établissement dispose d'une entrée secondaire, cette variable désigne le code de la commune de l'adresse secondaire de l'établissement, hors adresse à l'étranger.

**Type**

La variable n'est plus gérée, toujours  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## codePaysEtrangerEtablissement

---

Cette variable désigne le code du pays de localisation de l'établissement pour les adresses à l'étranger.
La variable codePaysEtrangerEtablissement commence toujours par 99 si elle est renseignée. Les 3 caractères suivants sont le code du pays étranger.

**Type**

Non-historisé. Liste de codes de longueur 5, ou  *null* . Lien vers le [code officiel géographique](https://www.insee.fr/fr/information/2560452).

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## codePaysEtranger2Etablissement

---

Dans le cas où l'établissement dispose d'une entrée secondaire, cette variable désigne le code du pays de localisation de l'adresse secondaire de l'établissement pour les adresses à l'étranger.

**Type**

La variable n'est plus gérée, toujours  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## codePostalEtablissement

---

Cette variable désigne le code postal de l'adresse de l'établissement.

**Type**

Non-historisé. Texte de longueur 9, ou  *null* , ou [ND] si l'unité est en diffusion partielle.
Les codes postaux étrangers sont donnés à titre indicatif. Ils sont de longueur variable et peuvent contenir des lettres ou des blancs.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## codePostal2Etablissement

---

Dans le cas où l'établissement dispose d'une entrée secondaire, cette variable désigne le code postal de l'adresse secondaire de l'établissement.

**Type**

Texte de longueur 4. La variable n'est plus gérée, toujours  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## complementAdresseEtablissement

---

Complément d'adresse de l'établissement.
Cette variable est un élément constitutif de l'adresse.

C'est une variable facultative qui précise l'adresse avec :

* une indication d'étage, d'appartement, de porte, de N° de boîte à lettres ;
* la désignation d'un bâtiment, d'un escalier, d'une entrée, d'un bloc ;
* le nom d'une résidence, d'un ensemble...

**Type**

Non-historisé. Texte de longueur 100, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## complementAdresse2Etablissement

---

Complément d'adresse secondaire de l'établissement.
Dans le cas où l'établissement dispose d'une entrée secondaire, cette variable est un élément constitutif de l'adresse secondaire.

**Type**

Texte de longueur 4. La variable n'est plus gérée, toujours  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## coordonneeLambertAbscisseEtablissement

---

Abscisse des coordonnees Lambert de l'adresse.
Une des deux coordonnées (avec coordonneeLambertOrdonneeEtablissement) permettant la géolocalisation des établissements.

**Type**

Non-historisé. Texte de longueur 18, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Dès Sirene 4                                  | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Dès Sirene 4              | non                                  |

## coordonneeLambertOrdonneeEtablissement

---

Ordonnée des coordonnees Lambert de l'adresse.
Une des deux coordonnées (avec coordonneeLambertAbscisseEtablissement) permettant la géolocalisation des établissements.

**Type**

Non-historisé. Texte de longueur 18, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Dès Sirene 4                                  | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Dès Sirene 4              | non                                  |

## dateCreationEtablissement

---

Date de création de l'établissement.
Elle correspond à la date qui figure dans la déclaration déposée au CFE compétent.
Pour les établissements des unités purgées (unitePurgeeUniteLegale= *true* ) : si la date de création est au 01/01/1900 dans Sirene, la date est forcée à  *null* .
Dans tous les autres cas, la date de création n'est jamais à  *null* . Si elle est non renseignée, elle sera au 01/01/1900.
La date de création ne correspond pas obligatoirement à dateDebut de la première période de l'établissement, certaines variables historisées pouvant posséder des dates de début soit au 1900-01-01, soit antérieures à la date de création.

**Type**

Non-historisé. Date, longueur 10, format AAAA-MM-JJ, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## dateDernierTraitementEtablissement

---

Date du dernier traitement de l'établissement dans le répertoire Sirene.
Elle peut concerner des mises à jour de données historisées ou non-historisées, mais aussi de données du répertoire Sirene qui ne sont pas diffusées par API Sirene.
Elle n’est pas impactée par une modification de la variable etablissementSiege, qui n’est pas une variable originelle de Sirene.
Cette variable peut être à  *null* , pour les unités purgées.

**Type**

Non-historisé. Date, longueur 23, format AAAA-MM-JJTHH:MM:SS.MMM, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## denominationUsuelleEtablissement

---

Cette variable désigne le nom sous lequel l'établissement est connu du grand public (nom commercial de l'établissement).
Cet élément facultatif d'identification de l'établissement a été enregistré au niveau établissement depuis l'application de la norme d'échanges CFE de 2008.
Avant la norme 2008, le nom commercial était enregistrée au niveau de l'unité légale sur trois champs (variables denominationUsuelle1UniteLegale à denominationUsuelle3UniteLegale).

**Type**

Historisé. Texte de longueur 100, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | oui                                  |

## dernierNumeroVoieEtablissement

---

En cas d'adresse groupée (ex : 11 à 17), dernier numéro du groupe, éventuellement complété par indice de répétition (bis, ter...).
Le premier numéro du groupe est renseigné dans la variable numeroVoieEtablissement.
En cas de numéro unique, la variable dernierNumeroVoieEtablissement est à  *null* .

**Type**

Non-historisé. Texte de longueur 9, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Dès Sirene 4                                  | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Dès Sirene 4              | non                                  |

## distributionSpecialeEtablissement

---

Distribution spéciale de l'établissement.
La distribution spéciale reprend les éléments particuliers qui accompagnent une adresse de distribution spéciale.
C'est un élément constitutif de l'adresse.

**Type**

Texte de longueur 4. La variable n'est plus gérée, toujours  *null* , ou [ND] si l'unité est en diffusion partielle. Exemples :

* BP : Boîte postale
* TSA : Tri par service à l'arrivée
* LP : Local postal
* RP : Référence postale
* SP : Secteur postal
* CP : Case postale
* CE : Case entreprise
* CS : Course spéciale
* POSTE RESTANTE
* CIDEX : Courrier individuel à distribution exceptionnelle
* CASE, NIVEAU : Mots utilisés pour la distribution interne du courrier à LA DEFENSE
* CASIER : Utilisé pour le centre commercial des Quatre Temps
* SILIC, SENIA, MAREE, FLEURS : Utilisés sur le site de Rungis

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## distributionSpeciale2Etablissement

---

Distribution spéciale de l'adresse secondaire de l'établissement.
Dans le cas où l'établissement dispose d'une entrée secondaire, la distribution spéciale reprend les éléments particuliers qui accompagnent l'adresse secondaire de distribution spéciale.
C'est un élément constitutif de l'adresse secondaire.
Cette variable est facultative.

**Type**

Texte de longueur 4. La variable n'est plus gérée, toujours  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## enseigne1Etablissement, enseigne2Etablissement, enseigne3Etablissement

---

Les trois variables enseigne1Etablissement, enseigne2Etablissement et enseigne3Etablissement contiennent la ou les enseignes de l'établissement. L'enseigne identifie l'emplacement ou le local dans lequel est exercée l'activité.
Cette variable est facultative. Un établissement peut posséder une enseigne, plusieurs enseignes ou aucune.
Si l'enseigne 1 est à  *null* , les deux autres le sont aussi ; si l'enseigne 2 est à  *null* , l'enseigne 3 l'est aussi.
L'analyse des enseignes et de son découpage en trois variables dans Sirene montre deux cas possibles : soit les 3 champs concernent 3 enseignes bien distinctes, soit ces trois champs correspondent au découpage de l'enseigne qui est déclarée dans la liasse (sur un seul champ) avec une continuité des trois champs.

**Type**

Historisé. Texte de longueur 50 pour chaque enseigne, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | oui                                  |

## etablissementSiege

---

C'est une variable booléenne qui indique si l'établissement est le siège ou non de l'unité légale.
Toutes les unités légales, actives comme cessées, ont un et un seul établissement siège.
Variable calculée (hors répertoire Sirene) toujours renseignée.

**Type**

Non-historisé. Booléen : *true* ou  *false* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## etatAdministratifEtablissement

---

Etat administratif de l'établissement.
Lors de son inscription au répertoire, un établissement est, sauf exception, à l'état  **Actif** .
Le passage à l'état **Fermé** découle de la prise en compte d'une déclaration de fermeture. Un établissement fermé peut être rouvert.
En règle générale, la première période d'historique d'un établissement correspond à un etatAdministratifUniteLegale égal à  **Actif** . Toutefois, l'état administratif peut être à *null* (première date de début de l'état postérieure à la première date de début d'une autre variable historisée).

**Type**

Historisé. Liste de codes de longueur 1, ou *null* :

* A : Actif
* F : Fermé

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | oui                                  |

## identifiantAdresseEtablissement

---

Il s'agit de l'identifiant unique de l'adresse. Il se termine par une lettre identifiant sa source.

**Type**

Non-historisé. Texte de longueur 15, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Format**

* xxxxxxxxx_B : adresse provenant de la Base Adresse Nationale (BAN)
* xxxxxxxxx_C : adresse provenant du cadastre

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Dès Sirene 4                                  | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Dès Sirene 4              | non                                  |

## indiceRepetitionDernierNumeroVoieEtablissement

---

En cas d'adresse groupée (ex : 11A à 11G), indice de répétition du dernier numéro du groupe.
Le premier numéro du groupe est renseigné dans la variable numeroVoieEtablissement.
Pour le moment, en l'absence de cette variable dans les données sources du répertoire Sirene, la variable indiceRepetitionDernierNumeroVoieEtablissement est à  *null* .

**Type**

Non-historisé. Longueur 4. Texte, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Dès Sirene 4                                  | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Dès Sirene 4              | non                                  |

## indiceRepetitionEtablissement

---

Indice de répétition du numéro dans la voie (B pour Bis, T pour TER, lettres ou chiffres pour identifier différents bâtiments à une même adresse...).
Cette variable facultative est un élément constitutif de l'adresse ; elle est généralement associée à la variable numeroVoieEtablissement.

**Type**

Non-historisé. Longueur 4. Texte, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## indiceRepetition2Etablissement

---

Indice de répétition du numéro dans la voie de l'adresse secondaire (B pour Bis, T pour TER, lettres ou chiffres pour identifier différents bâtiments à une même adresse...).
Dans le cas où l'établissement dispose d'une entrée secondaire, cette variable facultative est un élément constitutif de l'adresse.
Elle est généralement associée à la variable numeroVoie2Etablissement.

**Type**

Texte de longueur 4. La variable n'est plus gérée. Toujours  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## libelleCedexEtablissement

---

Libellé associé au code cedex.
Cette variable indique le libellé correspondant au code cedex de l'établissement si celui-ci est non  *null* .
Ce libellé est le libellé utilisé dans la ligne 6 d'adresse pour l'acheminement postal.

**Type**

Texte de longueur 4. La variable n'est plus gérée, toujours  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## libelleCedex2Etablissement

---

Libellé associé au code cedex de l'adresse secondaire.
Dans le cas où l'établissement dispose d'une entrée secondaire, cette variable indique le libellé correspondant au code cedex de l'établissement si celui-ci est non  *null* .
Ce libellé est le libellé utilisé dans la ligne 6 d'adresse pour l'acheminement postal.

**Type**

Texte de longueur 4. La variable n'est plus gérée, toujours  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## libelleCommuneEtablissement

---

Cette variable indique le libellé de la commune de localisation de l'établissement si celui-ci n'est pas à l'étranger.
C'est un élément constitutif de l'adresse.

**Type**

Non-historisé. Texte de longueur 100, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## libelleCommune2Etablissement

---

Dans le cas où l'établissement dispose d'une entrée secondaire, cette variable indique le libellé de la commune de localisation de l'établissement si celui-ci n'est pas à l'étranger.
C'est un élément constitutif de l'adresse.

**Type**

La variable n'est plus gérée, toujours  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## libelleCommuneEtrangerEtablissement

---

Libellé de la commune pour un établissement situé à l'étranger.
Cette variable est un élément constitutif de l'adresse pour les établissements situés sur le territoire étranger.

**Type**

Non-historisé. Texte de longueur 100, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## libelleCommuneEtranger2Etablissement

---

Libellé de la commune pour un établissement situé à l'étranger.
Dans le cas où l'établissement dispose d'une entrée secondaire, cette variable est un élément constitutif de l'adresse pour les établissements situés sur le territoire étranger.

**Type**

La variable n'est plus gérée, toujours  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## libellePaysEtrangerEtablissement

---

Cette variable indique le libellé du pays de localisation de l'établissement si celui-ci est à l'étranger.

**Type**

Non-historisé. Texte de longueur 100, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## libellePaysEtranger2Etablissement

---

Dans le cas où l'établissement dispose d'une entrée secondaire, cette variable indique le libellé du pays de localisation de l'établissement si celui-ci est à l'étranger.

**Type**

La variable n'est plus gérée, toujours  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## libelleVoieEtablissement

---

Cette variable indique le libellé de voie de la commune de localisation de l'établissement.
C'est un élément constitutif de l'adresse.
Cette variable est facultative : elle n'est pas toujours renseignée, en particulier dans les petites communes.

**Type**

Non-historisé. Texte de longueur 100, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## libelleVoie2Etablissement

---

Dans le cas où l'établissement dispose d'une entrée secondaire, cette variable indique le libellé de voie de la commune de localisation de l'établissement.
C'est un élément constitutif de l'adresse.
Cette variable est facultative : elle n'est pas toujours renseignée, en particulier dans les petites communes.

**Type**

Texte de longueur 4. La variable n'est plus gérée, toujours  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## nic

---

Numéro interne de classement de l'établissement, composé de cinq chiffres.
Il permet de distinguer les établissements d'une même entreprise.
Associé au siren, il forme le siret de l'établissement. Son cinquième chiffre permet de contrôler la validité du numéro Siret.
Le Nic est attribué une seule fois au sein de l'entreprise. Si l'établissement ferme, son nic ne peut être attribué à un autre établissement ; s'il rouvre, le nic est réactivé.

**Type**

Non-historisé. Texte de longueur 5.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | oui                                  |

## nombrePeriodesEtablissement

---

Cette variable donne le nombre de périodes [dateDebut,dateFin] de l'établissement.
Chaque période correspond à l'intervalle de temps pendant lequel aucune des variables **historisées** de l'établissement n'a été modifiée.
Les dates de ces périodes sont des dates d'effet (et non des dates de traitement).

**Type**

Non-historisé. Numérique de longueur 2.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## nomenclatureActivitePrincipaleEtablissement

---

Cette variable indique la nomenclature d'activité correspondant au code de l'activité principale de l'établissement, indiqué par la variable activitePrincipaleEtablissement.
La variable nomenclatureActivitePrincipaleEtablissement est à *null* si la variable activitePrincipaleEtablissement est à  *null* .
La nomenclature en vigueur est la Naf rév. 2, et ce depuis le 01 Janvier 2008. Chaque code comporte 4 chiffres et une lettre.

Liens vers les nomenclatures d'activités successives :

| Date                                     | Nomenclature      | Liens                                              |
| ---------------------------------------- | ----------------- | -------------------------------------------------- |
| Depuis le 1er janvier 2008               | NAF rév. 2, 2008 | [Lien](https://www.insee.fr/fr/information/2120875) |
| Du 1er janvier 2003 au 31 décembre 2007 | NAF rév. 1, 2003 | [Lien](https://www.insee.fr/fr/information/2408180) |
| Du 1er janvier 1993 au 31 décembre 2002 | NAF 1993          | [Lien](https://www.insee.fr/fr/information/2408178) |
| Du 1er janvier 1973 au 31 décembre 1992 | NAP               | [Lien](https://www.insee.fr/fr/information/3582824) |

**Type**

Historisé. Liste de codes de longueur 8, ou *null* :

* NAFRev2
* NAFRev1
* NAF1993
* NAP

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | oui                                  |

## numeroVoieEtablissement

---

Numéro dans la voie.
C'est un élément constitutif de l'adresse.
La variable est facultative.
Si l'adresse englobe plusieurs numéros dans la voie (5-7, 5 à 7...), l'information complète (5-7) ou (5 à 7) figure en complément d'adresse et le premier des numéros (5 dans l'exemple) est porté dans la variable numeroVoieEtablissement.

**Type**

Non-historisé. Texte de longueur 9, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## numeroVoie2Etablissement

---

Numéro dans la voie de l'adresse secondaire.
Dans le cas où l'établissement dispose d'une entrée secondaire, c'est un élément facultatif constitutif de l'adresse secondaire. Si l'adresse secondaire englobe plusieurs numéros dans la voie (5-7, 5 à 7...), l'information complète (5-7) ou (5 à 7) figure en complément d'adresse et le premier des numéros (5 dans l'exemple) est porté dans la variable numeroVoie2Etablissement.

**Type**

Texte de longueur 4. La variable n'est plus gérée, toujours  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## statutDiffusionEtablissement

---

Statut de diffusion de l'établissement.
Tous les établissements diffusibles ont le statut de diffusion à "O".
Les établissements ayant fait l'objet d'une demande d'opposition ont le statut de diffusion à "P" pour diffusion partielle.

**Type**

Non-historisé. Liste de codes de longueur 1 :

* O : Établissement diffusible
* P : Établissement en diffusion partielle

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## trancheEffectifsEtablissement

---

Tranche d'effectif salarié de l'établissement.
Il s'agit d'une variable statistique mise à jour une fois par an.
Sa valeur est calculée à partir des données connues au 31 décembre de l’année millésime **N** (anneeEffectifsEtablissement) et diffusée l’année  **N+2** , généralement à l’automne.

**Type**

Non-historisé. Liste de codes de longueur 2 :

* NN : Établissement non-employeur ou présumé non-employeur (faute de déclaration reçue)
* 00 : 0 salarié (n'ayant pas d'effectif au 31/12 mais ayant employé des salariés au cours de l'année N)
* 01 : 1 ou 2 salariés
* 02 : 3 à 5 salariés
* 03 : 6 à 9 salariés
* 11 : 10 à 19 salariés
* 12 : 20 à 49 salariés
* 21 : 50 à 99 salariés
* 22 : 100 à 199 salariés
* 31 : 200 à 249 salariés
* 32 : 250 à 499 salariés
* 41 : 500 à 999 salariés
* 42 : 1 000 à 1 999 salariés
* 51 : 2 000 à 4 999 salariés
* 52 : 5 000 à 9 999 salariés
* 53 : 10 000 salariés et plus

**Exemples**

Les données connues au **31-12-2023** sont intégrées à la base Sirene à l’automne  **2025** . Pas de déclaration en **2023** ➔ trancheEffectifsEtablissement =  **NN** . Déclaration d’absence d’effectif en **2023** ➔ trancheEffectifsEtablissement =  **NN** . Déclaration d’absence d’effectif au **31 décembre 2023** mais effectifs déclarés au cours de l’année **2023** ➔ trancheEffectifsEtablissement =  **00** .

**Avertissement**

Les variables trancheEffectifsEtablissement et caractereEmployeurEtablissement ne sont pas corrélées car elles n’ont pas le même processus d’élaboration (source et calcul).

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## typeVoieEtablissement

---

Type de voie de l'adresse.
C'est un élément constitutif de l'adresse.
La variable est facultative.
Les abréviations anciennes des données issues du répertoire Sirene 3 cohabitent avec les nouveaux libellés issus de la Base Adresse Nationale.

**Type**

Non-historisé. Texte de longueur 30, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

Abréviations anciennes issues du répertoire Sirene 3 (non exhaustif) :

* ACH : Ancien chemin
* AER : Aéroport
* AIRE : Aire
* ALL : Allée
* ART : Ancienne route
* AV : Avenue
* AVE : Avenue
* BASE : Base
* BD : Boulevard
* BRG : Bourg
* CAMI : Cami
* CAR : Carrefour
* CC : Chemin communal
* CD : Chemin départemental
* CF : Chemin forestier
* CHE : Chemin
* CHEM : Cheminement
* CHL : Chalet
* CHP : Champs
* CHS : Chaussée
* CHT : Château
* CHV : Chemin vicinal
* CITE : Cité
* CLOS : Clos
* COIN : Coin
* COR : Corniche
* COTE : Cote
* COUR : Cour
* CR : Chemin rural
* CRS : Cours
* DOM : Domaine
* DSC : Descente
* ECA : Ecart
* ESP : Esplanade
* ESPA : Espace
* FBG : Faubourg
* FG : Faubourg
* FON : Fontaine
* FRM : Ferme
* GARE : Gare
* GPL : Grand-place
* GR : Grande Rue
* HAB : Habitation
* HAM : Hameau
* HLE : Halle
* HLM : Habitation à loyer modéré
* HOT : Hôtel
* ILOT : Ilôt
* IMP : Impasse
* JARD : Jardin
* LD : Lieu dit
* LDT : Lieu-dit
* LOT : Lotissement
* MAR : Marché
* MTE : Montée
* PAE : Parc d’activités économiques
* PARC : Parc
* PAS : Passage
* PL : Place
* PLAN : Plan
* PLN : Plaine
* PLT : Plateau
* PONT : Pont
* PORT : Port
* PRO : Promenade
* PROM : Promenade
* PRV : Parvis
* QRT : Quartier
* QUA : Quartier
* QUAI : Quai
* RD : Route départementale
* RES : Résidence
* RLE : Ruelle
* ROC : Rocade
* RPT : Rond Point
* RTE : Route
* RUE : Rue
* SEN : Sente - Sentier
* SQ : Square
* STDE : Stade
* TOUR : Tour
* TPL : Terre-plein
* TRA : Traverse
* VALL : Vallée
* VC : Voie communale
* VCHE : Vieux chemin
* VIL : Ville
* VLA : Villa
* VLGE : Village
* VOIE : Voie
* VTE : Vieille route
* ZA : Zone artisanale
* ZAC : Zone d'aménagement concerté
* ZAD : Zone d'aménagement différé
* ZI : Zone industrielle
* ZONE : Zone

Nouveaux libellés issus de la Base Adresse Nationale (non exhaustif) :

* AERODROME
* AEROGARE
* AGGLOMERATION
* ALLEE
* ALLEES
* ANCIEN CHEMIN
* ANCIENNE ROUTE
* ANGLE
* ARCADE
* AUTOROUTE
* AVENUE
* BARRIERE
* BASSIN
* BERGE
* BOULEVARD
* BOURG
* BRETELLE
* CALL
* CALLADA
* CALLE
* CAMIN
* CAMPING
* CANAL
* CARREFOUR
* CARRIERA
* CARRIERE
* CASERNE
* CENTRE
* CHALET
* CHAMP
* CHASSE
* CHATEAU
* CHAUSSEE
* CHEMIN
* CHEMIN COMMUNAL
* CHEMIN DEPARTEMENTAL
* CHEMIN FORESTIER
* CHEMIN RURAL
* CHEMIN VICINAL
* CHEMINEMENT
* CONTOUR
* CORNICHE
* CORON
* COULOIR
* COURS
* COURSIVE
* CROIX
* DARSE
* DESCENTE
* DEVIATION
* DIGUE
* DOMAINE
* DRAILLE
* ECART
* ECLUSE
* EMBRANCHEMENT
* EMPLACEMENT
* ENCLAVE
* ENCLOS
* ESCALIER
* ESPACE
* ESPLANADE
* ETANG
* FAUBOURG
* FERME
* FOND
* FONTAINE
* FORET
* FOSSE
* GALERIE
* GRAND BOULEVARD
* GRAND PLACE
* GRANDE PLACE
* GRANDE RUE
* GREVE
* HABITATION
* HALAGE
* HALLE
* HAMEAU
* HAUTEUR
* HIPPODROME
* IMPASSE
* JARDIN
* JETEE
* LEVEE
* LICES
* LICES
* LIEU DIT
* LIGNE
* LOTISSEMENT
* MAISON
* MARCHE
* MARINA
* MONTEE
* MORNE
* NOUVELLE ROUTE
* PARKING
* PARVIS
* PASSAGE
* PASSE
* PASSERELLE
* PETIT CHEMIN
* PETITE ALLEE
* PETITE AVENUE
* PETITE ROUTE
* PETITE RUE
* PHARE
* PISTE
* PLACA
* PLACE
* PLACETTE
* PLACIS
* PLAGE
* PLAINE
* PLATEAU
* POINTE
* PORCHE
* PORTE
* PORTIQUE
* POSTE
* POTERNE
* PROMENADE
* QUARTIER
* RACCOURCI
* RAMPE
* RAVINE
* REMPART
* RESIDENCE
* ROCADE
* ROND POINT
* ROND-POINT
* ROTONDE
* ROUTE
* RUELLE
* RUELLETTE
* RUET
* RUETTE
* RUISSEAU
* SENTE
* SENTIER
* SQUARE
* STADE
* TERRAIN
* TERRASSE
* TERRE
* TERRE-PLEIN
* TERTRE
* TRABOULE
* TRAVERSE
* TUNNEL
* VALLEE
* VALLON
* VENELLE
* VIADUC
* VIEILLE ROUTE
* VIEUX CHEMIN
* VILLA
* VILLAGE
* VILLE
* VOIE COMMUNALE
* VOIRIE
* VOUTE
* VOYEUL
* ZONE ARTISANALE
* ZONE DAMENAGEMENT CONCERTE
* ZONE DAMENAGEMENT DIFFERE
* ZONE INDUSTRIELLE

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | non                                  |

## typeVoie2Etablissement

---

Type de voie de l'adresse secondaire.
Dans le cas où l'établissement dispose d'une entrée secondaire, c'est un élément constitutif de l'adresse.
La variable est facultative.

**Type**

Texte de longueur 4. La variable n'est plus gérée, toujours  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | Jusqu'à Sirene 4          | non                                  |

## dateDebut

---

Date de début d'une période de l'historique d'un établissement.
Une période est un intervalle de temps au cours duquel aucune variable historisée n'est modifiée.
La date 1900-01-01 signifie : date non déterminée. dateDebut peut-être vide, uniquement pour les unités légales purgées.
La date de début de la période la plus ancienne ne correspond pas obligatoirement à la date de création de l'établissement, certaines variables historisées pouvant posséder des dates de début soit au 1900-01-01, soit antérieures à la date d'ouverture.

**Type**

Date, de longueur 10, format AAAA-MM-JJ, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| non                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | oui                        | oui                                  |

## dateFin

---

Date de fin d'une période de l'historique d'un établissement.
Une période est un intervalle de temps au cours duquel aucune variable historisée n'est modifiée.
La date de fin est calculée, elle est égale à la veille de la date de début de la période suivante dans l'ordre chronologique.
Si la date de fin de la période est  *null* , la période correspond à la situation courante de l'établissement.

**Type**

Date, de longueur 10, format AAAA-MM-JJ, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| non                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | non                        | oui                                  |

## Les variables préfixées "changement"

---

Chaque variable historisée est accompagnée d'une variable signalant, pour chaque période, si elle a été modifiée ( *true* ) ou non ( *false* ), c'est à dire si elle est (seule ou avec d'autres variables) à l'origine de la création de la période :

* changementActivitePrincipaleEtablissement
* changementCaractereEmployeurEtablissement
* changementDenominationUsuelleEtablissement
* changementEnseigneEtablissement
* changementEtatAdministratifEtablissement

A l'exception de la première période de l'historique (la plus ancienne), il y a toujours au moins une variable de changement à *true* à chaque période.

**Type**

Booléen : *true* ou  *false* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| non                                            | non                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | non                                | non                        | oui                                  |
