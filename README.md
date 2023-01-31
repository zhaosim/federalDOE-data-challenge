# Code test for data engineering candidates

## Steps to use the images in the git repo

1. Install Docker

    Make sure you have a recent version of Docker. 

    Follow directions here: https://docs.docker.com/get-docker/.
2. Build the images included in this git repo
    
    This will build all of the images referenced in the Docker Compose file. You will need to re-run this after making code changes. To build, run 
    ```
    docker compose build
    ```

3. Starting MySql

    a. To start up the MySQL database, run the following command. This will will take a short while to run the database’s start-up scripts.
    ```
    docker compose up database
    ```

    b. Optional: If you want to connect to the MySQL database via the command-line client, run the following command. This may be useful for looking at the database schema or data.
    ```
    docker compose run database mysql --host=database --user=codetest --password=swordfish codetest
    ```

4. Running the scripts
    
    a. Make sure the MySQL database is running, and then load the schema with:
    ```
    docker compose run --no-TTY database mysql --host=database --user=codetest --password=swordfish codetest < schema.sql
    ```

    b. Then make sure that the containers have been built with `docker compose build` and run the program (in directory .\images\python\) with:
    ```
    docker compose run python
    ```
  
5. Cleaning up

    To tidy up, bringing down all the containers and deleting them, run `docker compose down`.
