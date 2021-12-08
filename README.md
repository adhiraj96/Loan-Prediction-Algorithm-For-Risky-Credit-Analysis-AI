# Loan Prediction Algorithm For Risky Credit Analysis


## Introduction

ML addresses knowledge based system. It is used in training the data using particular datasets and using the same trained data to test for risky credit models that are developed to predict the needs of attributes based on the outputs of various Machine Learning Algorithms. In particular, it addresses the importance for accuracy while determining credit risks for customers. The data representations can enable the banks to employ measures to increase their economy and reduce the loan debts for the customers. This knowledge based system would be a technological solution to the banking sector for the chronic problems mentioned above.


### Prerequisites


- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [SQLite](https://www.sqlite.org/download.html)


### Installing


The steps are:
 1. [Setting up Virtual Environment](#step-1---setting-up-virtual-environment)
 2. [Installing App](#step-2---installing-app)
 3. [Downloading necessary Python Libraries](#step-3---downloading-necessary-Python-Libraries)
 4. [Setting up SQLite database](#step-4---setting-up-sqlite-database)
 5. [Running the App](#step-5---running-the-app)


### Step 1 - Setting up Virtual Environment


- Open terminal Linux/Unix/Mac or Git bash on windows  create a directory on your system where you will place the project. Let
  the directories name be Project.

```
$ mkdir Project
```

- Now Change directory to Project

```
$ cd path/to/Project
```

- Create a venv directory under project folder.


```
$ mkdir path_to_project/venv
```

- Creating Virtual environmanent.

```
$ python3 -m venv path_to_project/venv
```

- To enable virtual environment for the current terminal type the following command.

```
$  . path_to_project/venv/bin/activate
```


### Step 2 - Installing App

- Extract project .zip file or
- In the terminal type the following command

```
$ git clone https://github.com/AnishaGharat/Loan-Prediction-Application.git
```

This command will pull the latest project files from git repository.


### Step 3 - Downloading necessary Python Libraries 


- Change directory to Loan-Predictor

```
$ cd path_to_project/Loan-Predictor
```

- For installing the required libraries type the following command

```
$ pip3 install -r requirements.txt
```


### Step 4 - Setting up SQLite database


- Run the convrert csv to sql.py file to convert the csv file to SQLite database which is in the Loan-Predictor folder

```
$ python3 convrert csv to sql.py
```


### Step 5 - Running the App

Make current working directory as Loan-Predictor then run the app with the following command.

```
$ cd path_to_project/Loan-Predictor
$ python3 run.py
```

## Versioning

We use [GitHub](http://github.com/) for versioning. Along with [GitKraken](https://www.gitkraken.com) for gui interface

## Authors

* **Anisha Gharat**
* **Gopesh Rajderkar**
* **Samson Anto Paul**


