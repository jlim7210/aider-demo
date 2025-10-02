import typer

app = typer.Typer()

@app.command()
def hi(name: str):
    typer.echo(f"Hi, {name}")

if __name__ == "__main__":
    app()
