from rich import print


def greet(name: str) -> str:
    return f"Hello, {name}!"

def main() -> None:
    print(f"[bold green]{greet('uv')}[/bold green]")
