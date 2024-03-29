# Translation files manipulation

## Frontend repository

Located at: https://github.com/interlink-project/frontend/tree/master/react/src/translations

You can change the content of the files manually or through [weblate](https://interlink-project.github.io/interlink-project/environments/weblate.html).

## Backend-catalogue

First of all, there are two sets of files:

* Object files: the files that represent the different objects, interlinkers, schemas and problemprofiles. As you can see in them, there are keys such as "name_translations" with a dictionary that contains the translations. Instead, these translations are not supposed to be changed here, but in the translation files.
    * https://github.com/interlink-project/backend-catalogue/tree/master/catalogue/seed/interlinkers
    * https://github.com/interlink-project/backend-catalogue/tree/master/catalogue/seed/problemprofiles
    https://github.com/interlink-project/backend-catalogue/tree/master/catalogue/seed/schemas

* Translations files: files that are updated when an object is changed / added / removed. For example, if I add a new interlinker, these files are completely erased and generated again.
    * https://github.com/interlink-project/backend-catalogue/tree/master/catalogue/seed/weblate


### Change workflows

* Push workflow: for example, someone adds a new schema or changes the phases of an existing one. The workflow generates new translation files based on the current status of the schemas, interlinkers and problemprofiles. So the translation files changed in a push are ignored.

* Pull request workflow: here, the workflow prevails the changes in the translation files, so the content is analyzed and the object files are updated with the content here. In fact, weblate makes pushes to a branch called "weblate", and when someone creates a pull request (usually me) this process is executed and then merged with the master branch. This merge (push) to the master branch triggers the "push workflow", generating new translation files after updating the object files with the translation files generated by weblate.

### Why?

Weblate needs a foreseeable file structure and key-value pair jsons to retrieve and store the translations made by the users.

The [generate.py](https://github.com/interlink-project/backend-catalogue/blob/master/catalogue/seed/generate.py) file gets all these translatable attributes from the object metadata files and generates Weblate compatible json files. For example:

[seed/interlinkers/software/google-drive/metadata.json](https://github.com/interlink-project/backend-catalogue/tree/master/catalogue/seed/interlinkers/software/google-drive/metadata.json) file:

```json
{
    ...
    "description_translations": {
        "en": "Google Drive is a file storage and synchronization service developed by Google. Launched on April 24, 2012, Google Drive allows users to store files in the cloud, synchronize files across devices, and share files.\nGoogle Drive encompasses Google Docs, Google Sheets, and Google Slides, which are a part of the Google Docs Editors office suite that permits collaborative editing of documents, spreadsheets, presentations, drawings, forms, and more. Files created and edited through the Google Docs suite are saved in Google Drive.\nThis software INTERLIKER allows users of the collaborative environment to create new documents, spreadsheets and presentations which can be co-edited and shared by co-production team participants",
        "es": "Google Drive es un servicio de almacenamiento y sincronizaci\u00f3n de archivos desarrollado por Google. Lanzado el 24 de abril de 2012, Google Drive permite a los usuarios almacenar archivos en la nube, sincronizar archivos entre dispositivos y compartir archivos.\nGoogle Drive incluye Google Docs, Google Sheets y Google Slides, que forman parte de Google Docs Editors. paquete ofim\u00e1tico que permite la edici\u00f3n colaborativa de documentos, hojas de c\u00e1lculo, presentaciones, dibujos, formularios y m\u00e1s. Los archivos creados y editados a trav\u00e9s de la suite Google Docs se guardan en Google Drive.\nEste software INTERLIKER permite a los usuarios del entorno colaborativo crear nuevos documentos, hojas de c\u00e1lculo y presentaciones que pueden ser coeditados y compartidos por los participantes del equipo de coproducci\u00f3n.",
        "it": "Google Drive \u00e8 un servizio di archiviazione e sincronizzazione di file sviluppato da Google. Lanciato il 24 aprile 2012, Google Drive consente agli utenti di archiviare file nel cloud, sincronizzare file tra dispositivi e condividere file.\nGoogle Drive comprende Google Docs, Google Sheets e Google Slides, che fanno parte della suite per ufficio di Google Docs Editors che consente la modifica collaborativa di documenti, fogli di lavoro, presentazioni, disegni, moduli e altro ancora. I file creati e modificati tramite la suite Google Docs vengono salvati in Google Drive.\nQuesto INTERLIKER software consente agli utenti dell'ambiente collaborativo di creare nuovi documenti, fogli di calcolo e presentazioni che possono essere modificati e condivisi dai partecipanti del team di coproduzione",
        "lv": "Google Drive ir failu uzglab\u0101\u0161anas un sinhroniz\u0113\u0161anas pakalpojums, ko izstr\u0101d\u0101jis Google. Pakalpojums uzs\u0101ka darb\u012bbu 2012. gada 24. apr\u012bl\u012b. Google Drive \u013cauj lietot\u0101jiem uzglab\u0101t failus m\u0101kon\u012b, sinhroniz\u0113t tos starp da\u017e\u0101d\u0101m ier\u012bc\u0113m un dal\u012bties ar tiem.\nGoogle Drive sast\u0101v no Google Docs, Google Sheets un Google Slides, kas ir da\u013ca no Google Docs Editors biroja komplekta, kas \u013cauj kop\u012bgi redi\u0123\u0113t dokumentus, izkl\u0101jlapas, prezent\u0101cijas, z\u012bm\u0113jumus, formas u.c. Google Docs izveidotie un redi\u0123\u0113tie faili tiek saglab\u0101ti Google Drive.\n\u0160is programmat\u016bras INTERLINKERs \u013cauj sadarb\u012bbas vides lietot\u0101jiem veidot jaunus dokumentus, izkl\u0101jlapas un prezent\u0101cijas, kas var tikt kop\u0113ji redi\u0123\u0113tas un izplat\u012btas starp koprades komandas dal\u012bbniekiem."
    },
    ...
    "name_translations": {
        "en": "Google Drive",
        "es": "Google Drive",
        "it": "Google Drive",
        "lv": "Google Drive"
    },
    ...
```

[seed/weblate/es/interlinkers.json](https://github.com/interlink-project/backend-catalogue/blob/master/catalogue/seed/weblate/es/interlinkers.json) file:

```json
{
    
    ...
    "softwareinterlinker;google-drive;name": "Google Drive",
    "softwareinterlinker;loomio;description": "<p>Loomio is an Open Source solution that offers a workspace for conversation, sharing information and opinions, making proposals, deciding actions and achieving outcomes. Con Loomio es posible</p><ul><li>iniciar y organizar discusiones y mantener un registro de la participaci\u00f3n e implicaci\u00f3n;</li><li>gestionar las decisiones colaborativas a trav\u00e9s de diferentes formas de sondeos, encuestas, etc;</li><li>permitir la votaci\u00f3n colaborativa en torno a ideas y propuestas en discusi\u00f3n.</li></ul>",
    ...
}
```

Weblate modifies these last files, so there is a need to pass the changes made to them to the object metadata files. For that, the [input.py](https://github.com/interlink-project/backend-catalogue/blob/master/catalogue/seed/input.py) file gets the values in the files managed by weblate and passes them to the object metadata files.

### Workaround to modify the translation files manually

1. Make the local changes to the files AND locally execute "python3 input.py". Then, commit and push all the changes generated to master.

2. Push the changes (only the translation files) to the "weblate" branch and open a pull request, wait for the workflow to finish and delete the branch.