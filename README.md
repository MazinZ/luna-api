## Install Homebrew

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

## Install git, git-flow and wget

```brew install git git-flow wget```

## Clone the repository

`git clone https://github.com/MazinZ/luna-web.git`

## Init git-flow

```git flow init -d```

## Install pip

```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```

## Create a virtual environment
cd into the luna-web folder that you cloned and run:

```
sudo pip install virtualenv
virtualenv -p python3 lunaenv
source lunaenv/bin/activate
```

Run the following commands (from the /luna-web directory) to setup the client and server:

### Client
```
brew install npm
cd angular
npm install
cd app/js/external_libs
bower install
```

These should also be done from the /luna-web directory:

### Server
```
pip install -r requirements.txt
cd django
python manage.py migrate
python manage.py runserver
```

After all that is finished, open a new terminal window, go back to the root of the project (/luna-web) and run `foreman start`.
