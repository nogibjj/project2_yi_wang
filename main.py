import pandas as pd
from pandasql import sqldf
import typer
from psycopg2.extras import NamedTupleCursor
from tabulate import tabulate

app = typer.Typer()

@app.command()
def showfline(): 
    """show the fisrt line in dataset"""
    df = pd.read_csv('n_movies.csv', encoding= 'unicode_escape')
    table = df.head(1)
    print("Successfully load dataset")
    print(table)


@app.command()
def showlen():
    """Finding out how many rows dataset has"""
    df = pd.read_csv('n_movies.csv', encoding= 'unicode_escape')
    rows = len(df)
    print("successful load dataset")
    print(rows)


@app.command()
def high_rate():
    """show top 10 high rating movies in list"""
    df = pd.read_csv('n_movies.csv', encoding= 'unicode_escape')
    df = df[df.rating > 9]
    df = df.head(10)
    print(df.title)


@app.command()
def searchtitle():
    """user enter the title, then it will show the info of that movie"""
    df = pd.read_csv('n_movies.csv', encoding= 'unicode_escape')
    title = input("please enter the title you want to search: ")
    title = str(title)
    df = df[df['title'] == title]
    print(df)





if __name__ == "__main__":
    app()