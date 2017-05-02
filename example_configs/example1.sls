{% set install_prefix = salt['grains.get']('conda:install_prefix', salt['pillar.get']('conda:install_prefix', '/opt/anaconda/'))  %}

libgeos-dev:
  pkg.installed

ais-analysis-install:
  pip.installed:
    - name: git+https://jrcoyle@bitbucket.org/ICCTnaya/ais_analysis.git
    - bin_env: {{ install_prefix }}/bin/pip
    - require:
      - pkg: libgeos-dev


