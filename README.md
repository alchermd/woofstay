# woofstay

Pet boarding management application

## Development

### Requirements

`woofstay` assumes Docker is installed on the developer's machine

### Getting Started

```console
$ cp .env.example .env # edit as necessary
$ docker compose up --build
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 12, 2023 - 02:13:04
Django version 4.1.7, using settings 'config.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C
```

To run administrative commands, open up another terminal window and use `docker compose exec django`. Example:

```console
$ docker compose exec django python manage.py migrate
```

### Running the test suite

```console
$ docker compose exec django python manage.py behave
```