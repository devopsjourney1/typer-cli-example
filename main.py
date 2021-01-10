import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

@app.command()
def goodbye(name: str, iq: int, display_iq: bool = False):
    if display_iq:
        typer.echo(f"Goodbye {name} who has {iq} IQ ")
    else:
        typer.echo(f"Goodbye {name}")


if __name__ == "__main__":
    app()