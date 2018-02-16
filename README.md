# Log Analysis

Part of Udacity's Full Stack Web Developer Nanodegree

This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

### How to Run?

#### Requirements:
* Python3
* Vagrant
* VirtualBox

#### Setup
1. Clone this repository
2. Download and save `VagrantFile` in the repository by running the following command:
```
curl https://raw.githubusercontent.com/udacity/fullstack-nanodegree-vm/master/vagrant/Vagrantfile
```
*This file is required to launch Vagrant VM*
3. Download and unzip the [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
4. Copy the `newsdata.sql` file from the zip file you downloaded into the repository


#### To Run
1. Launch Vagrant VM by running `vagrant up` command
2. Log in with `vagrant ssh` command
3. Use the command `psql -d news -f newsdata.sql` to connect a database called `news` in your Vagrant VM

There are three tables in this database:
* Authors table: information about the authors of articles
* Articles table: includes the articles themselves
* Log table: included one entry for each time a user has accessed the site

4. Run `python3 log_analysis.py` to get the reports in plain text

