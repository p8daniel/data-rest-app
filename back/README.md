# API resources


## Characters

GET /api/v1/characters
####Description
Get the list of characters with details

<br><br/>
POST /api/v1/characters
####Description
Add a new character to the database
####Parameters
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
  <tr>
    <th>name</th>
    <th>The name of the character name</th>
    <th>text</th>
  </tr> 
   <tr>
    <th>age</th>
    <th>The age of the character</th>
    <th>integer</th>
  </tr> 
   <tr>
    <th>weight</th>
    <th>The weigth of the character</th>
    <th>integer</th>
  </tr>
   <tr>
    <th>human</th>
    <th>When true the character is human</th>
    <th>boolean</th>
  </tr>
   <tr>
    <th>hat</th>
    <th>Optional argument: choose one  of the authorized colors for hats</th>
    <th>text</th>
  </tr>
</table>

<br><br/>
## Character

GET /api/v1/character/{character id}
####Description
Get the detail of a specific character by the character id

<br><br/>
DELETE /api/v1/character/{character id}
####Description
Delete the specific character from the database

<br><br/>
PATCH /api/v1/character/{character id}
####Description
Update one or more parameters of the character
####Parameters
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
  <tr>
    <th>name</th>
    <th>Optional argument: the name of the character name</th>
    <th>text</th>
  </tr> 
   <tr>
    <th>age</th>
    <th>Optional argument: the age of the character</th>
    <th>integer</th>
  </tr> 
   <tr>
    <th>weight</th>
    <th>Optional argument: the weigth of the character</th>
    <th>integer</th>
  </tr>
   <tr>
    <th>human</th>
    <th>Optional argument: when true character is a human</th>
    <th>boolean</th>
  </tr>
   <tr>
    <th>hat</th>
    <th>Optional argument: choose one of the authorized colors for hats</th>
    <th>text</th>
  </tr>
</table>

<br><br/>
## Hats

GET /api/v1/hats
####Description
Get the list of hats with details of the associated character 

<br><br/>
## Data

POST /api/v1/data
####Description
Store into database the names and the average value by name of the data table

####Required field
{'name': [list of names],
'value': [list of values]}
<br><br/>
