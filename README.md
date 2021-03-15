# Deep Learning in Virtual Screening: Recent Applications and Developments
## Review

- Talia B. Kimber
- Yonghui Chen
- Andrea Volkamer

[![Actions Status](https://github.com/volkamerlab/DL_in_VS_review/workflows/CI/badge.svg)](https://github.com/volkamerlab/DL_in_VS_review/actions)

#### Content

This repository provides 
   * the code to produce all subfigures (generated programmatically), as well as
   * the final figures in the review.

The folder *image_generation* holds the following information: 
   * ligand_encoding: scripts to produce ligand encoding examples
   * complex_encoding: scripts to produce complex encoding examples
   * review_images: composed review figures

Check out more of our work at [Volkamer Lab](https://volkamerlab.org/).


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
