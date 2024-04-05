## Utilitaires pour l'accès aux données data.gouv.fr

1. Les données Météo-France sont accessibles sur https://meteo.data.gouv.fr : vous pouvez directement les télécharger sur la plateforme. C'est une opération manuelle
2. Ces données sont également présentes sur https://wwW.data.gouv.fr : la plateforme data.gouv.fr contient l'ensemble du catalogue nationale, pas uniquement les données météo

### Télécharger l'ensemble des données d'un jeu de données sur meteo.data.gouv.fr ou data.gouv.fr

ATTENTION : Télécharger l'ensemble des données d'un jeu de données peut s'avérer couteux (temps de téléchargement, volume téléchargé sur votre connexion...). Vérifiez bien, avant de vous servir de cet utilitaire, que vous avez besoin de l'ensemble des données d'un jeu de données.

Vous pouvez utiliser l'utilitaire `download_datasets.py` de ce dépôt de la manière suivante : 

```
python download_datasets.py <URL_DATA_GOUV_OU_METEO_DATA_GOUV>
# Exemple : python download_datasets.py https://www.data.gouv.fr/fr/datasets/indices-de-position-sociale-dans-les-lycees-a-partir-de-2022/
# Exemple : python download_datasets.py https://meteo.data.gouv.fr/datasets/656dab84db1bdf627a40eaae
```

Les données sont alors téléchargées localement dans le dossier dans lequel vous exécutez le code.

### Données de modèle de prévision PNT

#### Run de modèle courant

Les donneés sont disponibles sur meteo.data.gouv.fr : https://meteo.data.gouv.fr/datasets?topic=65e0c82c2da27c1dff5fa66f

Ces données sont les résultats des derniers runs de modèle disponibles (ARPEGE et AROME) de Météo-France. 

Pour des raisons d'ergonomie de la plateforme, nous avons décidé de ne référencer que le dernier run des différents modèles.

Pour télécharger le dernier run disponible, vous pouvez utiliser le script : download_latest_run_pnt.py de la manière suivante :

```
python download_pnt.py <motcle> <optional:datedurun>
# python download_pnt.py arome-om-indien
# python download_pnt.py arpege01 2024-04-05T06:00:00Z # peut être pratique pour savoir si un nouveau run est sorti sans avoir à télécharger les données
```

Vous trouverez les mots-clés à utiliser dans le tableau ci-dessous.

ATTENTION : les volumes de données sont importants ! Ne téléchargez les données que si vous en avez besoin.

| Volumétrie estimative | Données | mot-clé |
| -- | -- | -- |
| 7,6G | /arome-om/ANTIL | arome-om-antil |
| 2,7G | ./arome-om/GUYANE | arome-om-guyane |
|  19G | ./arome-om/INDIEN | arome-om-indien |
| 4,1G | ./arome-om/NCALED | arome-om-ncaled |
| 4,8G | ./arome-om/POLYN | arome-om-polyn |
| 4,8G | ./arome/001 | arome001 |
|  20G | ./arome/0025 | arome0025 |
|  13G | ./arpege/01 | arpege01 |
|  21G | ./arpege/025 | arpege025 |

### API data.gouv.fr 

Toutes les métadonnées des jeux de données disponibles sur data.gouv.fr sont récupérables sur l'API, par exemple `https://www.data.gouv.fr/api/1/datasets/65bd19226c4e3fcbf4948f99` il suffit de modifier le slug du datasets (soit son `id` soit son `slug`)

Doc sur l'API : https://doc.data.gouv.fr/api/reference/

