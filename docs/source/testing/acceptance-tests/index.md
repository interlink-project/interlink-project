# Acceptance testing

<dl>
  <dt>Acceptance Testing</dt>
  <dd>This is a type of testing done by users, customers, or other authorised entities to determine application/software needs and business processes. Description: Acceptance testing is the most important phase of testing as this decides whether the client approves the application/software or not.</dd>
</dl>

This document ilustrates the different tests needed to ensure that the expected functionality of the INTERLINK Collaborative Environment is met. 

## Smoke Testing

The first section carries out a so-called *Smoke Testing*

<dl>
  <dt>Smoke Testing</dt>
  <dd>In computer programming and software testing, smoke testing is preliminary testing to reveal simple failures severe enough to, for example, reject a prospective software release.</dd>

  <dt>Staging server</dt>
  <dd>A server used to temporarily show certain users new and revised Internet and/or intranet pages before they are put into production.</dd>
</dl>

The following Smoke Testing should be applied over [INTERLINK's staging server](https://demo.interlink-project.eu/):

0. Before using the Collaborative environment, you must first login with your google credentials or create your own credentials at [https://demo.interlink-project.eu/](https://demo.interlink-project.eu/), i.e. the staging server of INTERLINK. **IMPORTANT**: All members of an envisaged team must logged into the platform before they can be added to a team. ![Login required screen](images/image0.PNG) ![AAC screen](images/image1.PNG)
1. Create a team which wants to take part in a co-production process. ![Two user sessions](images/image2.PNG) ![Creating a team](images/image3.png) ![Adding a user](images/image4.png) ![Team editing window](images/image5.png)
2. Create a co-production project where the activity to co-create is assessed ![Creating a new co-production project](images/image6.png)
3. Link the created team to the created co-production process. ![Select Team menu option and "Add new Team" button](images/image8.png) ![Click on pop-up window's Add team button](images/image9.png)
3. Choose a co-production process guide (flexibility to choose the best fitting schema)
   - Notice that there are several co-production trees available. We will take the one named "Default schema" ![Select default schema](images/image7.png)
   - You may customize such tree to the specific needs of your co-production process. Currently only DELETE task allowed, soon we will be able to add new objectives & tasks
   - Observe that specific co-production trees can be defined (e.g. VARAM case)
4. Create new roles and new teams with different rights than the core co-producers’ team. Currently a role applies to all phases, objectives and tasks of a co-production process. 
5. Use the guide to co-produce SOMETHING, e.g. project to co-assess the implementation of the co-production methodology of INTERLINK through the collaborative environment
   - For each of the tasks in the co-production phases you may select any of the recommended INTERLINKERs or instantiate a new one based on the generic software INTERLINKERs available at the bottom of the screen shown when selecting a co-production task. Check for the blue button at the bottom entitled "Initiate Procedure"
6. Review progress of project in OVERVIEW
7. Check functionality of the INTERLINK catalogue by clicking on INTERLINKERs, browsing, filtering and selecting INTERLINKERs.


## Acceptance testing 

Next, we will illustrate how to perform a more exhaustive suite of manual tests that expore all currently available functionalities within the Collaborative Environment.

The steps to validate that the miminum functionalities to allow a collaborative process to be materialized are listed below:

0. Ensure that team members have logged in at least once at [INTERLINK's staging server](https://demo.interlink-project.eu/)
   - Ensure that two sessions at least are opened, e.g. one for user dipina@deusto.es and another one for user dipina@gmail.com, to be able to test the environment's collaborative features sensibly. 
1. Create a team “INTERLINK co-production team for co-evaluation of collaborative environment” which will jointly generate an assessment of the environment and its capabilities to carry out collaborative processes. Add at least 2 members to the team, e.g. dipina@deusto.es and dipina@gmail.com
2. Create a co-production project, namely “Co-evaluation of the co-production process”
3. Go to settings and ensure that the project has a good logo. Click on the pencil icon and then SAVE.
4. Click on “Team” left hand side menu and add the created Team to the project. 
   - You can modify the team composition at any time by clicking on the hyperlink of the Team name. 
5. Click on “Overview” and select the co-production schema (tree) to use. Choose **“Default schema”**
6. Hit on “Guide” and let’s start as a team co-evaluating the collaborative environment 
7. Browse through the different phases of the co-production guide
   - Select different phases
   - Select objectives within a phase 
   - Select tasks within an objective
   - Observe that different INTERLINKERs are recommeded for different tasks
8. Instantiate a generic INTERLINKER, where feedback with your observations can be gathered in a shared Google Docs with the rest of the co-evaluators
   - In GUIDE view, select BUILD > Technical Implementation > Technical implementation
   - Hit on “Initiate Procedure” > “Create a Google Drive document” > create asset “Feedback about usage of Collaborative Environment”
   - Ensure that all team members edit and insert their comments in such shared document
   - Notice that they all could access to feedback document when clicking on Overview menu option on the left hand side. 
9. Explore how to navigate across the different views of the Collaborative Environment.
   - Explore navigation between “Guide” view and “Workplan” view by hitting on “Time planification”, once within a chosen task
   - Test changing the Time planification of a task, by hitting on the pencil and selecting start and end period, under the task screen within GUIDE view
   - Explore navigation between “Overview” view and “Guide” view by hitting on “See Task”
10. Use one of the recommended INTERLINKERs
   - For instance, select "Stakeholders Mapping Canvas" INTERLINKER under task shown when navigating to Engage > Identify Stakeholders  
   - Click on button “Instantiate as resource to use in the project”
   - Check the newly created resource appears at the bottom of the page under “Current resources”
   - Open the generated resource in the form of a presentation and add some modifications
11. Check that different recommended INTERLINKERs or those generic ones instantiated through "Initiate Procedure" can be started
   - Continue inspecting the different tasks and INTERLINKERs that are recommended for 5’
   - During the whole process PLEASE GATHER YOUR IMPRESSIONS / FEEDBACK on the shared document entitled “Feedback about usage of Collaborative Environment”
   - Remember that from OVERVIEW, you can simply click on the resource title to be able to open it. 
12. In order to provide direct feedback on any mistakes, bugs requested please use the following two channels:
   - Fill in the [ALPHA QUESTIONNAIRE](https://docs.google.com/forms/d/e/1FAIpQLSei2Iful343wNa3WMwS4di4Z_cqzv0ibuFf_I41hIrUm1pUVA/viewform) of INTERLINK. 
   - Access to the [Redmine support channel](http://redmine.interlink-project.eu/), log in and create a new issue under [proj_wp4_PLATFORM](http://redmine.interlink-project.eu/projects/proj_wp4_platform)


