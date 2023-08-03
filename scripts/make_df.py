import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

def main():
    dataset = fetch_openml(data_id=40945, parser="auto")
    df = pd.concat([pd.DataFrame(dataset.data), pd.DataFrame(dataset.target)], axis=1)

    df["passenger_id"] = 0

    original_order = df.columns.tolist()
    new_column_order = ['passenger_id'] + [col for col in original_order if col != 'passenger_id']
    df = df[new_column_order]

    df = df.drop(['boat', 'body', 'home.dest'], axis=1)

    new_column_names = {
        'passenger_id': 'PassengerId',
        'pclass': 'Pclass',
        'name': 'Name',
        'sex': 'Sex',
        'age': 'Age',
        'sibsp': 'SibSp',
        'parch': 'Parch',
        'ticket': 'Ticket',
        'fare': 'Fare',
        'cabin': 'Cabin',
        'embarked': 'Embarked',
        'survived': 'Survived'
    }
    df = df.rename(columns=new_column_names)

    df_train, df_test = train_test_split(df, test_size=0.25, random_state=2023, shuffle=True)

    df_train = df_train.reset_index(drop=True)
    df_train["PassengerId"] = df_train.index + 1

    df_test = df_test.reset_index(drop=True)
    df_test["PassengerId"] = df_train["PassengerId"].max() + df_test.index + 1

    df_test_true = df_test[["PassengerId", "Survived"]]
    df_test = df_test.drop("Survived", axis=1)

    df_train.to_csv("data/train.csv", index=False)
    df_test.to_csv("data/test.csv", index=False)
    df_test_true.to_csv("data/test_true.csv", index=False)

if __name__ == "__main__":
    main()
