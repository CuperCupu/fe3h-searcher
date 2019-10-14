# Fire Emblem Three Houses Gift Guide

Credits to [this google sheet](source-google-doc) and its contributors

This is a simple web app to help you find the correct gifts for the correct character!

## Running

### Parsing data source

Download the datasource as `.xlsx` file

Then run the following command:
```bash
PYTHONPATH=src python src/data_parser fe3h_sheet.xlsx data.json
```
note that `fe3h_sheet.xlsx` is whatever the name of the spreadsheet that you downloaded

### Running the server

#### Using Docker

Build the docker image
```bash
docker build . fe3h
```

Run the docker image
```bash
docker run -p PORT:8080 fe3h
```
note that `PORT` is the port number you want the server to run on

[source-google-doc]: https://docs.google.com/spreadsheets/d/1PCjGLCeHClMaZ43L-H5h6z5I5oz70NA2R7fNANOcwG0