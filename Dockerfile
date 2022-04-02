FROM python:3.10-slim

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir /code/
WORKDIR /code/
ADD rb_fake_repo_creator.py /code/
ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4444

CMD ["./rb_fake_repo_creator.py"]
