####How to build and run the application randon-cat-app on flask


Project sructure:

-flask-app

 --templates
 
   --index.html
   
 --app.py
 
 --Dockerfile

1. Download and install Docker Desktop

2. Build the image with command:
    docker build -t random-cat-app .

3. Run the container with command:
   docker run -p 8866:5001 --name random-cat-app random-cat-app

4. Open the browser

5. Redirect to adress: http://localhost:8866/
