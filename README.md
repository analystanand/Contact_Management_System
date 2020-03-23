## Web Application for Managing Contact List
### Features
- Contact Display Window
- Contact Search
- Adding New Contacts
- Modifying / Deleting Existing Contacts

### Platform Details :Exported from Conda
``Language: Python``
``Framework: Django``
``OS: Ubuntu 18.04/linux-64``

``python version : 3.7.4.final.0``

`` conda version : 4.8.2``


## Requirements

#### 
```
name: contact_management
channels:
  - defaults
dependencies:
  - _libgcc_mutex=0.1=main
  - asgiref=3.2.3=py_0
  - ca-certificates=2020.1.1=0
  - certifi=2019.11.28=py38_0
  - django=3.0.3=py_0
  - ld_impl_linux-64=2.33.1=h53a641e_7
  - libedit=3.1.20181209=hc058e9b_0
  - libffi=3.2.1=hd88cf55_4
  - libgcc-ng=9.1.0=hdf63c60_0
  - libstdcxx-ng=9.1.0=hdf63c60_0
  - ncurses=6.2=he6710b0_0
  - openssl=1.1.1e=h7b6447c_0
  - pip=20.0.2=py38_1
  - python=3.8.1=h0371630_1
  - pytz=2019.3=py_0
  - readline=7.0=h7b6447c_5
  - setuptools=46.0.0=py38_0
  - sqlite=3.31.1=h7b6447c_0
  - sqlparse=0.3.0=py_0
  - tk=8.6.8=hbc83047_0
  - wheel=0.34.2=py38_0
  - xz=5.2.4=h14c3975_4
  - zlib=1.2.11=h7b6447c_3
prefix: /home/user/anaconda3/envs/contact_management
```

## How to build the application and run 
*  Create virtual environment using environment.yml.``conda env create -f environment.yml``

* Alternatively Create [Virtual Environment](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/)  and use requirements.txt. (prefered for *windows*)
``pip install -r requirements.txt``

* Change directory to contact and Run below given command for running server and access http://localhost:8000/ in browser.
``python manage.py runserver``
