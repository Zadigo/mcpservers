
# Unité légale

## Siren

---

Le numéro Siren est le numéro d’identitification de l’unité légale, composé de 9 chiffres.

**Règles de gestion**

Il est attribué par l’Insee à toute personne physique ou morale « soit à l’occasion des demandes d’immatriculation au registre du commerce et des sociétés ou des déclarations effectuées au répertoire des métiers, soit à la demande d’administrations » (article R123-224 du code de commerce).
Les entrepreneurs individuels, ou personnes physiques, conservent le même numéro Siren jusqu’à leur décès.
Les sociétés, ou personnes morales, perdent la personnalité juridique au moment de la cessation de l’activité de l’entreprise. Si l’activité devait reprendre ultérieurement, un nouveau numéro Siren sera attribué.
Les numéros d’identification sont uniques : lorsqu’un numéro Siren a été attribué, il ne peut pas être réutilisé et attribué à une nouvelle unité légale, même lorsque l’activité a cessé.

**Historique**

Même si la mise en place du répertoire Sirene remonte à 1973, toutes les unités légales, y compris celles créées avant cette date, disposent d’un numéro Siren pour le secteur privé non agricole.
En 1983, le champ du répertoire Sirene et l’obligation d’immatriculation ont été étendus aux institutions et services de l’État et aux collectivités territoriales.
En 1993, le champ du répertoire Sirene et l’obligation d’immatriculation ont été étendus au secteur privé agricole.

**Type**

Non-historisé. Numérique de longueur 9.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | oui                        | oui                                  |

## activitePrincipaleNAF25UniteLegale

---

Cette variable contient le code APE de l'unité légale en nomenclature NAF25.
Elle est renseignée pour les unités actives (hormis les mises en sommeil), ou récemment cessées.
Elle est présente à titre d'information, et disparaîtra lorsque la NAF25 deviendra la nomenclature officielle, donc au 01/01/2027. A partir de cette date, on pourra alors retrouver le code NAF25 dans la variable  *activitePrincipaleUniteLegale* .
Les personnes qui souhaitent demander une correction de leur code NAF25 peuvent le faire via un site de rectification du code APE.

**Type**

Non-historisé. Liste de codes de longueur 6, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## activitePrincipaleUniteLegale

---

Lors de son inscription au répertoire, l’Insee attribue à toute unité légale un code dit « APEN » (Activité Principale de l'ENtreprise) sur la base de la description de l’activité principale faite par le déclarant.
Ce code est modifiable au cours de la vie de l’unité légale en fonction des déclarations de l’exploitant.
Pour chaque unité légale, il existe à un instant donné un seul code APEN.

La variable nomenclatureActivitePrincipaleUniteLegale indique à quelle nomenclature d'activité appartient le code.
Toutes les unités légales actives ont un code d'activité principale appartenant à la nomenclature la plus récente (actuellement la NAF rév. 2).
Les unités légales fermées ont un code d'activité principale appartenant à la nomenclature en vigueur à la date de prise en compte de leur fermeture.

Les personnes morales ont la possibilité de s'immatriculer sans activité (elles déclarent alors leur commencement d'activité dans un second temps, dans les 12 mois suivant la création) : dans ce cas, l'Insee attribue le code APEN 00.00Z jusqu'à la prise d'activité.
L'APE peut être à *null* (cas des unités purgées, première date de début de l'APE postérieure à la première date de début d'une autre variable historisée).

**Historique**

Le code APE est historisé depuis le 01/01/2005.

La règle d’historisation des données d’activité est la suivante :

* Pour les entreprises cessées avant le 31/12/2004, seul le dernier code activité connu figure, dans la nomenclature en vigueur à la date de fermeture.
* Pour les entreprises actives après le 01/01/2005 et cessées avant le 31/12/2007, l’historique des codes attribués sur la période est disponible.
* Pour les entreprises actives après le 01/01/2005 et toujours actives le 01/01/2008, l’historique intègre le changement de nomenclature.
* Pour les entreprises créées après le 01/01/2008, l’historique comprend les modifications apportées au cours de la vie de l’entreprise.

**Type**

Historisé. Liste de codes de longueur 6, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## anneeCategorieEntreprise

---

C'est l'année de validité correspondant à la catégorie d'entreprise diffusée.
La mise à jour de la catégorie d’entreprise est annuelle (en juillet N+2 pour l’année N).

**Type**

Non-historisé. Date, de longueur 4, format AAAA, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## anneeEffectifsUniteLegale

---

Année de validité de la tranche d'effectif salarié de l'unité légale.
La mise à jour des tranches d'effectifs est annuelle (automne).
Pour les unités dont la tranche d’effectifs est renseignée, l’année de validité correspondante est l’année millésime N (voir trancheEffectifsUniteLegale).
Il n'y a jamais plus d’un seul millésime présent dans la base Sirene.

**Type**

Non-historisé. Date, de longueur 4, format AAAA, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## caractereEmployeurUniteLegale

---

Caractère employeur de l'unité légale.

**Type**

La variable n'est plus gérée, toujours  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| Jusqu'à Sirene 4                              | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| Jusqu'à Sirene 4        | Jusqu'à Sirene 4                  | non                        | non                                  |

## categorieEntreprise

---

La catégorie d'entreprise de l'unité légale est une variable statistique calculée par l'Insee : ce n'est donc pas une variable intrinsèque du répertoire Sirene.
Lorsque l’unité légale appartient à un [groupe](https://www.insee.fr/fr/metadonnees/definition/c1041), la catégorie d'entreprise est [calculée au niveau du groupe](https://www.insee.fr/fr/metadonnees/definition/c1057) auquel appartient l’unité légale.

La variable categorieEntreprise ne peut pas être modifiée à la demande des entreprises.
Elle n’est pas utilisable à des fins administratives.

La variable categorieEntreprise est associée à une année de validité (anneeCategorieEntreprise).
Elle est mise à jour une fois par an (en juillet N+2 pour l’année N).

**Type**

Non-historisé. Liste de codes de longueur 3, ou *null* :

* PME : petite ou moyenne entreprise
* ETI : entreprise de taille intermédiaire
* GE : grande entreprise

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## categorieJuridiqueUniteLegale

---

La catégorie juridique de l'unité légale est un attribut des unités légales.
Pour une personne physique, elle vaut toujours 1000, que la personne soit artisan, commerçant, profession libérale, agriculteur ou autre, et ne peut changer.
Pour les personnes morales, la catégorie juridique est susceptible d'évoluer au cours de la vie de l'entreprise.
Le code est attribué selon la [nomenclature](https://www.insee.fr/fr/information/2028129) en vigueur, mais peut être à *null* (cas des unités purgées notamment).

**Type**

Historisé. Liste de codes de longueur 4, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## dateCreationUniteLegale

---

La date de création de l'unité légale correspond à la date déclarée lors du dépôt des formalités de création.
Pour les unités purgées (unitePurgeeUniteLegale=true) : si la date de création est au 01/01/1900 dans Sirene, la date est forcée à  *null* .
Dans tous les autres cas, la date de création n'est jamais à  *null* .
Si elle est non renseignée, elle sera au 01/01/1900.

La date de création ne correspond pas obligatoirement à dateDebut de la première période de l'unité légale.
Certaines variables historisées peuvent posséder des dates de début soit au 01/01/1900, soit antérieures à la date de création.

**Type**

Non-historisé. Format date de longueur 10 (AAAA-MM-JJ), ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## dateDernierTraitementUniteLegale

---

Date de la dernière modification d'une variable de niveau unité légale, qu'elle soit historisée ou non.
Cette date peut concerner des mises à jour de données du répertoire Sirene qui ne sont pas diffusées.

**Type**

Non-historisé. Format date, de longueur 23 (AAAA-MM-JJTHH:MM:SS.MMM) ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## denominationUniteLegale

---

Cette variable désigne la raison sociale pour les personnes morales. Il s'agit du nom sous lequel est déclarée l'unité légale.
Cette variable est à *null* pour les personnes physiques.
La dénomination peut parfois contenir la mention de la forme de la société (SA, SAS, SARL, etc.).
Elle peut contenir des caractères spéciaux tel que - & + @ ! ? * ° . % : # | (liste non exhaustive).

**Type**

Historisé. Format texte, de longueur 130, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## denominationUsuelle1UniteLegale, denominationUsuelle2UniteLegale, denominationUsuelle3UniteLegale

---

Ces variables facultatives désigne le nom (ou les noms) commercial, sous lequel l'entreprise est connue du grand public.
Ces éléments facultatifs d'identification de l'entreprise ont été enregistrés au niveau unité légale avant l'application de la norme d'échanges CFE de 2008.
À partir de la norme 2008, le nom commercial est enregistré au niveau de l'établissement sur un seul champ : denominationUsuelleEtablissement.
Les 3 variables sont historisées avec une seule indicatrice de changement pour les trois variables.

**Type**

Historisé. Format texte, de longueur 70, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## economieSocialeSolidaireUniteLegale

---

Cette variable indique si l'entreprise appartient au champ de l'économie sociale et solidaire.
La loi n° 2014-856 du 31 juillet 2014 définit officiellement le périmètre de l'économie sociale et solidaire (ESS). Celle-ci comprend les quatre familles traditionnelles en raison de leur régime juridique (associations, fondations, coopératives et mutuelles) et inclut une nouvelle catégorie, les entreprises de l'ESS, adhérant aux mêmes principes :

* poursuivre un but social autre que le seul partage des bénéfices ;
* un caractère lucratif encadré (notamment des bénéfices majoritairement consacrés au maintien et au développement de l'activité) ;
* une gouvernance démocratique et participative.

**Type**

Historisé. Liste de codes de longueur 1, ou *null* :

* O : l'entreprise appartient au champ de l'économie sociale et solidaire ;
* N : l'entreprise n'appartient pas au champ de l'économie sociale et solidaire.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## etatAdministratifUniteLegale

---

État administratif de l'unité légale.

Le passage à l'état « Cessée » découle de la prise en compte d'une déclaration de cessation administrative :

* Pour les personnes morales, cela signifie disparition de la personne morale : l'état administratif "Cessée" est *a priori* irréversible. Cependant, il existe actuellement dans la base un certain nombre d'unités légales personnes morales avec un historique d'état présentant un état cessé entre deux périodes à l'état actif.
* Pour les personnes physiques, cela signifie une cessation totale d'activité, décidée ou contrainte (décès, faillite). Hormis en cas de décès, la personne physique est susceptible d'être réactivée (même siren), en cas de reprise d'activité (identique ou non), sans condition de délai.

En règle générale, la première période d'historique d'une unité légale correspond à un etatAdministratifUniteLegale égal à « Active ».
Toutefois, l'état administratif peut être à  *null* , dans le cas d'une première date de début de l'état postérieure à la première date de début d'une autre variable historisée.

**Type**

Historisé. Liste de codes de longueur 1, ou *null* :

* A : l'entreprise est administrativement active (même mise en sommeil, c'est à dire avec tous ses établissements fermés) ;
* C : l'entreprise est administrativement cessée.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## identifiantAssociationUniteLegale

---

Numéro au Répertoire National des Associations (RNA).
Lors de sa déclaration en préfecture, l'association reçoit automatiquement un numéro d'inscription au RNA.
Elle doit en outre demander son immatriculation au répertoire Sirene lorsqu'elle souhaite demander des subventions auprès de l'État ou des collectivités territoriales, lorsqu'elle emploie des salariés ou lorsqu'elle exerce des activités qui conduisent au paiement de la TVA ou de l'impôt sur les sociétés.
Le RNA est le fichier national, géré par le ministère de l'Intérieur, qui recense l'ensemble des informations sur les associations.

**Type**

Non-historisé. Texte de longueur 10, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## nicSiegeUniteLegale

---

Numéro interne de classement (Nic) de l'établissement siège de l'unité légale.

Toutes les unités légales ont un établissement siège :

* Pour les personnes morales, il s'agit d'une donnée juridique. Le transfert du siège d'un établissement à un autre fait l'objet d'une formalité et entraîne le changement de nicSiegeUniteLegale.
* Pour les personnes physiques, le siège n'a pas de réalité juridique, mais le répertoire calque la structure des personnes physiques sur celle des personnes morales, et attribue la qualité de siège au premier établissement créé : le transfert de siège est géré à partir des formalités de création, transfert ou fermeture d'établissement(s).

Le Nic du siège peut être à *null* sur une période mais, en règle générale, pas sur l'ensemble de l'historique (cas des unités purgées, première date de début du Nic postérieure à la première date de début d'une autre variable historisée).

**Type**

Historisé. Texte de longueur 5 (numérique), ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## nombrePeriodesUniteLegale

---

Nombre de périodes de l'unité légale.
Chaque période correspond à un intervalle de temps pendant lequel aucune des variables **historisées** de l'unité légale n'est modifiée.
Les dates de ces périodes sont des dates d'effet (et non des dates de traitement).

**Type**

Non-historisé. Longueur 2, numérique.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| non                                            | oui                                         | non                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## nomenclatureActivitePrincipaleUniteLegale

---

Cette variable indique la nomenclature d'activité correspondant au code de l'activité principale de l'unité légale, indiqué par la variable activitePrincipaleUniteLegale.
La variable nomenclatureActivitePrincipaleUniteLegale est à *null* si la variable activitePrincipaleUniteLegale est à  *null* .
La nomenclature en vigueur est la Naf Rév.2, et ce depuis le 01 Janvier 2008. Chaque code comporte 4 chiffres et une lettre.

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
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## nomUniteLegale

---

Nom de naissance de la personnes physique.
Cette variable est à *null* pour les personnes morales.
Elle peut être à *null* pour une personne physique (cas des unités purgées, première date de début du nom postérieure à la première date de début d'une autre variable historisée).

**Type**

Historisé. Texte de longueur 100, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## nomUsageUniteLegale

---

Le nom d'usage est celui que la personne physique a choisi d'utiliser.
Cette variable est à *null* pour les personnes morales.
Le nom peut être à *null* pour une personne physique (cas des unités purgées, première date de début du nom postérieure à la première date de début d'une autre variable historisée).

**Type**

Historisé. Texte de longueur 100, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## prenom1UniteLegale à prenom4UniteLegale

---

Les variables prenom1UniteLegale à prenom4UniteLegale sont les prénoms déclarés pour une personne physique.
Ces variables sont à *null* pour les personnes morales.
Toute personne physique sera identifiée au minimum par son nom de naissance et son premier prénom. Toutefois, il existe des personnes physiques pour lesquelles le nom est renseigné alors que les 4 prénoms sont à  *null* .
Les prenom1UniteLegale à prenom4UniteLegale peuvent contenir des *, qui ne sont pas significatifs.

**Type**

Non-historisé. Texte de longueur 20, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## prenomUsuelUniteLegale

---

Le prénom usuel est le prénom par lequel une personne physique choisit de se faire appeler dans la vie courante, parmi l'ensemble de ceux qui lui ont été donnés à sa naissance et qui sont inscrits à l'état civil.
Cette variable n'est plus gérée, et toujours égale au prenom1UniteLegale.
Cette variable est à *null* pour les personnes morales.

**Type**

Non-historisé. Texte de longueur 20, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## pseudonymeUniteLegale

---

Le pseudonyme correspond au nom qu'une personne physique utilise pour se désigner dans l'exercice de son activité, généralement littéraire ou artistique.

**Type**

Non-historisé. Texte de longueur 100, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## sexeUniteLegale

---

Caractère féminin ou masculin de la personne physique.
Cette variable est à *null* pour les personnes morales, ainsi que pour quelques personnes physiques.

**Type**

Non-historisé. Liste de codes de longueur 4, ou  *null* , ou [ND] si l'unité est en diffusion partielle :

* F : Féminin
* M : Masculin

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## sigleUniteLegale

---

Un sigle est une forme réduite de la raison sociale ou de la dénomination d'une personne morale ou d'un organisme public.
Il est habituellement constitué des initiales de certains des mots de la dénomination.
Afin d'en faciliter la prononciation, il arrive qu'on retienne les deux ou trois premières lettres de certains mots : il s'agit alors, au sens strict, d'un acronyme; mais l'usage a étendu à ce cas l'utilisation du terme sigle.
Cette variable est à *null* pour les personnes physiques ; facultative, elle peut également être à *null* pour les personnes morales.

**Type**

Non-historisé. Texte de longueur 20, ou  *null* , ou [ND] si l'unité est en diffusion partielle.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## societeMissionUniteLegale

---

Cette variable indique si l'entreprise appartient au champ des sociétés à mission.
L'article 176 de la loi du 22 mai 2019 relative à la croissance et la transformation des entreprises, dite loi Pacte, introduit la qualité de société à mission. Il permet à une société de faire publiquement état de la qualité de société à mission en précisant sa raison d'être ainsi qu’un ou plusieurs objectifs sociaux et environnementaux que la société se donne pour mission de poursuivre dans le cadre de son activité.

**Type**

Historisé. Liste de codes de longueur 1, ou *null* :

* O : l'entreprise appartient au champ des sociétés à mission ;
* N : l'entreprise n'appartient pas au champ des sociétés à mission.

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## statutDiffusionUniteLegale

---

Statut de diffusion de l'unité légale.
Toutes les unités légales diffusibles ont le statut de diffusion à "O".
Les unités légales ayant fait l'objet d'une demande d'opposition ont le statut de diffusion à "P" pour diffusion partielle.

**Type**

Non-historisé. Liste de codes de longueur 1 :

* O : Unité diffusible
* P : Unité en diffusion partielle

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## trancheEffectifsUniteLegale

---

Tranche d'effectif salarié de l'unité légale.
Il s'agit d'une variable statistique mise à jour une fois par an.
Sa valeur est calculée à partir des données connues au 31 décembre de l’année millésime **N** (anneeEffectifsUniteLegale) et diffusée l’année  **N+2** , généralement à l’automne.

**Type**

Non-historisé. Liste de codes de longueur 2 :

* NN : unité non-employeuse ou présumée non-employeuse (faute de déclaration reçue)
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

Les données connues au **31-12-2023** sont intégrées à la base Sirene à l’automne  **2025** . Pas de déclaration en **2023** ➔ trancheEffectifsUniteLegale =  **NN** . Déclaration d’absence d’effectif en **2023** ➔ trancheEffectifsUniteLegale =  **NN** . Déclaration d’absence d’effectif au **31 décembre 2023** mais effectifs déclarés au cours de l’année **2023** ➔ trancheEffectifsUniteLegale =  **00** .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## unitePurgeeUniteLegale

---

Cette variable indique si l'unité légale a été purgée.
Pour des raisons de capacité de stockage des données, les données concernant les entreprises cessées avant le 31/12/2002 ont été purgées.
La variable n'est affichée en Json que lorsqu'elle vaut  *true* , qu'on interroge les unités légales ou les établissements ; elle est toujours affichée en csv.

Pour ces unités dites purgées :

* L'état administratif est à **C** (cessée) ;
* Seules les dernières valeurs des variables de niveau Unité Légale et de niveau Établissement sont conservées ;
* En théorie, seul l'établissement siège au moment de la purge est conservé avec uniquement les dernières valeurs de cet établissement. Toutefois, pour plus de 300 unités légales purgées de la base, cette règle n'est pas respectée et ces unités ont toujours plus d'un établissement en base sans pouvoir garantir que tous les établissements ont été conservés ;
* L'indicatrice unitePurgeeUniteLegale est à  *true* .

Plus de 4 millions d'unités légales sont purgées. Plus d'une unité purgée sur quatre a une date de création indéterminée.

NB : les établissements des unités purgées sont fermés et n'ont qu'une seule période, avec dateDebut=date de début de l'état fermé si cette date est renseignée, sinon dateDebut (établissement) est à  *null* .

**Type**

Non-historisé. Booléen : *true* ou  *false* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| oui                                            | oui                                         | oui                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | non                                | non                        | non                                  |

## dateDebut

---

Date de début d'une période de l'historique d'une unité légale.
Une période est un intervalle de temps au cours duquel aucune variable historisée n'est modifiée.
La date 1900-01-01 signifie : date non déterminée.
dateDebut peut-être vide, uniquement pour les unités légales purgées.
La date de début de la période la plus ancienne ne correspond pas obligatoirement à la date de création de l'entreprise, certaines variables historisées pouvant posséder des dates de début soit au 1900-01-01, soit antérieures à la date de création.

**Type**

Date, de longueur 10, format AAAA-MM-JJ, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| non                                            | oui                                         | non                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| oui                      | oui                                | non                        | non                                  |

## dateFin

---

Date de fin d'une période de l'historique d'une unité légale. Une période est un intervalle de temps au cours duquel aucune variable historisée n'est modifiée.
La date de fin est calculée, elle est égale à la veille de la date de début de la période suivante dans l'ordre chronologique ; si la date de fin de la période est  *null* , la période correspond à la situation courante de l'unité légale.

**Type**

Date, de longueur 10, format AAAA-MM-JJ, ou  *null* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| non                                            | oui                                         | non                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | oui                                | non                        | non                                  |

## Les variables préfixées "changement"

---

Chaque variable historisée est accompagnée d'une variable signalant, pour chaque période, si elle a été modifiée ( *true* ) ou non ( *false* ), c'est à dire si elle est (seule ou avec d'autres variables) à l'origine de la création de la période :

* changementActivitePrincipaleUniteLegale
* changementCaractereEmployeurUniteLegale
* changementCategorieJuridiqueUniteLegale
* changementDenominationUniteLegale
* changementDenominationUsuelleUniteLegale
* changementEconomieSocialeSolidaireUniteLegale
* changementEtatAdministratifUniteLegale
* changementNicSiegeUniteLegale
* changementNomUniteLegale
* changementNomUsageUniteLegale
* changementSocieteMissionUniteLegale

A l'exception de la première période de l'historique (la plus ancienne), il y a toujours au moins une variable de changement à *true* à chaque période.

**Type**

Booléen : *true* ou  *false* .

**Présence de la variable selon le dessin de fichier**

| Liste constituée sur annuaire des entreprises | API Sirene 3.11-collection Unités Légales | API Sirene 3.11-collection Établissements |
| ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| non                                            | oui                                         | non                                        |

| Fichier StockUniteLegale | Fichier StockUniteLegaleHistorique | Fichier StockEtablissement | Fichier StockEtablissementHistorique |
| ------------------------ | ---------------------------------- | -------------------------- | ------------------------------------ |
| non                      | oui                                | non                        | non                                  |
