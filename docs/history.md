catalunha@pop-os:~/myapp/musictobelight/musictobelightapi$ pyenv versions
  system
* 3.11.0 (set by /home/catalunha/.pyenv/version)
  3.11.4
catalunha@pop-os:~/myapp/musictobelight/musictobelightapi$ pyenv local 3.11.0
catalunha@pop-os:~/myapp/musictobelight/musictobelightapi$ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [musictobelightapi]:  
Version [0.1.0]:  
Description []:  
Author [catalunha <catalunha.mj@gmail.com>, n to skip]:  
License []:  
Compatible Python versions [^3.11]:  

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "musictobelightapi"
version = "0.1.0"
description = ""
authors = ["catalunha <catalunha.mj@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
catalunha@pop-os:~/myapp/musictobelight/musictobelightapi$ poetry shell
Creating virtualenv musictobelightapi in /home/catalunha/myapp/musictobelight/musictobelightapi/.venv
Spawning shell within /home/catalunha/myapp/musictobelight/musictobelightapi/.venv
. /home/catalunha/myapp/musictobelight/musictobelightapi/.venv/bin/activate
catalunha@pop-os:~/myapp/musictobelight/musictobelightapi$ . /home/catalunha/myapp/musictobelight/musictobelightapi/.venv/bin/activate
(musictobelightapi-py3.11) catalunha@pop-os:~/myapp/musictobelight/musictobelightapi$ poetry add django
Using version ^5.0 for django

Updating dependencies
Resolving dependencies... (0.5s)

Package operations: 3 installs, 0 updates, 0 removals

  • Installing asgiref (3.7.2)
  • Installing sqlparse (0.4.4)
  • Installing django (5.0)

Writing lock file
(musictobelightapi-py3.11) catalunha@pop-os:~/myapp/musictobelight/musictobelightapi$ poetry add djangorestframework
Using version ^3.14.0 for djangorestframework

Updating dependencies
Resolving dependencies... (2.3s)

Package operations: 2 installs, 0 updates, 0 removals

  • Installing pytz (2023.3.post1)
  • Installing djangorestframework (3.14.0)

Writing lock file
(musictobelightapi-py3.11) catalunha@pop-os:~/myapp/musictobelight/musictobelightapi$ django-admin startproject project .
(musictobelightapi-py3.11) catalunha@pop-os:~/myapp/musictobelight/musictobelightapi$ cd project/
(musictobelightapi-py3.11) catalunha@pop-os:~/my
(musictobelightapi-py3.11) catalunha@pop-os:~/my
(musictobelightapi-py3.11) catalunha@pop-os:~/myapp/musictobelight/musictobelightapi/project$ d
(musictobelightapi-py3.11) catalunha@pop-os:~/myapp/musictobelight/musictobel
ightapi/project$ django-admin start accounts
No Django settings specified.
Unknown command: 'start'. Did you mean startapp?
Type 'django-admin help' for usage.
(musictobelightapi-py3.11) catalunha@pop-os:~/myapp/musictobelight/musictobelightapi/project$ django-admin startapp accounts
(musictobelightapi-py3.11) catalunha@pop-os:~/myapp/musictobelight/musictobelightapi/project$ 
