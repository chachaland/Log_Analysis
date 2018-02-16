# Log Analysis

This project is part of Udacity's Full Stack Web Developer Nanodegree. It is to create a reporting tool that prints out reports in plain text based on the data in the database.

### How to Run?

#### Requirements:
* Python3
* Vagrant
* VirtualBox

#### Setup
1. Clone or download [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository
2. Download the [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3. Copy the newsdata.sql file from the zip file you downloaded into the Vagrant sub-directory in the fullstack-nanodegree-vm repository
4. Clone this repository into Vagrant sub-directory as well

#### To Run
1. Launch Vagrant VM by running `vagrant up` command in Vagrant sub-directory
2. Log in with `vagrant ssh` command
3. Use the command `psql -d news -f newsdata.sql` to connect a database called `news` in your Vagrant VM

There are three tables in this database:
* Authors table: information about the authors of articles
* Articles table: includes the articles themselves
* Log table: included one entry for each time a user has accessed the site

4. Run `python3 log_analysis.py` to get the reports in plain text

