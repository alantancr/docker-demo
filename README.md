# Containerise your Flask applications using Docker and deploy it on Heroku

## Running on Docker

- Build the image with `docker build -t your-app-name .`
- Run the container with `docker run -d -p 5000:5000 -e PORT=5000 --name your-app-server-name your-app-name`
- Check that the container is running
- Go to `localhost:5000`. You should see `Hello, this is a test for Docker image hosting on Heroku.`



## Deploying on Heroku

- Login to Heroku container. It would open the browser and prompt you to login with your Heroku credentials if you are not logged in already. If you are logged in, you will see "Login Succeeded"

  `heroku container:login`

- Creating the application name on Heroku. Make sure you have the 3 files in the same folder.

  `heroku create your-app-name`

- Creating the Heroku container on the app

  `heroku container:push web --app your-app-name`

- Releasing the container on app

  `heroku container:release web --app your-app-name`

- Open your application,  You should see `Hello, this is a test for Docker image hosting on Heroku.`

