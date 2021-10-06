import click
import json
from .req import ping_servers as ping
import sys

@click.command()
@click.option("--json-file", "-f", help="Path to json input file")
@click.option("--host", "-s", multiple=True, help="host:port to send the request to")
def cli(host=None, json_file=None):
    if not(host and json_file):
        print("This CLI requires arguments to run. See --help for more information")
        sys.exit(1)

    if json_file:
        try:
            with open(json_file, "r") as f:
                servers = set(json.load(f))
        except:
            print(f"Unable to open file '{json_file}'")
    else:
        servers = set(host)
    
    print(ping(servers))