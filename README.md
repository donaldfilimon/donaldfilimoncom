# 👋 Hello developer!

This is one of the many templates available from W3Schools. Check our [tutorials for frontend development](https://www.w3schools.com/where_to_start.asp) to learn the basics of [HTML](https://www.w3schools.com/html/default.asp), [CSS](https://www.w3schools.com/css/default.asp) and [JavaScript](https://www.w3schools.com/js/default.asp). 🦄  
Also check [Python](https://www.w3schools.com/python/) and [Django](https://www.w3schools.com/django/) tutorials to grasp the backend of this template.

## Knowledge requirements

To be able to fully understand and modify this template to your needs, there are several things you should know (or learn):

- [HTML](https://www.w3schools.com/html/default.asp)
- [CSS](https://www.w3schools.com/css/default.asp)
- [JavaScript](https://www.w3schools.com/js/default.asp)
- [Python](https://www.w3schools.com/python/)
- [Django](https://www.w3schools.com/django/)
- [SQLite](https://www.sqlite.org/docs.html)

## Warning - environment variables

Do not change DATABASE_URL and SECRET_KEY, as these are generated. If they are changed the space may not behave as predicted.
**Remember to switch DEBUG to false when going to production**

## 🔨 What's next?

Customize this template to make it your own.  
Remember to make your layout responsive - if you want your site to look good on smaller screens like mobile.

## 🎨 Where to find everything?

This template is made by using several technologies.
Below are explanations about where to find specific code.

### HTML

HTML files are stored in a folder called `templates`. Files have `.html` extension.
In `templates/base.html` you can add your external links and scripts, or change other meaningful things that is relevant on every page.
You can find other templates in `templates/`.

### CSS

CSS files can be found in `/blog/static/css`.  

### Core files

You can find:
  - views in `blank/views.py`.
  - local URL configuration in `blank/urls.py`.
  - global URL configuration in `blank_template/urls.py`.
  - models (for tables) in `blank/models.py`.
  - static files in `blank/static`.
  - settings in blank_template/settings.py

## Database

Dynamic spaces can use [SQLite](https://www.sqlite.org/docs.html) database.  
The database file is called `database.db`. It is placed inside the `w3s-dynamic-storage` folder.  
SQLite connection path to the database is `sqlite:///w3s-dynamic-storage/database.db` which you can use to connect to the SQLite database programmatically.   
For this template, the database connection path can also be found in the environment.  

---  
**Do not change the `w3s-dynamic-storage` folder name or `database.db` file name!**  
**By changing the `w3s-dynamic-storage` folder name or `database.db` file name, you risk the space not working properly.**

## 🔨 Please note
For now files created/uploaded or edited from within the terminal view will not be backed up or synced. 

## ⛑ Need support?
[Join our Discord community](https://discord.gg/6Z7UaRbUQM) and ask questions in the **#spaces-general** channel to get your space on the next level.  
[Send us a ticket](https://support.w3schools.com/hc/en-gb) if you have any technical issues with Spaces.

Happy coding!