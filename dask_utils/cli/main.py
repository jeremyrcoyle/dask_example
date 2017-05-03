from __future__ import print_function, division, absolute_import

import click
import dask_utils
from ..ConfigCluster import ConfigCluster

def start():
  import sys
  import logging
  import traceback

  try:
    cli(obj={})
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
@click.argument('config_file', type=click.Path(exists=True))
def up(ctx, config_file):
  conf_cluster=ConfigCluster.from_config_file(config_file)
  conf_cluster.up()

@cli.command(short_help="SSH to Cluster")
@click.pass_context
@click.argument('config_file', type=click.Path(exists=True))
def ssh(ctx, config_file):
  conf_cluster=ConfigCluster.from_config_file(config_file)
  conf_cluster.ssh()

@cli.command(short_help="Destroy Cluster")
@click.pass_context
@click.argument('config_file', type=click.Path(exists=True))
def destroy(ctx, config_file):
  conf_cluster=ConfigCluster.from_config_file(config_file)
  conf_cluster.destroy()

@cli.command(short_help="Upload State")
@click.pass_context
@click.argument('config_file', type=click.Path(exists=True))
@click.argument('salt_path', type=click.Path(exists=True))
def state(ctx, config_file, salt_path):
  conf_cluster=ConfigCluster.from_config_file(config_file)
  conf_cluster.upload_custom_state(salt_path)

if __name__ == "__main__":
  main()