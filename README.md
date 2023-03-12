# woofstay

Pet boarding management application

## Development

### Requirements

`woofstay` assumes Docker is installed on the developer's machine

### Getting Started

```console
$ docker image build -t alchermd/woofstay .
$ docker container run -v $PWD:/opt/app -p 80:8000 --name woofstay --rm alchermd/woofstay
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 12, 2023 - 02:13:04
Django version 4.1.7, using settings 'config.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C
```

To run administrative commands, open up another terminal window and use `docker container exec`. Example:


```console
$ docker container exec woofstay python manage.py migrate
```