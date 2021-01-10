
## Typer

# What is Typer and Typer-Cli

Typer is a library easily build CLI applications.

Typer-Cli is an optional utility to add tab-completion to your scripts.


### Simple Typer application

A simple example

``` shell
import typer

def main(name: str):
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)
```

### A multi-command application
```shell
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
```


###


## Auto completion using Typer-Cli

Instead of packaging your app, you could make use of typer-cli for autocompletion.

### Installing and enabling Typer-Cli
Install Typer-CLI
``` shell
python -m pip install typer-cli
```

Enable auto completion for your terminal (It will auto-detect)

```shell
typer --install-completion
```

### Running app with Typer-Cli

typer .\main.py run goodbye


### Resources:
https://typer.tiangolo.com/
https://typer.tiangolo.com/typer-cli/
