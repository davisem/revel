VariantSearch
=========================
A simple query interface for searching various variant databases, including REVEL

Prerequisites
[Docker](https://docs.docker.com/engine/installation)
[Docker Compose](https://docs.docker.com/compose/install)
sqlite3

Quickstart
==========

Clone Github Repository
-----------------------
```
$ git clone
$ cd variant_search
```

Setup
------------------
```
curl -O https://rothsj06.u.hpc.mssm.edu/revel/revel_all_chromosomes.csv.zip
gunzip
sqlite3 REVEL.db < revel.sql
$ docker-compose up
```

Usage
-----
Navigate to http://0.0.0.0:5000/ in your browser.
