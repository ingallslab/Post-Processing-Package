
from CellProfilerAnalysis.strain.ProcessCellProfilerData import process_data

if __name__ == '__main__':
    input_file = r'C:\Users\aaron\OneDrive - University of Waterloo\Research\Microscope Data Processing\Post-Processing-Package\examples\conjugation\tracking_cells.csv'
    # input_file = '../examples/50-50/50-50_CP_output.csv'
    output_directory = r'C:\Users\aaron\OneDrive - University of Waterloo\Research\Microscope Data Processing\Post-Processing-Package\examples\conjugation'
    # output_directory = '../examples/50-50/outputs'

    # optional parameters
    # unit: hours
    interval_time = 5/60
    # `Average` or `Linear Regression`
    growth_rate_method = "Linear Regression"
    # useful for fixing transition & more than two daughters errors
    number_of_gap = 0
    # convert pixel to um
    um_per_pixel = 0.144
    assigning_cell_type = False
    # for assign cell type
    intensity_threshold = 0.1

    # run post-processing
    process_data(input_file, output_directory, interval_time, growth_rate_method, number_of_gap, um_per_pixel,
                 intensity_threshold, assigning_cell_type)
