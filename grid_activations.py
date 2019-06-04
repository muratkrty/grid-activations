import numpy as np
import seaborn as sns

def generate_grids(grid_size = 64):
    ''' Generate grid activations to cover experiment area 
        This function was adapted from the matlab code provided in 
        [1] https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006316
        which is based on 
        [2] https://www.ncbi.nlm.nih.gov/pubmed/17094145
    '''
    grid_env = (grid_size, grid_size)
    spatial_freqs = np.arange(2, 7.5, 0.5)
    n_spatial_freqs = len(spatial_freqs)

    grid =  np.zeros(grid_env, dtype=np.float32)
    pi, inds  = 3.1416, np.arange(1,4)    

    for i in range(n_spatial_freqs):
        sfreq = spatial_freqs[i]
        orientation_step = pi / 3.0
        phase = round(np.random.rand(),4) * pi
        orientation_base =  round(np.random.rand(),4) * pi  # orient_0 from the paper

        ramp1d = np.linspace(-1*pi, pi, grid_size)*sfreq + phase 

        [ramp2d_x, ramp2d_y] = np.meshgrid(ramp1d, ramp1d) # check with matlab manual
        
        for ii in inds:
            orientation = orientation_step * (ii-1) + orientation_base
            rotated_ramp2d = ramp2d_x*np.cos(orientation) + ramp2d_y*np.sin(orientation)
            grating = np.cos(rotated_ramp2d)

            if ii > 1: 
                grid = grid + grating/3.0
            else:
                grid = grating/3.0

        grid = grid * round(2.0/3.0, 4) + round(1.0/3.0, 4)
        grid = np.around(grid, decimals=4)

    return grid

def main():

    grid_area = generate_grids(128)
    ax = sns.heatmap(grid_area, xticklabels=False, yticklabels=False, cbar=False)
    sns.plt.show()

if __name__ == '__main__':
    main()
