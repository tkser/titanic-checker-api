# titanic-checker-api

![Uptime Robot status](https://img.shields.io/uptimerobot/status/m794943788-518f686ad9b5b68a07cbc8ee)

API server for validating predicts of the Titanic dataset.<br />
It is expected to be used with [tkser/titanic-checker-front](https://github.com/tkser/titanic-checker-front).

## Usage
```bash
poetry install
poetry run start
```

## Dataset
This verification is based on the dataset files under the data folder. The data that exists are `train.csv`, `test.csv`, and `test_true.csv`, but only `test_pred.csv` is actually used.

If you prefer to prepare your own dataset, follow the steps below. This will create 3 data files.

```bash
python ./scripts/make_df.py
```

## License

### Data (CSV Files)
The CSV files in the `data` folder of this project are provided under the Attribution 4.0 International ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)) license.

### Code
The code parts (excluding the CSV files) of this project are licensed under the [MIT License](https://github.com/tkser/titanic-checker-api/blob/main/LICENSE).
