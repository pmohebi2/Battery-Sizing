# Battery-Sizing
Our objective is to determine the optimal battery capacity in a grid-connected PV-battery system. The code is organized into several components, all integrated through the  main script.
# Main 
We simply need to run this module which automaticly call others.
# Input
The only variable module is the input, which can be adjusted as needed. This module includes battery features, Time of use, and Net load data (data.csv) for the year, including 8760 hours.
# Optimizer
The optimization process uses the Pyomo library. The objective is to minimize annual cost.
# Output
The results are saved and visualized in the output file.
