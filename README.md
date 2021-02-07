# gscrapper

gscrapper is a Django application for scrapping google.

## Installation

Clone the repository.

```bash
git clone https://github.com/blackhold/gscrapper.git
```

Place to project directory, create virtualenv and activate virtualenv.

```bash
cd gscrapper
virtualenv -p python3.7 venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run gscrapper

```bash
python manage.py runserver 0.0.0.0:5001
```

Access to gscrapper

[http://localhost:5001](http://localhost:5001)

## Test in Docker

Alternatively, you can test it inside a Docker container without having to install additional dependencies in your local computer.

Build the image

```
docker build -t gscrapper .
```
Run the container

```
docker run -dit --name gscrapper-container -p 5001:5001 gscrapper
```

Access to gscrapper as usual, by typing the following URL in the browser

[http://localhost:5001](http://localhost:5001)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
