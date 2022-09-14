## ⚓ Anchor API


## Description

Project to facilitate event users and event creators to manage events, from the place where the event took place to the purchase of a ticket.

ANCHOR YOUR TIME IS WORTH MORE WITH OUR EVENTS!

### Main features

* Separated dev and production settings

* Example app with custom user model

* Bootstrap static files included

* User registration and logging in as demo

* Heroku for easy deployments

* Separated requirements files

* SQLite by default if no env variable is set

## 💻 Prerequisites

Before starting, make sure you've met the following requirements:

* You have installed the latest version of `<python>` and `<pip>`


## 🚀 Install Anchor-API

To install Anchor, follow these steps:

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/matheusprado1/anchor-tcm-m5.git
$ cd anchor-tcm-m5
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/`.

# Website with documentation with api swagger

https://anchor-tcm-m5.herokuapp.com/schema/swagger-ui/


## 📫 Contributing to Anchor-API

To contribute to AnchorApi, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <branch_name> / <local>`
5. Create the pull request.

Alternatively, see the GitHub documentation at [How to create a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Libraries used in the api

[Django-rest-framework][https://www.django-rest-framework.org/]

[Django-filter][https://django-filter.readthedocs.io/]

[Cloudinary][https://cloudinary.com/]

[Geopy][https://geopy.readthedocs.io/]

## Deploy Website

https://anchor-tcm-m5.herokuapp.com/

## 🤝 Collaborators

We thank the following people who contributed to this project:

<table>
  <tr>
    <td align="center">
        <a href="https://github.com/amandaolits" width="100px;" alt="">
          <b>Amanda Oliveira</b>
      </a>
      </br>
          <b>Dev</b>
    </td>
    <td align="center">
        <a href="https://github.com/caiogiffoni" width="100px;" alt="">
          <b>Caio Giffoni</b>
      </a>
      </br>
          <b>Product Owner</b>
    </td>
   <td align="center">
        <a href="https://github.com/jaquemalinoski" width="100px;" alt="">
          <b>Jaqueline Malinoski</b>
      </a>
      </br>
          <b>Dev</b>
    </td>
    <td align="center">
        <a href="https://github.com/matheusprado1" width="100px;" alt="">
          <b>Matheus Prado</b>
      </a>
      </br>
          <b>Tech Lead</b>
    </td>
    <td align="center">
        <a href="https://github.com/paulo-david " width="100px;" alt="">
          <b>Paulo David</b>
      </a>
        </br>
          <b>Dev</b>
    </td>
    <td align="center">
        <a href="https://github.com/talitta-nunes" width="100px;" alt="">
          <b>Talitta Nunes</b>
      </a>
      </br>
          <b>Scrum Master</b>
    </td>
  </tr>
</table>
