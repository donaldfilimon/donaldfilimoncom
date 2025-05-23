# 👋 Hello developer!

This project serves as an example of what can be achieved. It is not a fully functional product. Feel free to use the source code and ideas as a starting point for your own projects.

This is one of the many templates available from W3Schools. Check our [tutorials for frontend development](https://www.w3schools.com/where_to_start.asp) to learn the basics of [HTML](https://www.w3schools.com/html/default.asp), [CSS](https://www.w3schools.com/css/default.asp) and [JavaScript](https://www.w3schools.com/js/default.asp). 🦄  
Also check [Python](https://www.w3schools.com/python/) and [Django](https://www.w3schools.com/django/) tutorials to grasp the backend of this template.

This template provides a comprehensive example of utilizing TensorFlow to train a machine learning model for image recognition. The model is trained to identify images based on 10 distinct categories. The template features a user-friendly frontend interface, developed using Django, that seamlessly integrates with the trained AI in the backend. The backend AI processes the input image and returns the predicted category to the frontend for display. The overall design is simple yet effective, making it easy for users to understand and utilize the AI's capabilities.

We provide a simple trained AI for the website to use. It is not perfect by any means. It is stored in `app/CNN/model/cifar_model.h5`. 

You can find the model structure in `app/CNN/model.py`. The model is easy to understand, and the training doesn't demand too much computer resources. 

If you want to train a model yourself you have to use your own computer and do it locally. You do this by cloning the repository to your local machine and running the training script. The training script is located in `ai/CIFAR_training.py`. It is set up for CPU use. If your computer has the correct architecture, you can also use a GPU for faster training.

To train the model locally, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/donaldfilimon/donaldfilimoncom.git
   cd donaldfilimoncom
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the training script:
   ```
   python ai/CIFAR_training.py
   ```

4. The trained model will be saved as `cifar_model_<timestamp>.h5` in the current directory.

## Knowledge requirements

To be able to fully understand and modify this template to your needs, there are several things you should know (or learn):

- [HTML](https://www.w3schools.com/html/default.asp)
- [CSS](https://www.w3schools.com/css/default.asp)
- [JavaScript](https://www.w3schools.com/js/default.asp)
- [Python](https://www.w3schools.com/python/)
- [Django](https://www.w3schools.com/django/)
- [SQLite](https://www.sqlite.org/docs.html)
- [TensorFlow](https://www.tensorflow.org/)

### Resources

- [TensorFlow Image Classification example](https://www.tensorflow.org/tutorials/images/cnn)

## Warning - environment variables

Do not change DATABASE_URL and SECRET_KEY, as these are generated. If they are changed the space may not behave as predicted.
**Remember to switch DEBUG to false when going to production**

## 🔨 What's next?

Customize this template to make it your own. 
Remember to make your layout responsive - if you want your site to look good on smaller screens like mobile.

There is an endless amount of possibilities going forwards.
- Expand the file input like supporting drag and drop or uploading multiple images.
- Expand the website with multiple sections showing results or history.
- Set up Django models and save information to the database like training history or datasets
- Learn how to make your own datasets. This AI is trained based on RGB images. You can customize the already made dataset, like changing it to grayscale (1 channel instead of 3) or add rotation, as well as put together your own image set.
- Add administration UI for statistics.
- Write custom datasets to your liking. [See TensorFlow's guide](https://www.tensorflow.org/datasets/add_dataset) for how.

## 🎨 Where to find everything?

This template is made by using several technologies.  
Below are explanations about where to find specific code.

### HTML

HTML files are stored in a folder called `templates`. Files have `.html` extension.
In `templates/base.html` you can add your external links and scripts, or change other meaningful things that is relevant on every page.
You can find other templates in `templates/`.

### CSS and icons

CSS files can be found in `/app/assets/css`.  
Icons are stored in `/app/assets/images`.

### Core files

You can find:
  - views in `app/views.py`
  - local URL configuration in `app/urls.py`
  - global URL configuration in `app_settings/urls.py`
  - models (for tables) in `app/models.py`
  - settings in `blog_template/settings.py`
  - the AI training and model in `app/CNN/`

## Database

Dynamic spaces can use [SQLite](https://www.sqlite.org/docs.html) database.  
The database file is called `database.db`. It is placed inside the `w3s-dynamic-storage` folder.  
SQLite connection path to the database is `sqlite:///w3s-dynamic-storage/database.db` which you can use to connect to the SQLite database programmatically.   
For this template, the database connection path can also be found in the environment.  

---  
**Do not change the `w3s-dynamic-storage` folder name or `database.db` file name!**  
**By changing the `w3s-dynamic-storage` folder name or `database.db` file name, you risk the space not working properly.**
## Misc: 
  - `python3 manage.py makemigrations`
    - If you make models as well as changing them you need to make migrations to create a new database.
  - `python3 manage.py migrate`
    - Migrate is needed to put the model changes into effect after making migrations. This will create new tables which means you may have conflicts to already stored data. In that case Django will ask in the terminal what you would like to do. This is the message:
    `It is impossible to add a non-nullable field <name> to <model> without specifying a default`. This is because the database needs something to populate existing rows.
    Please select a fix:
      1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
      2) Quit and manually define a default value in models.py.
      Select an option: `
    You avoid this by setting a default when you add the field to the model. E.g. `title = models.CharField(("title"), max_length=250)`

## 🔨 Please note
For now files created/uploaded or edited from within the terminal view will not be backed up or synced. 

## ⛑ Need support?
[Join our Discord community](https://discord.gg/6Z7UaRbUQM) and ask questions in the **#spaces-general** channel to get your space on the next level.  
[Send us a ticket](https://support.w3schools.com/hc/en-gb) if you have any technical issues with Spaces.

Happy learning!
