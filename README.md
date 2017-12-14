# assignment1-django-models-SerkanEkremCengiz

## Django Codes
###  Creating_Migrations
This is responsible for creating new migrations and creates changes to the database.
It also adds a new table and creates changes to the table.
```
python manage.py makemigrations
```

### Applying_to_Changes
After the changes in the database are created, the changes are applied to the database.
```
python manage.py migrate
```

### SuperUser
This creates a user which have every privilege in the system.
```
python manage.py createsuperuser
```

### Running_Server
This activates the system in the specified address and if the address is not specified, it broadcasts at 127.0.0.1:8000.
```
python manage.py runserver
```

### Controlling_Database_ByTerminal
This allows us to control the database through the terminal.
```
python manage.py shell
```


## Git codes
### OpeningWriting_Readme
This opens the readme file and write the text("# assignment1-django-models-SerkanEkremCengiz") into it.
```
echo "# assignment1-django-models-SerkanEkremCengiz" >> README.md
```

### Creating_Repository
This creating a new git repository.
```
git init
```

### Inserting_Repository
This inserts the generated repository into the readme file.
```
git add README.md
```

### First_Commit
This specifies the files that are generated in the repository and collects them under the "first commit" heading.
```
git commit -m "first commit"
```

### Identifying_Adress
This code identifies the target point of git(this is the address being sent).
```
git remote add origin https://github.com/IstanbulSehirUniversity2017Fall/assignment1-django-models-SerkanEkremCengiz.git
```

### SendingFiles_toMaster
The committed files are sent to the specified destination under the "master" domain.
```
git push -u origin master
```
