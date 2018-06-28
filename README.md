# RecSys-Challenge-2018-creative-track
code used to generate the minrva team's submission to the 2018 RecSys Challenge in the creative track

# Engine:

Apache PredictionIO (http://predictionio.apache.org/) 'similar product template' (https://github.com/apache/predictionio-template-similar-product) with Alternating Least Squares (ALS) algorithm, as implemented in Spark MLlib (https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html); system relied on PostgreSQL 10 (https://www.postgresql.org/) for data persistence.

# Software:

- Python, data load (import-users.py, import-items.py, import-views.py)

- OpenRefine (http://openrefine.org/) with 'conciliator' (https://github.com/codeforkjeff/conciliator) for enrichment of known artist names with VIAF (Virtual International Authority File) to create an association for related artists. 


# Data Set:

VIAF: http://viaf.org/viaf/data/
The Virtual International Authority File (VIAF) is an OCLC service -- built in cooperation with national libraries and other partners -- that virtually combines multiple LAM (Library Archives Museum) name authority files into a single name authority service.


# System:

-  Ubuntu 18.04 LTS (GNU/Linux 4.15.0-20-generic x86_64)
-  java-8-openjdk-amd64
-  128GB RAM, 24 CPU Cores, 2.5 TB SSD
-  psql (10.4 (Ubuntu 10.4-0ubuntu0.18.04))
