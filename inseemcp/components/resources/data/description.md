## Presentation

### French

L'API Sirene donne accès aux informations concernant les entreprises et les établissements enregistrés au répertoire interadministratif Sirene depuis sa création en 1973, y compris les unités fermées. Cet accès est permis via trois types de web-services :

* la recherche unitaire, sur unité légale ou établissement
* la recherche multicritère, sur unités légales ou établissements
* la recherche sur les liens de succession entre établissements

Les différents services interrogent l'une des trois collections (types de donnée) suivantes :

* collection Unités Légales
* collection Établissements
* collection Liens de succession

Ce service de l'Insee permet de :

* créer et de mettre à jour ses propres listes
* rechercher les données clés d'une entreprise
* valoriser ses fichiers clients ou fournisseurs
* éviter de devoir recopier en local les données du répertoire Sirene et d'intégrer ses mises à jour

Les données Sirene interrogées sont mises à jour quotidiennement dans la nuit et intègrent les mises à jour de la veille.

**Contenu du répertoire Sirene à la date d'aujourd'hui**

Institué par les articles [R. 123-220 à R. 123-234](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046073477) du code de commerce, le Répertoire National d'identification des entreprises et des établissements concerne les unités implantées en métropole, dans les DOM et dans les collectivités d'Outre-Mer de Saint Pierre et Miquelon, Saint Barthélémy et Saint Martin. La gestion de ce répertoire est confiée à l'INSEE. Elle est effectuée à travers le système Sirene (Système Informatique pour le Répertoire des ENtreprises et des Etablissements). L'INSEE est chargé d'identifier :

* les entrepreneurs individuels exerçant de manière indépendante une profession non salariée (exemple : un commerçant, un médecin) ;
* les personnes morales de droit privé ou de droit public soumises au droit commercial ;
* les institutions et services de l'État et les collectivités territoriales, ainsi que tous leurs établissements ;
* les associations dans certains cas.
Sont donc inscrites au répertoire tous les entrepreneurs individuels ou les personnes morales :

* immatriculées au Registre du Commerce et des Sociétés ;
* immatriculées au Répertoire des Métiers ;
* employant du personnel salarié (à l'exception des particuliers employeurs) ;
* soumises à des obligations fiscales ;
* bénéficiaires de transferts financiers publics.

Toutes les mises à jour d'entreprises et d'établissements (créations, modifications, cessations) enregistrés dans Sirene proviennent des informations déclaratives des entreprises auprès du Guichet Unique et de certains Centres de Formalités des Entreprises (CFE).

**Historique du répertoire Sirene**

Le décret n°73-314 du 14 mars 1973 a confié à l'Insee la tenue du répertoire Sirene.

Le décret n°83-121 du 17 février 1983 a étendu les données du répertoire Sirene :

* aux personnes morales de droit public soumises au droit commercial (entreprises publiques) ;
* aux personnes morales (ou organismes assimilés comme telles) soumises au droit administratif (comme les institutions et services de l'État, les collectivités territoriales, etc.).

Le répertoire Sirene contient toutes les entreprises actives à la création du répertoire et celles créées depuis. Pour les personnes morales de droit public et les administrations, le répertoire est exhaustif depuis 1983. L'intégration complète du secteur privé agricole date de 1993.

**Diffusion du répertoire Sirene en open data**

Suite à la loi n° 2016-1321 du 7 octobre 2016 pour une république numérique, et s'agissant de la mise à disposition du répertoire Sirene, l'Insee a créé deux canaux de diffusion :

Les API Sirene, qui permettent après création d'un compte, une exploration complète des données, manuellement ou automatiquement. Les valeurs courantes et, le cas échéant, les valeurs historiques des variables sont disponibles ;

Les fichiers stock, mis à jour chaque début de mois, qui permettent le téléchargement d'une copie complète de la base Sirene sous forme de fichiers disponibles sur data.gouv.fr :

* le fichier stock des entreprises (entreprises actives et cessées dans leur état courant au répertoire) ;
* le fichier stock des valeurs historisées des entreprises ;
* le fichier stock des établissements (établissements actifs et fermés dans leur état courant au répertoire) ;
* le fichier stock des valeurs historisées des établissements ;
* le fichier stock des liens de succession des établissements.

Via L'Annuaire des Entreprises, il est également possible d'accéder simplement aux informations du répertoire Sirene, sans ouverture de compte, notamment la recherche d'une entreprise, d'un établissement ou encore la constitution d'une liste d'établissements selon différents critères de recherche.

**Les données historisées**

Sirene conserve tout l'historique des variables dans les cas suivants :

* les informations figurent dans le code de commerce comme, par exemple, la dénomination ;
* les informations sont utiles au sens de l'utilisation statistique comme, par exemple, l'activité principale.

Quand une variable est historisée au niveau de l'unité légale, si son pendant existe au niveau de l'établissement, il est également historisé. C'est ainsi qu'on dispose de :

* l'historique de l'activité principale de l'unité légale ;
* l'historique de l'activité principale de chacun des établissements qui dépendent de cette unité légale.

L'historisation des variables du répertoire Sirene a été mise en oeuvre à partir de 2005.

**Variables historisées au niveau de l'unité légale**

Les variables historisées au niveau de l'unité légale sont les suivantes :

* La dénomination pour les personnes morales ;
* Le nom de naissance pour les personnes physiques ;
* Le nom d'usage pour les personnes physiques ;
* La dénomination usuelle ;
* La catégorie juridique ;
* L'état ;
* Le Nic du siège ;
* L'activité principale ;
* L'appartenance à l'économie sociale et solidaire (ESS) ;
* L'appartenance au champ des sociétés à mission.

**Variables historisées au niveau de l'établissement**
Les variables historisées au niveau de l'établissement sont les suivantes :

* L'enseigne ;
* La dénomination usuelle ;
* L'activité principale de l'établissement ;
* La nomenclature de l'activité principale de l'établissement ;
* L'état ;
* Le caractère employeur de l'établissement.

**Définition de l'historique**

L'historique se présente comme une liste de périodes, distinctes les unes des autres. Une période est définie par le Siren ou le Siret (Siren+Nic), la date de début et la date de fin. La date de fin d'une période correspond à la veille du début de la période suivante. Au cours d'une période, toutes les valeurs des variables historisées sont constantes. Dans les fichiers stock, pour chaque Siren ou Siret, il y a autant de lignes que de périodes. Quel que soit le nombre de périodes, les fichiers ont toujours la même structure. Pour chaque variable historisée, une indicatrice de changement donne l'information sur une modification par rapport à la période précédente (si l'indicatrice est à true, il y a eu changement par rapport à la période précédente).

La date 1900-01-01 correspond dans la très grande majorité des cas à une date manquante, comme la valeur null. Les dates de début et de fin sont issues des historiques des variables concernées et par conséquent le résultat de gestions successives depuis la création du répertoire Sirene. La cohérence entre les dates des différentes variables n'est pas obligatoirement assurée. En conséquence, les premières périodes peuvent avoir des valeurs de variables historisées à null juste par construction. Les dates de ces périodes sont des dates d'effet (par opposition aux dates de traitement).

**Les unités disponibles aujourd'hui**

Sont disponibles à tout public :

* Les unités légales et établissements de diffusion publique (accessibles par les fichiers fournis par l'Insee dont ceux qui sont accessibles sur data.gouv.fr, par l'avis de situation au répertoire Sirene, par l'Annuaire des Entreprises) ;
* Les unités légales et établissements en diffusion partielle, pour les variables qui ne sont pas concernées par la diffusion partielle ;
* Les unités légales dont les établissements ont été purgés ainsi que les établissements siège de ces unités à la date de la purge.

Cas des unités légales doublon : une même unité légale peut être identifiée dans Sirene avec 2 numéros siren différents pendant quelques temps. Les services web permettent la redirection entre l'unité qui a été créée à tort et celle qui a été doublonnée, pour les doublons qui ont été détectés.

Sont disponibles suivant droit d'accès :

* Les unités légales et établissements dépendant de l'article A123-96 du code de commerce (accessibles aux administrations ou organismes assimilés) ;
* Les unités et établissements Défense (accessibles sur autorisation du Ministère de la Défense) ;
* Les unités légales et établissements en diffusion partielle, pour les variables qui sont concernées par la diffusion partielle.

**Les liens de succession (API Sirene et Data.gouv uniquement)**

La construction d'un lien de succession entre établissements repose sur le traitement d'une déclaration. En effet, lorsqu'un établissement est vendu (ou acheté), la norme de déclaration prévoit que la destination (ou l'origine) soit indiquée. Pour cela, il est demandé de fournir la dénomination, voire le numéro Siren, de l'acquéreur (ou du vendeur). Un lien de succession est également établi dans le cadre des déclarations de transferts d'établissements au sein de la même unité légale. Pour les entreprises des grands groupes, qui sont plus souvent concernées par des restructurations que les autres entreprises, il arrive que le lien soit fourni par l'entreprise.

Au cours de sa vie, un établissement peut avoir plusieurs prédécesseurs, voire plusieurs successeurs. En effet, un établissement peut transférer une partie de ses activités sans pour autant fermer. Lors d'une succession, un établissement peut avoir un ou plusieurs successeurs à la même date. Idem pour les prédécesseurs.

**Les unités en diffusion partielle**

Toutes les unités légales et tous les établissements diffusibles ont le statut de diffusion à "O".

Les informations d'identification de personnes physiques ainsi que les informations de localisation des établissements - hormis la commune - ne sont pas diffusées pour les unités ayant fait l'objet d'une demande d'opposition et qui ont donc le statut de diffusion à "P" pour diffusion partielle. La valeur "[ND]" (Non Diffusée) remplace alors les données non diffusées.

Depuis le 21 mars 2023, la modalité non diffusible "N" n'est plus disponible, et le statut de diffusion des unités antérieurement non diffusibles "N" a été automatiquement passé à "P". Il n'y a donc plus d'unités non diffusibles "N" dans la base Sirene.

Activité principale exercée (APE)
Dans le cadre de sa mission de gestion du répertoire Sirene, l'Insee attribue un code dit activité principale exercée (APE) à partir de la nomenclature d'activités française (NAF) définie par décret. L'APE est déterminée séparément pour l'entreprise dans son ensemble (fonction de la ventilation des activités de l'entreprise) et pour chacun des établissements. Ce code est constitué de quatre chiffres et une lettre d'après la nomenclature actuellement en vigueur. Il est attribué à des fins statistiques et ne peut constituer qu'un élément d'appréciation d'une réglementation ou d'un contrat.

## Définitions

**Catégorie juridique**

La catégorie juridique décrit le statut juridique de l'entreprise. Elle est déterminée, pour les personnes morales, à partir de la déclaration remplie lors de la création. Pour les organismes publics, la catégorie juridique est déterminée à partir du texte réglementaire à l'origine de la création.

La nomenclature interadministrative des catégories juridiques sert de référence commune à toutes les administrations, aux organismes associés au répertoire Sirene et aux procédures des centres de formalités des entreprises.

Elle est organisée selon trois niveaux hiérarchiques successifs : agrégé, intermédiaire et détaillé.

Dans la base de données Sirene®, la nature juridique correspond uniquement à la catégorie juridique pour les personnes morales.

**Les catégories juridiques**

**Cessation d'une entreprise**
La cessation d'entreprise est pris dans le sens large d'entreprises qui cessent leur activité et cessent d'exister juridiquement. La cessation d'une entreprise correspond à la fin de vie d'une entité juridique. Dans tous les cas, une entreprise qui cesse aura toujours l'ensemble de ses établissements fermés.

L'identifiant Siren est lié à l'existence juridique de l'entreprise et cesse avec elle. Pour tenir compte à la fois des impératifs juridiques et des réalités économiques, il existe deux catégories de cessations :

la cessation juridique de l'entreprise : une entreprise est cessée en cas de dissolution s'il s'agit d'une personne morale, et en cas de décès ou lors de la cessation de toute activité s'il s'agit d'un entrepreneur individuel ;
la cessation d'activité de l'entreprise : l'entreprise cesse son activité. On parle aussi de cessation économique lorsque tous les établissements de l'entreprise sont fermés.
**Code officiel géographique**
Le code officiel géographique rassemble les codes et libellés des communes, des cantons, des arrondissements, des départements, des régions, des collectivités d'outre-mer, des pays et territoires étrangers.

Le code officiel géographique.

**Création d'une entreprise**
La création d'une entreprise correspond à la création d'une nouvelle personne juridique et à l'attribution d'un nouveau Siren. La création d'entreprise est toujours associée à la création d'au moins un établissement économiquement actif.

La création d'entreprise peut correspondre :

à une nouvelle immatriculation dans le répertoire Sirene. Les moyens de production associés à une création d'entreprise peuvent être créés et sont donc réellement nouveaux ;
à une réactivation économique d'une entreprise. Les moyens de production associés à une création d'entreprise peuvent être réactivés, c'est-à-dire remis en exploitation après une cessation d'activité.
**Entreprise**
Une entreprise est une unité économique, juridiquement autonome, organisée pour produire des biens ou des services pour le marché.

Il existe deux grandes catégories (ou familles) :

l'entreprise individuelle qui ne possède pas de personnalité juridique distincte de celle de son exploitant (commerçant, artisan, profession libérale) ;
l'entreprise dite personne morale : société anonyme (SA), société à responsabilité limitée (SARL).

**Établissement**
Un établissement est une unité d'exploitation ou de production localisée géographiquement, individualisée mais dépendant juridiquement d'une entreprise. C'est le lieu où est effectivement exercée l'activité (magasin, atelier).

**Nomenclature d'activités française - NAF rév. 2, 2008**
L'activité principale exercée (APE) des entreprises et des établissements au répertoire Sirene est codifiée selon la nomenclature d'activité française (NAF), adaptation nationale de la nomenclature des activités économiques des communautés européennes (NACE).

La version en vigueur (rév. 2, 2008) est la nouvelle nomenclature statistique nationale depuis le 1^er^ janvier 2008. Elle reprend tous les niveaux de la nomenclature européenne et y ajoute un niveau national pour tenir compte des spécificités et des habitudes françaises (quatre chiffres et une lettre).

[La nomenclature d'activités française - NAF rév. 2, 2008.](https://www.insee.fr/fr/metadonnees/nafr2/section/A) aussi [disponible en local](./naf.csv)

**Siège**

Le siège est un établissement particulier. Pour les personnes morales, le siège est l'établissement où sont centralisées l'administration et la direction effective de l'entreprise. Le siège d'une personne morale est un élément juridique et obligatoire, constitutif de son identité. Par construction, les personnes physiques ont également un établissement siège dans le répertoire Sirene, mais celui-ci n'a pas d'existence ni de valeur au plan juridique ou administratif : il reste un concept interne. Chaque entreprise a un et un seul établissement siège.

**Siren**

Identifiant à neuf chiffres attribué par l'Insee à toute personne physique ou morale inscrite au répertoire des entreprises et des établissements.

**Sirene**

Système national d'identification et du répertoire des entreprises et de leurs établissements.

**Siret**

Le numéro Siret est le numéro unique d'identification attribué à chaque établissement par l'Insee. Ce numéro est un simple numéro d'ordre, composé de 14 chiffres non significatifs : les neuf premiers correspondent au numéro Siren de l'entreprise dont l'établissement dépend et les cinq derniers à un numéro interne de classement (NIC).

Une entreprise est constituée d'autant d'établissements qu'il y a de lieux différents où elle exerce son activité. L'établissement est fermé quand l'activité cesse dans l'établissement concerné ou lorsque l'établissement change d'adresse.

**Unité légale**

L'unité légale est une entité juridique de droit public ou privé. Elle peut être :

* une personne morale, dont l'existence est reconnue par la loi indépendamment des personnes qui la possèdent ou qui en sont membres ;
* une personne physique indépendante exerçant une activité économique.

Elle doit être déclarée aux administrations compétentes (greffes, Sécurité sociale, DGI...) pour exister.

> [!NOTE]
> Ne pas confondre avec la définition de l’entreprise au sens de la loi de modernisation de l'économie (LME), qui est une unité statistique.

## Les services de l'API Sirene

### Recherche unitaire - Présentation du service

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

**Tableau de la réponse**

| Variable                                      | longueur | Contenu                                                                                                                                               | Commentaire                                                                                                                               |
| --------------------------------------------- | -------: | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| siren                                         |        9 | Numéro Siren de l'entreprise                                                                                                                          | Toujours renseigné                                                                                                                        |
| statutDiffusionUniteLegale                    |        1 | Statut de diffusion de l’unité légale                                                                                                                 | O ou P (ou M prochainement)                                                                                                               |
| **unitePurgeeUniteLegale**                    |          | True si l'unité est une unité purgée                                                                                                                  | Pour les unités non purgées, variable non présente dans la réponse                                                                        |
| dateCreationUniteLegale                       |       10 | Date de création de l'unité légale                                                                                                                    | Format AAAA-MM-JJ                                                                                                                         |
| sigleUniteLegale                              |       20 | Sigle de l’unité légale                                                                                                                               | [ND] si diffusion partielle                                                                                                               |
| sexeUniteLegale                               |        4 | Sexe pour les personnes physiques                                                                                                                     | M, F<br>*Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                  |
| prenom1UniteLegale                            |       20 | Premier prénom pour les personnes physiques                                                                                                           | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| prenom2UniteLegale                            |       20 | Deuxième prénom pour les personnes physiques                                                                                                          | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| prenom3UniteLegale                            |       20 | Troisième prénom pour les personnes physiques                                                                                                         | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| prenom4UniteLegale                            |       20 | Quatrième prénom pour les personnes physiques                                                                                                         | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| prenomUsuelUniteLegale                        |       20 | Prénom usuel pour la personne physique                                                                                                                | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| pseudonymeUniteLegale                         |      100 | Pseudonyme pour les personnes physiques                                                                                                               | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| identifiantAssociationUniteLegale             |       10 | Numéro au Répertoire National des Associations ou autre répertoire d'association                                                                      |                                                                                                                                           |
| trancheEffectifsUniteLegale                   |        2 | Tranche d’effectif salarié de l’unité légale                                                                                                          | Valeur de la tranche d’effectif si connue, sinon NN                                                                                       |
| anneeEffectifsUniteLegale                     |        4 | Année de la tranche d’effectif salarié de l’unité légale                                                                                              | Uniquement si trancheEffectifsUniteLegale est renseignée, sinon *null*                                                                    |
| dateDernierTraitementUniteLegale              |       23 | Date de la dernière mise à jour effectuée au répertoire Sirene sur le Siren concerné                                                                  | Format AAAA-MM-JJTHH:MM:SS.MMM                                                                                                            |
| nombrePeriodesUniteLegale                     |        2 | Nombre de périodes dans la vie de l’unité légale                                                                                                      |                                                                                                                                           |
| categorieEntreprise                           |        3 | Catégorie à laquelle appartient l’entreprise : PME = petite ou moyenne entreprise ; ETI = entreprise de taille intermédiaire ; GE = grande entreprise |                                                                                                                                           |
| anneeCategorieEntreprise                      |        4 | Année de validité de la catégorie d’entreprise                                                                                                        |                                                                                                                                           |
| dateFin                                       |       10 | Date de fin de la période                                                                                                                             | *Null* pour la dernière période<br>Format AAAA-MM-JJ                                                                                      |
| dateDebut                                     |       10 | Date de début de la période                                                                                                                           | Format AAAA-MM-JJ                                                                                                                         |
| etatAdministratifUniteLegale                  |        1 | État de l'entreprise pendant la période : A = entreprise active ; C = entreprise cessée                                                               |                                                                                                                                           |
| changementEtatAdministratifUniteLegale        |          | Indicatrice de changement d'état par rapport à la période précédente                                                                                  |                                                                                                                                           |
| nomUniteLegale                                |      100 | Nom de naissance pour les personnes physiques pour la période                                                                                         | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| changementNomUniteLegale                      |          | Indicatrice de changement du nom de naissance par rapport à la période précédente                                                                     |                                                                                                                                           |
| nomUsageUniteLegale                           |      100 | Nom d’usage pour les personnes physiques si celui-ci existe                                                                                           | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| changementNomUsageUniteLegale                 |          | Indicatrice de changement du nom d’usage par rapport à la période précédente                                                                          |                                                                                                                                           |
| denominationUniteLegale                       |      130 | Raison sociale pour les personnes morales                                                                                                             | *Null* pour les personnes physiques<br>[ND] si diffusion partielle                                                                        |
| changementDenominationUniteLegale             |          | Indicatrice de changement de la dénomination par rapport à la période précédente                                                                      |                                                                                                                                           |
| denominationUsuelle1UniteLegale               |       70 | Premier nom sous lequel l’entreprise est connue du public                                                                                             | [ND] si diffusion partielle                                                                                                               |
| denominationUsuelle2UniteLegale               |       70 | Deuxième nom sous lequel l’entreprise est connue du public                                                                                            | [ND] si diffusion partielle                                                                                                               |
| denominationUsuelle3UniteLegale               |       70 | Troisième nom sous lequel l’entreprise est connue du public                                                                                           | [ND] si diffusion partielle                                                                                                               |
| changementDenominationUsuelleUniteLegale      |          | Indicatrice de changement de la dénomination usuelle (ensemble des 3 dénominations usuelles) par rapport à la période précédente                      |                                                                                                                                           |
| categorieJuridiqueUniteLegale                 |        4 | Catégorie juridique de l'entreprise                                                                                                                   | =1000 pour les personnes physiques                                                                                                        |
| changementCategorieJuridiqueUniteLegale       |          | Indicatrice de changement de la catégorie juridique par rapport à la période précédente                                                               |                                                                                                                                           |
| activitePrincipaleUniteLegale                 |        6 | Activité principale de l'entreprise pendant la période                                                                                                | APE codifiée selon la nomenclature d'Activités Française (NAF) depuis 1993 et la nomenclature d'activités et de produits (NAP) auparavant |
| nomenclatureActivitePrincipaleUniteLegale     |        8 | Nomenclature de l’activité                                                                                                                            | Indique la nomenclature utilisée pour activitePrincipaleUniteLegale                                                                       |
| changementActivitePrincipaleUniteLegale       |          | Indicatrice de changement de l'activité principale par rapport à la période précédente                                                                |                                                                                                                                           |
| nicSiegeUniteLegale                           |        5 | Identifiant du siège pour la période                                                                                                                  | Le Siret du siège est obtenu en concaténant le Siren et le Nic                                                                            |
| changementNicSiegeUniteLegale                 |          | Indicatrice de changement de siège par rapport à la période précédente                                                                                |                                                                                                                                           |
| economieSocialeSolidaireUniteLegale           |        1 | Appartenance de l’unité légale au champ de l’économie sociale et solidaire (ESS)                                                                      | O, N ou *null*                                                                                                                            |
| changementEconomieSocialeSolidaireUniteLegale |          | Indicatrice de changement de l’appartenance à l’ESS par rapport à la période précédente                                                               |                                                                                                                                           |
| societeMissionUniteLegale                     |        1 | Appartenance de l’unité légale au champ des sociétés à mission                                                                                        | O, N ou *null*                                                                                                                            |
| changementSocieteMissionUniteLegale           |          | Indicatrice de changement de l'appartenance au champ des sociétés à mission par rapport à la période précédente                                       |                                                                                                                                           |
| caractereEmployeurUniteLegale                 |          | Toujours *null*                                                                                                                                       | La variable n'est plus gérée                                                                                                              |
| changementCaractereEmployeurUniteLegale       |          | Indicatrice de changement du caractère employeur par rapport à la période précédente                                                                  | La variable n'est plus gérée                                                                                                              |


| Variable                                       | longueur | Contenu                                                                                                                                               | Commentaire                                                                                                                               |
| ---------------------------------------------- | -------: | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| siren                                          |        9 | Numéro Siren de l'entreprise à laquelle appartient l'établissement                                                                                    |                                                                                                                                           |
| nic                                            |        5 | Numéro interne de classement de l'établissement                                                                                                       |                                                                                                                                           |
| siret                                          |       14 | Numéro Siret de l’établissement                                                                                                                       | Concaténation de siren et nic                                                                                                             |
| statutDiffusionEtablissement                   |        1 | Statut de diffusion de l’établissement                                                                                                                | O ou P (ou M prochainement)                                                                                                               |
| dateCreationEtablissement                      |       10 | Date de création de l'établissement                                                                                                                   | Format AAAA-MM-JJ                                                                                                                         |
| trancheEffectifsEtablissement                  |        2 | Tranche d’effectif salarié de l’établissement                                                                                                         | Valeur de la tranche d’effectif si connue, sinon NN                                                                                       |
| anneeEffectifsEtablissement                    |        4 | Année de la tranche d’effectif salarié de l’établissement                                                                                             | Uniquement si trancheEffectifsEtablissement est renseignée, sinon *null*                                                                  |
| activitePrincipaleRegistreMetiersEtablissement |        6 | Code de l’activité exercée par l’artisan inscrit au registre des métiers                                                                              | L’APRM est codifiée selon la nomenclature d’Activités Française de l’Artisanat (NAFA)                                                     |
| dateDernierTraitementEtablissement             |       23 | Date de la dernière mise à jour effectuée au répertoire Sirene sur l’établissement                                                                    | Format AAAA-MM-JJTHH:MM:SS.MMM                                                                                                            |
| etablissementSiege                             |          | Indicatrice précisant si le Siret est celui de l’établissement siège ou non                                                                           |                                                                                                                                           |
| nombrePeriodesEtablissement                    |        2 | Nombre de périodes dans la vie de l’établissement                                                                                                     |                                                                                                                                           |
| etatAdministratifUniteLegale                   |        1 | État de l'entreprise ; A = entreprise active ; C = entreprise cessée                                                                                  |                                                                                                                                           |
| statutDiffusionUniteLegale                     |        1 | Statut de diffusion de l’unité légale                                                                                                                 | O ou P (ou M prochainement)                                                                                                               |
| unitePurgeeUniteLegale                         |          | True si l'unité légale est une unité purgée                                                                                                           | Pour les unités non purgées variable non présente dans la réponse                                                                         |
| dateCreationUniteLegale                        |       10 | Date de création de l'unité légale                                                                                                                    | Format AAAA-MM-JJ                                                                                                                         |
| denominationUniteLegale                        |      130 | Raison sociale pour les personnes morales                                                                                                             | *Null* pour les personnes physiques<br>[ND] si diffusion partielle                                                                        |
| sigleUniteLegale                               |       20 | Sigle de l’unité légale                                                                                                                               | [ND] si diffusion partielle                                                                                                               |
| denominationUsuelle1UniteLegale                |       70 | Premier nom sous lequel l’entreprise est connue du public                                                                                             | [ND] si diffusion partielle                                                                                                               |
| denominationUsuelle2UniteLegale                |       70 | Deuxième nom sous lequel l’entreprise est connue du public                                                                                            | [ND] si diffusion partielle                                                                                                               |
| denominationUsuelle3UniteLegale                |       70 | Troisième nom sous lequel l’entreprise est connue du public                                                                                           | [ND] si diffusion partielle                                                                                                               |
| categorieJuridiqueUniteLegale                  |        4 | Catégorie juridique de l'entreprise                                                                                                                   | =1000 pour les personnes physiques                                                                                                        |
| sexeUniteLegale                                |        4 | Sexe pour les personnes physiques                                                                                                                     | M, F<br>*Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                  |
| nomUniteLegale                                 |      100 | Nom de naissance pour les personnes physiques                                                                                                         | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| nomUsageUniteLegale                            |      100 | Nom d’usage pour les personnes physiques                                                                                                              | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| prenom1UniteLegale                             |       20 | Premier prénom pour les personnes physiques                                                                                                           | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| prenom2UniteLegale                             |       20 | Deuxième prénom pour les personnes physiques                                                                                                          | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| prenom3UniteLegale                             |       20 | Troisième prénom pour les personnes physiques                                                                                                         | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| prenom4UniteLegale                             |       20 | Quatrième prénom pour les personnes physiques                                                                                                         | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| prenomUsuelUniteLegale                         |       20 | Prénom usuel pour la personne physique                                                                                                                | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| pseudonymeUniteLegale                          |      100 | Pseudonyme pour les personnes physiques                                                                                                               | *Null* pour les personnes morales<br>[ND] si diffusion partielle                                                                          |
| activitePrincipaleUniteLegale                  |        6 | Activité principale de l'entreprise                                                                                                                   | APE codifiée selon la nomenclature d'Activités Française (NAF) depuis 1993 et la nomenclature d'activités et de produits (NAP) auparavant |
| nomenclatureActiviteUniteLegale                |        8 |                                                                                                                                                       | Indique à partir de quelle nomenclature d’activité est codifiée activitePrincipaleUniteLegale                                             |
| identifiantAssociationUniteLegale              |       10 | Numéro au Répertoire National des Associations                                                                                                        |                                                                                                                                           |
| economieSocialeSolidaireUniteLegale            |        1 | Appartenance de l’unité légale au champ de l’économie sociale et solidaire(ESS)                                                                       | O, N ou *null*                                                                                                                            |
| societeMissionUniteLegale                      |        1 | Appartenance de l’unité légale au champ des sociétés à mission                                                                                        | O, N ou *null*                                                                                                                            |
| caractereEmployeurUniteLegale                  |          | Toujours *null*                                                                                                                                       | La variable n'est plus gérée                                                                                                              |
| trancheEffectifsUniteLegale                    |        2 | Tranche d’effectif salarié de l’unité légale                                                                                                          | Valeur de la tranche d’effectif si connue, sinon NN                                                                                       |
| anneeEffectifsUniteLegale                      |        4 | Année de la tranche d’effectif salarié de l’unité légale                                                                                              | Uniquement si trancheEffectifsUniteLegale est renseignée, sinon *null*                                                                    |
| nicSiegeUniteLegale                            |        5 | Identifiant du siège                                                                                                                                  | Le Siret du siège est obtenu en concaténant le numéro Siren et le Nic                                                                     |
| dateDernierTraitementUniteLegale               |       23 | Date de la dernière mise à jour effectuée au répertoire Sirene sur le Siren concerné                                                                  | Format AAAA-MM-JJTHH:MM:SS.MMM                                                                                                            |
| categorieEntreprise                            |        3 | Catégorie à laquelle appartient l’entreprise : PME = petite ou moyenne entreprise ; ETI = entreprise de taille intermédiaire ; GE = grande entreprise |                                                                                                                                           |
| anneeCategorieEntreprise                       |        4 | Année de validité de la catégorie d’entreprise                                                                                                        |                                                                                                                                           |
| complementAdresseEtablissement                 |      100 | Complément d'adresse de l'établissement                                                                                                               | [ND] si diffusion partielle                                                                                                               |
| numeroVoieEtablissement                        |        9 | Numéro dans la voie                                                                                                                                   | [ND] si diffusion partielle                                                                                                               |
| indiceRepetitionEtablissement                  |        4 | Indice de répétition du numéro dans la voie                                                                                                           | [ND] si diffusion partielle                                                                                                               |
| dernierNumeroVoieEtablissement                 |        9 | Dernier numéro dans la voie                                                                                                                           | [ND] si diffusion partielle                                                                                                               |
| indiceRepetitionDernierNumeroVoieEtablissement |        4 | Indice de répétition du dernier numéro dans la voie                                                                                                   | [ND] si diffusion partielle                                                                                                               |
| typeVoieEtablissement                          |       30 | Type de la voie                                                                                                                                       | [ND] si diffusion partielle                                                                                                               |
| libelleVoieEtablissement                       |      100 | Libellé de la voie                                                                                                                                    | [ND] si diffusion partielle                                                                                                               |
| codePostalEtablissement                        |        9 | Code postal                                                                                                                                           | [ND] si diffusion partielle                                                                                                               |
| libelleCommuneEtablissement                    |      100 | Libellé de la commune pour une adresse en France                                                                                                      | Libellé d’acheminement, *null* pour une adresse à l’étranger                                                                              |
| libelleCommuneEtrangerEtablissement            |      100 | Libellé complémentaire pour une adresse à l'étranger                                                                                                  |                                                                                                                                           |
| distributionSpecialeEtablissement              |          | Distribution spéciale (BP par ex)                                                                                                                     | La variable n'est plus gérée                                                                                                              |
| codeCommuneEtablissement                       |        5 | Code commune de localisation de l’établissement hors établissements situés à l’étranger                                                               | Le code commune est défini dans le code officiel géographique (COG)                                                                       |
| codeCedexEtablissement                         |          | Numéro de Cedex                                                                                                                                       | La variable n'est plus gérée                                                                                                              |
| libelleCedexEtablissement                      |          | Libellé correspondant au numéro de Cedex (variable codeCedexEtablissement)                                                                            | La variable n'est plus gérée                                                                                                              |
| codePaysEtrangerEtablissement                  |        5 | Code pays pour les établissements situés à l’étranger                                                                                                 |                                                                                                                                           |
| libellePaysEtrangerEtablissement               |      100 | Libellé du pays pour les adresses à l’étranger                                                                                                        |                                                                                                                                           |
| identifiantAdresseEtablissement                |       15 | Identifiant unique de l'adresse                                                                                                                       | [ND] si diffusion partielle                                                                                                               |
| coordonneeLambertAbscisseEtablissement         |       18 | Abscisse des coordonnées Lambert de l'adresse (géolocalisation)                                                                                       | [ND] si diffusion partielle                                                                                                               |
| coordonneeLambertOrdonneeEtablissement         |       18 | Ordonnée des coordonnées Lambert de l'adresse (géolocalisation)                                                                                       | [ND] si diffusion partielle                                                                                                               |
| complementAdresse2Etablissement                |          | Complément d'adresse de l'établissement                                                                                                               | La variable n'est plus gérée                                                                                                              |
| numeroVoie2Etablissement                       |          | Numéro dans la voie                                                                                                                                   | La variable n'est plus gérée                                                                                                              |
| indiceRepetition2Etablissement                 |          | Indice de répétition dans la voie                                                                                                                     | La variable n'est plus gérée                                                                                                              |
| typeVoie2Etablissement                         |          | Type de la voie                                                                                                                                       | La variable n'est plus gérée                                                                                                              |
| libelleVoie2Etablissement                      |          | Libellé de la voie                                                                                                                                    | La variable n'est plus gérée                                                                                                              |
| codePostal2Etablissement                       |          | Code postal                                                                                                                                           | La variable n'est plus gérée                                                                                                              |
| libelleCommune2Etablissement                   |          | Libellé de la commune pour une adresse complémentaire en France                                                                                       | La variable n'est plus gérée                                                                                                              |
| libelleCommuneEtranger2Etablissement           |          | Libellé complémentaire pour une adresse complémentaire à l'étranger                                                                                   | La variable n'est plus gérée                                                                                                              |
| distributionSpeciale2Etablissement             |          | Distribution spéciale (BP par ex)                                                                                                                     | La variable n'est plus gérée                                                                                                              |
| codeCommune2Etablissement                      |          | Code commune de localisation de l’établissement hors établissements situés à l’étranger                                                               | La variable n'est plus gérée                                                                                                              |
| codeCedex2Etablissement                        |          | Numéro de Cedex                                                                                                                                       | La variable n'est plus gérée                                                                                                              |
| libelleCedex2Etablissement                     |          | Libellé correspondant au numéro de Cedex (variable codeCedex2Etablissement)                                                                           | La variable n'est plus gérée                                                                                                              |
| codePaysEtranger2Etablissement                 |          | Code pays pour les établissements situés à l’étranger                                                                                                 | La variable n'est plus gérée                                                                                                              |
| libellePaysEtranger2Etablissement              |          | Libellé du pays pour les adresses complémentaires à l’étranger                                                                                        | La variable n'est plus gérée                                                                                                              |
| dateFin                                        |       10 | Date de fin de la période                                                                                                                             | *Null* pour la dernière période Format AAAA-MM-JJ                                                                                         |
| dateDebut                                      |       10 | Date de début de la période                                                                                                                           | Format AAAA-MM-JJ                                                                                                                         |
| etatAdministratifEtablissement                 |        1 | État de l'établissement pendant la période : A = établissement actif ; F = établissement fermé                                                        |                                                                                                                                           |
| changementEtatAdministratifEtablissement       |          | Indicatrice de changement de l'état administratif de l'établissement par rapport à la période précédente                                              |                                                                                                                                           |
| enseigne1Etablissement                         |       50 | Première ligne d'enseigne                                                                                                                             | [ND] si diffusion partielle                                                                                                               |
| enseigne2Etablissement                         |       50 | Deuxième ligne d'enseigne                                                                                                                             | [ND] si diffusion partielle                                                                                                               |
| enseigne3Etablissement                         |       50 | Troisième ligne d'enseigne                                                                                                                            | [ND] si diffusion partielle                                                                                                               |
| changementEnseigneEtablissement                |          | Indicatrice de changement de l'enseigne de l'établissement par rapport à la période précédente                                                        | Un seul indicateur pour les trois variables enseigne                                                                                      |
| denominationUsuelleEtablissement               |      100 | Nom sous lequel l’établissement est connu du public                                                                                                   | [ND] si diffusion partielle                                                                                                               |
| changementDenominationUsuelleEtablissement     |          | Indicatrice de changement de la dénomination usuelle de l’établissement par rapport à la période précédente                                           |                                                                                                                                           |
| activitePrincipaleEtablissement                |        6 | Activité principale de l'établissement pendant la période                                                                                             | APE codifiée selon la nomenclature d'Activités Française (NAF) depuis 1993 et la nomenclature d'activités et de produits (NAP) auparavant |
| nomenclatureActiviteEtablissement              |        8 | Nomenclature de l’activité                                                                                                                            | Indique à partir de quelle nomenclature d’activité est codifiée la variable activitePrincipaleEtablissement                               |
| changementActivitePrincipaleEtablissement      |          | Indicatrice de changement de l'activité principale de l'établissement par rapport à la période précédente                                             |                                                                                                                                           |
| caractereEmployeurEtablissement                |        1 | Caractère employeur de l'établissement                                                                                                                | O, N ou *null*                                                                                                                            |
| changementCaractereEmployeurEtablissement      |          | Indicatrice de changement du caractère employeur de l’établissement par rapport à la période précédente                                               |                                                                                                                                           |

# References

* https://portail-api.insee.fr/catalog/api/2ba0e549-5587-3ef1-9082-99cd865de66f/doc?page=cf5b6bb8-63fa-4d15-9b6b-b863fa3d1517
