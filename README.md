#Flask Blog

A Basic Bloging platform writen in python using flaks micro framework.
Resources to create this project from scrach : https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

#Technology stack:

    Language / Platfrom: Python
    Framework : Flask
    Databse: sqlite (This can be change to any relational db)
    Database handling / mapper: SQLAlchemy (flask_sqlalchmey package)
    Basic Styling: Bootstrap (and some custom styling 😉)
    User authentication and session handling: flask_loging package
    Password encrypting and decrypting: Bcrypt (flask_bcrypt package)
    Sending emails: Flask Mail package
    Pasword reset token handling: Itsdangerous package
    Image manipulation: Pillow package
 

#What it can:
	Register new users
    create/preview/update/delete articles;
    update user profiles
    reset passwords via a reset email
    coustom error pages


#Requirements:

    bcrypt==3.1.6
	blinker==1.4
	cffi==1.12.3
	Click==7.0
	Flask==1.0.2
	Flask-Bcrypt==0.7.1
	Flask-Login==0.4.1
	Flask-Mail==0.9.1
	Flask-SQLAlchemy==2.4.0
	Flask-WTF==0.14.2
	itsdangerous==1.1.0
	Jinja2==2.10.1
	MarkupSafe==1.1.1
	Pillow==6.0.0
	pycparser==2.19
	six==1.12.0
	SQLAlchemy==1.3.3
	Werkzeug==0.15.4
	WTForms==2.2.1

#Installation:

git clone https://github.com/madushan-sooriyarathne/Flask-Blog.git

cd Flask-Blog

pipenv install

After this edit the config.cfg file to match your configs

    mail_server = your mail provider's mail server(eg: smtp.mail.yahoo.com)
	mail_port = mail provider's port (eg: 457)
	mail_username = your email (eg: madushan@example.com)
	mail_password = your email password
	database_uri = your database uri (eg: sqlite:///site.db)
	secret_key = your secret key (eg: 2682162fa3b9a00a98c03c2427fe39b0)

Note: If you are running this code on a production sever set the debug flag to False in run.py file.
    
    


