# BerkeleyStartups
### Set up
1. Download [Django](https://www.djangoproject.com/download/)
2. Download [mySql](https://dev.mysql.com/downloads/mysql/)  
    a. Choose the Community Server  
    b. Download your corresponding version macOS YOUR VERSION, Compressed TAR Archive
3. start mySQL server by using **brew services start mysql**  
    a. if that did not work, either you do not have **brew** or some strange error  
    b. if you do no have brew, go to this [website](https://brew.sh/)  
    c. if strange error happened, use **sudo mysql.server start**  
4. Install [taggit](https://github.com/alex/django-taggit)
5. pull from github [repo](https://github.com/EatB/BerkeleyStartups)  
    a. **cd** into a desired directory  
    b. type **git clone https://github.com/EatB/BerkeleyStartups **  


All the neccessary environments should be set up now, lets proceed to setting up database  
open up a shell terminal


1. **cd** into your project directory
2. follow [Django Tutorial](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#creating-an-admin-user)  
    a. username: admin  
    b. password: YOUR_PASSWORD  
3. set up mySQL database, use the following commands  
    a. mysql -u root  
    b. CREATE DATABASE django  
    c. exit  
4. go to YOUR_PROJECT_DIRECTORY/BerkeleyStartups/settings.py  
    a. in the DATABASE section, replace XXX with YOUR_PASSWORD  


OK, you should be good to go now


1. To start the server, **cd** into your project directory and type **python manage.py runserver**
2. If you made changes in the model, please do the following:  
    python manage.py makemigrations [the app you made changes]  
    python manage.py sqlmigrate database 0001  
    python manage.py migrate  
    python manage.py runserver  
    
