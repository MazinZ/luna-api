## Install Homebrew

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

## Install git, git-flow and wget

```brew install git git-flow wget```

## Clone the repository

`git clone https://github.com/MazinZ/luna-api.git`

## Init git-flow

```git flow init -d```

## Install pip

```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```

## Create a virtual environment
cd into the luna-api folder that you cloned and run:

```
sudo pip install virtualenv
virtualenv lunaenv
source lunaenv/bin/activate
```

Run the following commands (from the /luna-api directory):

```
pip install -r requirements.txt
python manage.py migrate
```

After all that is finished, make sure you're in the root of the project (/luna-api) and run `foreman start`.
The api should start up at localhost:8000.

