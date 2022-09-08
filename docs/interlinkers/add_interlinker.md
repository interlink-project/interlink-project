**Instructions to create new Interlinkers**

A new software interlinker can be added directly to the catalogue following the steps below:

- Create a new folder with the name`s name, if the name has multiple words, it can't use spaces (hyphens between words):

For example:

"Survey Editor Interlinker" should be named: survey-editor

- Inside the interlinker's folder create the following files and directories:

snapshots (directory)

instructions.md (file)

logo.jpeg (file)

metadata.json (file)

- The catalogue allow to any interlinker to have several snapshots which display the interlinker functionality. All images must be included in the **snapshots** folder. For example for the interlinker augmenter the snapshots are:
  1. annotate.png
  2. approve.png
  3. descriptions.png
  4. manage.png
- Fill the _ **instructions.md** _ file with all necessary information to be able to use this interlinker. The instructions must follow markdown language ([https://en.wikipedia.org/wiki/Markdown](https://en.wikipedia.org/wiki/Markdown)).

- The _ **logo.jpeg** _ must be the logo which will identify assets created by the interlinker.

- The _ **metadata.** _ **json** must include the following information:

- **Administrative\_scopes**

This metadata information refers to the scope where the interlink is implemented, this information must be one of the follow options:

eu = European Union

national= Inside a specific country

local= Inside a specific city

- **Constraints\_and\_limitations\_translations**

- **Description\_translations**

This metadata describes and present the interlinker. It could be added as a list of several languages. For example, in the case of two languages the metadata information will be:

"en": "Augmenter is an Open Source application …",

"es":"Augmenter es una aplicación de código abierto …"

- **Difficulty**

Describe the leve lof difficulty in the use of the interlinker. For example if the component is very easy and requires few easy steps to deploy then the level of difficulty could be easy. In others cases the level could be greater as it need a lot of parameters to configure or depends on other software to deploy, the level then could be hard.

- **Environments**

The environment where the interlinker will be deploy. For example, if there are several severs where the platform is deployed, it will contain a list with the names of each server.

- **Id**

A unique identifier for the interlinker in the catalogue.

- **Instructions\_translations**

This metadata contains a link to a document where the instructions to create a new translation language.

- **Integration**

This metadata contains several variables used by the collaborative environment to integrate with a new interlinker. Several of them can be grouped inside the same category.

_Server configuration parameters. For example, in case of augmenter it will be located inside a subdomain called "servicepedia" (https://servicepedia.dev.interlink-project.ue):_

Domain: "",

Is\_subdomain: true,

Path: "servicepedia",

Service\_name: "servicepedia"

_Interlinker calling options. For example, for the interlinker augmenter the options used to call the interlinker functionality are:_

"_capabilities": {_

_"clone":false,_

"_delete":true,_

"_edit":true,_

"_instantiate":true,_

"_open\_in\_modal":false,_

"_preview":false,_

"_shortcut":true,_

"_view":true_

_}_

_Translation messages needed when the interlinker is called. For example, in case of the augmenter the options are:_

"capabilities\_translations": {

"delete\_text\_translations":

{ "en": "Delete una description of Augmenter",

"es": "Eliminar una descripción del Augmenter"},

"instantiate\_text\_translations":

{ "en": "Create a new description in Augmenter",

"es": "Crear una nueva descripci\u00f3n en Augmenter"},

"view\_text\_translations":

{"en": "Open a description web site to annotate.",

"es": "Abrir una p\u00e1gina con descripciones para anotar"}

- **Is\_responsive**

This metadata specifies if the component is responsive

- **Is\_sustainability\_related**

- **Laguages**

This metadata specifies the languages supported by the interlinker.

- **Licence**

This metadata specifies the license needed to use this interlinker.

- **Logotype**

This metadata specifies the location of the logo file.

- **Name\_translations**

This metadata specifies the translations of the interlinker's name. For example, in the case of the augmenter all the translation are the same:

"name\_translations": {

"en": "Augmenter",

"es": "Augmenter",

"it": "Augmenter",

"iv": "Augmenter"

}

- **Overview\_text**

This metadata contains a short description of the interlinker.

- **Problemprofiles**

This metadata contains all the related problem profiles.

- **Regulations\_and\_standards\_translations**

"regulations\_and\_standards\_translations": {

"en": "None",

"es": "None"

},

- **Supported\_by**

This metadata specifies if the interlinker is deployed together with the platform or in a external server.

- **Supports\_internationalization**

Specifies if the interlinker support several languages.

- **Tags\_translations**

Contains a several tags where the interlinker that describe the interlinker functionality.

"en": [

"decision making",

"idea management",

"improve descriptions",

"public service descriptions"

]

- **Targets**

"targets": [

"all"

],

- **Type**

This metadata specifies the type of interlinker, there is two options:

  - Software
  - Knowledge
- **Types**

"types": [

"enabling\_services;operation\_services"

]