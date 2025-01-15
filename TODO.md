1. Parse the request
   1. What request is it GET/POST? (validity) Kernel will drop UDP/otherones anyway
      2. header extraction
         3. both listen and dispatch should be on it's own threads to avoid blocking/sequencing problems
         4. configure a way to setup target backends and write some tests
   2. path? We can target different applications on the backend
   3. fragmented data?
   4. errors?
2. Forward it the request appropriate backend (even it's only 1)
   3. Return the response to the client
3. Threads for each conn?
4. Healthcheck the backend?


----
Nice to have:
* Cache responses
* SSL termination?
* Throttling?