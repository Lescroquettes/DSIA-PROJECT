# DSIA PROJECT README

###### last modification 03/11/2021

## CONTRIBUTER

Hello, my name is Bérangère MAHMOUD--LAMY. I am a french student in engineering school at E.S.I.I.E. PARIS placed in Noisy-Le-Grand. I am currently in the fourth year of my cursus in theorical computer science degree.

## PROJECT

This work was realised in October and November 2021 by myself in order to graduate a subject. The entitled was to search a database to analyse and treat. The final aim was to open a local website using dashboard to smartly show the dataset. 

## USER GUIDE
### INSTALLATION

To be able to open and use the project, please follow next steps : 

Please make sure that you have download last version of Python : [DOWNLOAD PYTHON HERE](https://www.python.org/downloads/).

Futhermore, you will need the last version of Anaconda : [DOWNLOAD ANACONDA HERE](https://www.anaconda.com/products/individual).

After had download Anaconda, you will be able to launch the 'Conda prompt'. In your computer search bar, please enter "Anaconda Prompt (anaconda3)" and open it.
In the Conda prompt, use the package manager [pip](https://pip.pypa.io/en/stable/) to install libraries :

The project that you are trying to use require multiple libraries.
```bash
pip install pandas 
```
```bash
pip install dash
```
```bash
pip install dash_bootstrap_components 
```
```bash
pip install dash_core_components 
```
```bash
pip install dash_html_components 
```
```bash
pip install plotly
```

### LAUNCH THE PROJECT

In the command prompt, you need to place yourself in the right path, then you will just need to use the next command :
```bash
python main.py
```
Then you can open a browser at [http://127.0.0.1:8085/](http://127.0.0.1:8085/) to manage the project.
To close the project, use "CTRL+C" or close the prompt command.

### LIBRARIES DOCUMENTATION
[PANDAS DOC](https://pandas.pydata.org/docs/)

[BASH DOC](https://dash.plotly.com/)

[DBC DOC](https://dash-bootstrap-components.opensource.faculty.ai/docs/)

[DCC DOC](https://dash.plotly.com/dash-core-components)

[DHC DOC](https://dash.plotly.com/dash-html-components)

[PLOTLY DOC](https://plotly.com/python/)

## DEVELOPPER GUIDE

If you want to modify the project, here you will find some instructions :

### CHANGE DATABASE

If you want to change the dataset, you will need to put your datas in .csv format in the folder "Datas". In the code, at "PARAMETER LABEL INIT" you will need to change checklists and rangeslider labels and values according to your dataset. You will need to change their ID. At the callback section "INTERACTIONS, CALLBACKS" please make sure to change outputs, inputs and statements (states) according to your new ID name. In update_graph_1 and update_graph_2 functions you will also need to change the path to reading file because your dataset isn't the same as mine. After that you will be able to use the project with your own database.

### CHANGE DATABASE // ADD FUNCTIONS

If you want to change function, please make sure to have correct parameters according to inputs and states, correct returned variables according to outputs. Don't forget to check documentations if you want to change visualisation.
If you want to add function, please make sure to attribute correct callback signal. You will need a place to put your new display. I use "content" to put my displays. In "content" are refered "content_first_row" and "content_second_row" which are dash_bootstrap_components Row(). In those object you will find dash_bootstrap_components Col(). You can share space in the a Row() by creating another dash_bootstrap_components Col(). Or you can create a third dash_bootstrap_components Row() in which you will be able to create dash_bootstrap_components Col(). Don't forget to put the new dash_bootstrap_components Row() in "content".

### CHANGE STYLE / FONT / SPACES

If you want to personalize your own page you can modify the "STYLE INIT" section in the code. You will find "PARAMETERBAR_STYLE", "CONTENT_STYLE", "TEXT_STYLE" and "CARD_TEXT_STYLE". They are style object format use for dash_bootstrap_components. In the documentation you can find pre-existing style and their attributes. Change attributes as you want in my style object. If you want, you can create style object for other dash_bootstrap_components, like putting background colors or images, changing police, fontsize, colors and more. 

## ANALYSIS RAPPORT

I chose the followed database [HERE](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/). My aim was at first to be able to map a area with lightning strike impact like on map.blitzortung.org [HERE](https://map.blitzortung.org/#4.72/42.64/9.4). But lightning map showed on the web are using private database, and i couldn't find one public, so i search for meteorological events. I found this database but didn't want to use it because it was datas from United States of America and not from Europe. I asked "Meteo France" to share private database with me for my project but never had answers. So i keep my previous database.

This database is very complete for meteorological events but isn't as good as i hope. Firstly, even if datas are fill since 1961, datas before 1986 are really poor. Secondly, not all events have GPS coordinates, and even if somes have it, they are not fill for previous years. Thirdly, some events changed their name between one period to the other, so some refers to old datas and others to recent datas.

Despite this, the database is rich in informations. With the project, you will be able to comparate meteorological events between states choosed according to your study period. If gps coordinates are filled, you will be able to look at them on the map directly. You can see close area of repetitive meteorological events through years.

If you want more details about the database : [MORE INFO](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/Storm-Data-Export-Format.pdf).

Please find the meteorological events classification used for the project and the analysis of the dataset [CLASSIFICATION](https://www.emdat.be/classification).

## PRECISIONS

In the dashboard in parameters, you can check all events box or states box with the check all box, but you need to click on submit first to submit the request then if you want to study all of it then you need to submit it again without modiying anything. If you want to uncheck all box, you need to check the check all box then submit, then uncheck it then submit then choose what you want to study.
If no events or no states are filled the page will continue but no graph will change. 

If you select a large dataset to study, please make sure to wait at least 3 minutes max before graphics update.
