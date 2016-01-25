# DandD
Dungeons and Dragons Dungeon Master API
162.243.13.105

https://www.youtube.com/watch?v=L8p8ceKqvVQ

### TL;DR: A tool for a Dungeon Master (DM) to record all data pertaining to the the game. Other players can also look at it and see information pertaining to their own character.

##### Understood:  
  Databases (mongoDB) to store each account's information (games, characters, items, monsters, story progress)  
  Forms to grab the information entered by the DM  
  CSS to prettify  
  Javascript to animate certain interactions (selecting an icon, drag and drop, etc.)  

##### Not understood but probably not that bad:  
  flask-socketio to constantly update the information  

##### Wat:  
  Map maker for the DM to create his dungeon.  
  Map of the dungeon that is interactive - can place characters on squares and move things around.  

##### Player Traits:  

  Strength (*Str*)  
  Dexterity (*Dex*)  
  Constitution (*Con*)  
  Intelligence (*Int*)  
  Wisdom (*Wis*)  
  Charisma (*Cha*)  

##### Skills:  
  Physical:  
  Magical:  
  Passive:  


##### Items:  
  Weapons:  
  Consumables:  
  Armor:  
  Trinkets:  
  Quest Items:  

##### Races:  
  Aberrations  
  Beasts  
  Celestials  
  Constructs  
  Dragons  
  Elementals  
  Fey  
  Fiends  
  Giants  
  Humanoids  
  Monstrosities  
  Oozes  
  Plants  
  Undead  

##### Home Page:  
  A brief description of the page and how to use it.

##### Register and Login/Logout:
  Save your games so you can abstain with the pen and paper! No more hassle!

##### Games Page:  
  A list of all games you currently manage.

##### Build and Run!:  
  req - pymongo, flask-socketio, flask, eventlet, gunicorn, nginx
  to simply run this just python app.py in the home directory of this folder
  
##### Changelog:
12/16/15 - Inital flask, app.py, and example JSON 
12/17/15 - Outline of project written in README, started login 
12/18/15 - Master.html, more login, styles.css, utils.py, register.js, characters.js
12/19/15 - Added pages to app.py
12/21/15 - Mongo stuff in utils.py, testing socket stuff
12/22/15 - Fixing up utils, character.js
1/4/16 - Resuming work 
1/5/16 - Pop-up windows! And Bootstrap
1/7/16 - Javascript and JQuery is happening, more styling too
1/8/16 - More styling and Bootstrap
1/9/16 - charinfo.js and gameinfo.js
1/12/16 - Lots of cleaning up files
1/13/16 - Account editing
1/14/16 - Editing .js files, characters. editaccount
1/19/16 - Prettifying fonts
1/20/16 - Universal form styling added
1/21/16 - Form styling only applied to editaccount, charinfo and gameinfo js functions
1/23/16 - Adding more JS functions
1/24/16 - Digital Ocean set up, cool pictures added, Youtube video filmed
1/25/16 - README on the website and here updated, changelog written





