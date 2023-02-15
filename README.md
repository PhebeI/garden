# Creating a virtual environment for the project
python -m venv my_nlp

# Setting up the Docker Container
docker build -t my_nlp ./
docker run -d -p 80:80 my_nlp


