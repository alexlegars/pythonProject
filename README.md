# Global Terrorism API

This API allows you to get terrorists attacks, in json, with all the details of the attacks.

## Initialization

You first have to download the dataset in csv at this [link](https://www.kaggle.com/START-UMD/gtd).<br/>
Or, you can download the csv with this command if you have kaggle installed : <br/>
`kaggle datasets download -d START-UMD/gtd`

Then, put the csv in a folder named "data" that you have to create.

Once you've done this, rename the csv file like this : <br/>
`globalterrorismdb.csv`

To launch the converter from csv to json, launch the parser.py in the console :<br/>
`python csvtojson/parser.py`<br/>
OR <br/>
`python3 csvtojson/parser.py`

## API

To use the API, you have to launch from your console the app.py file :<br/>
`python app.py`<br/>
OR<br/>
`python3 app.py`

Then, go on your browser and type for example :<br/>
[http://127.0.0.1:5000/gt/197000000001](http://127.0.0.1:5000/gt/197000000001)
Then, you will have the result in json of the Terrorist attack with the ID 197000000001

Coming up next:
    - Cleaning of the useless or worthless columns
    - Request by something else than the ID (country or year for instance)
    - Solution to make the search quicker
