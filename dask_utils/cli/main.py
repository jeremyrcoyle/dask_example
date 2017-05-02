import click
import dask_utils


def start():
  import sys
  import logging
  import traceback

  try:
    cli(obj={})
  except DaskEc2Exception as e:
    click.echo("ERROR: %s" % e, err=True)
    sys.exit(1)
  except ClientError as e:
    click.echo("Unexpected EC2 error: %s" % e, err=True)
    sys.exit(1)
  except KeyboardInterrupt:
    click.echo("Interrupted by Ctrl-C. One or more actions could be still running in the cluster")
    sys.exit(1)
  except Exception as e:
    click.echo(traceback.format_exc(), err=True)
    sys.exit(1)


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(prog_name="dask_utils", version=dask_utils.__version__)
@click.pass_context
def cli(ctx):
  ctx.obj = {}


@cli.command(short_help="Start Cluster")
@click.pass_context
@click.option("--config",
              required=True,
              type=click.Path(exists=True),
              help="Cluster definition")
def up(ctx, config):
  click.echo("Launching nodes")