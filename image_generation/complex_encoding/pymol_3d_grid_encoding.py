from pathlib import Path
from pymol import cmd
from drawgridbox import drawgridbox

HERE = Path('./')
DATA = HERE / "data"

# load system
cmd.load(DATA / "protein.pdb", "ROCK1")
cmd.load(DATA / "ligand.sdf", "ROCK1_ligand")

# protein
cmd.show_as("cartoon", "*")
cmd.color("white", "ROCK1")

# ligand and pocket residues
cmd.show_as("licorice", "ROCK1_ligand")
cmd.color("pink", "ROCK1_ligand")
cmd.color("atomic", "not element C")
cmd.hide("licorice", "hydro")

# general settings
cmd.bg_colour("white")
cmd.set("ambient", 0.4)
cmd.set("antialias", 1)
cmd.set("ortho", 1)
cmd.set("sphere_mode", 5)
cmd.set("ray_trace_mode", 1)
cmd.set("cartoon_fancy_helices", 1)
cmd.set("cartoon_highlight_color", "grey30")

# draw the grid
## select the range
cmd.select('20A', 'ROCK1_ligand expand 20')
cmd.load('drawgridbox.pml')

# view
cmd.set_view ((
     0.003532045,   -0.998905182,   -0.046578705,
     0.942174196,   -0.012283626,    0.334894955,
    -0.335102588,   -0.045066781,    0.941101432,
    -0.000204355,    0.000496300, -208.231918335,
    53.537849426,  102.745925903,   29.107488632,
   130.434631348,  285.912689209,  -20.000000000 ))

# save pymol session
cmd.save(HERE / "pymol_3d_grid_encoding.pse")
cmd.ray(800, 800)
cmd.png(DATA / "pymol_3d_grid_encoding.png")