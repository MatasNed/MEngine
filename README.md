# Context

* There are various files that explain high-level design
* MEngine HDL of the idea and LLD of the design

To run the project you need two things
1. In MEngine foldder click run in IDE, it will run __init__.py of the project
2. Setup a target backend for forwarding requests ``python -m SimpleHTTPServer 9000``

Later on we need application to forward this to probably Django.


# ConnectionManager
Every call is a blocking call, the idea is to use threads to block the threads and continue to listen indefinetely