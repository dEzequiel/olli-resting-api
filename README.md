# I'm resting

The README of this branch will explain the instructions that make up the project's Dockerfile. In a quick and simple way I will explain each line and its function.

The slim image is a paired down version of the full image. This image generally only installs the minimal packages needed to run your particular tool. In the case of python, that's the minimum packages to run python

```
FROM python:3.8-slim
```

We upgrade the container Linux system.

```
RUN apt-get update -y
```

With the following two instructions, what we do is establish the container's working directory and copy the files from the root directory where the Dockerfile is located on our local machine to the container's working directory.

The `EXPOSE` statement indicates the ports on which a container listens for connections. Consequently, you must use the traditional common port for your application.

```
EXPOSE 5000/udp
EXPOSE 5000/tcp
```


```
WORKDIR /app
COPY . /app
```

Install the necessary dependencies for the program to work

```
RUN pip install -r requirements.txt
```

The API contains a database and two commands associated with it. The first is `init-db` which initializes the database with a schema and the second, `insert-db`, registers fields within it.

```
RUN flask db init-db
RUN flask db insert-db
```

Execute the API when the container starts.

```
CMD ["flask run", "--host=0.0.0.0", "--port=5000"]
```

Now we can create the image based on our `Dockerfile`.

```
docker build -t olli-resting .
```

And run the container with some extras parameters to allow bash session. Just for debugging purposes.

```
docker run --name olli --rm -i -t olli-resting:latest bash
```

With the container running, we can enter in the bash.

```
docker exec -it olli bash
```