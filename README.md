# Deep Learning in Virtual Screening: Recent Applications and Developments
## Review

- Talia B. Kimber
- Yonghui Chen
- Andrea Volkamer

[![Actions Status](https://github.com/volkamerlab/DL_in_VS_review/workflows/CI/badge.svg)](https://github.com/volkamerlab/DL_in_VS_review/actions)

#### Content

This repository was set-up to provide 
   * the code to produce all the parts of the overview figures that were be generated programmatically
   * as well as the review figures.

The folder *image_generation* holds the following information: 
   * ligand_encoding: scripts to produce ligand encoding examples
   * complex_encoding: scripts to produce complex encoding examples
   * review_images: composed review figures

Check out more of our work at [volkamerlab](https://volkamerlab.org/).



#### Conda installation
Create a conda environment:

```console
$ conda env create -f devtools/env.yml
```

Activate the environment:

```console
$ conda activate dl-review
```

Install widgets:
```console
(dl-review)$ jupyter labextension install @jupyter-widgets/jupyterlab-manager nglview-js-widgets
```

Run jupyter lab:
```console
(dl-review)$ jupyter lab
```
