# supercarers

You can go to: tychosan.pythonanywhere.com/weather/london/<date>/<time>/ 
To see the app in action. 

How to start with Docker. First, ensure you have Docker installed.

Then, build the image when in the project directory:
```
docker build -t supercarers .
```

Use ``` docker image ls ``` to see your built image.

Now run the app with:
```
docker run -p 4000:80 supercarers
```
This maps port 80 of the container to port 4000. So go to:
```
localhost:4000/weather/london/<date>/<time>/
```
To see the app in action.
