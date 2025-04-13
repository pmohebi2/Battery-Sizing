import pyomo.environ as pyo
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def save_and_plot_results(model):
    # Extract results
    B_State_values = [pyo.value(model.B_State[t]) for t in model.T]
    Charge_R_values = [pyo.value(model.Charge_R[t]) for t in model.T]
    Discharge_R_values = [pyo.value(model.Discharge_R[t]) for t in model.T]
    Grid_I_values = [pyo.value(model.Grid_I[t]) for t in model.T]
    Grid_E_values = [pyo.value(model.Grid_E[t]) for t in model.T]
    Grid_IMax_values = [pyo.value(model.Grid_IMax[m]) for m in model.M]

    # Prepare data for CSV
    results_df = pd.DataFrame({
        'Time Period': list(model.T),
        'B_State': B_State_values,
        'Charge_R': Charge_R_values,
        'Discharge_R': Discharge_R_values,
        'Grid_I': Grid_I_values,
        'Grid_E': Grid_E_values,
    })
    
    # Save results to CSV
    results_df.to_csv('battery_optimization_results.csv', index=False)

    # Plot results
    plt.figure(figsize=(12, 10))

    plt.subplot(4, 1, 1)
    plt.plot(results_df['Time Period'], results_df['B_State']/1000, label='Battery State', color='blue')
    plt.title('Battery State Over Time')
    plt.xlabel('Time Period (Hour)')
    plt.ylabel('Battery State (MWh)')
    plt.grid()
    plt.legend()

    plt.subplot(4, 1, 2)
    plt.plot(results_df['Time Period'], results_df['Charge_R']/1000, label='Charge Rate', color='green')
    plt.plot(results_df['Time Period'], results_df['Discharge_R']/1000, label='Discharge Rate', color='red')
    plt.title('Charge and Discharge Rates Over Time')
    plt.xlabel('Time Period (Hour)')
    plt.ylabel('Charge/Discharge Rate (MW)')
    plt.grid()
    plt.legend()

    plt.subplot(4, 1, 3)
    plt.plot(results_df['Time Period'], results_df['Grid_I']/1000, label='Grid Import', color='orange')
    plt.plot(results_df['Time Period'], results_df['Grid_E']/1000, label='Grid Export', color='purple')
    plt.title('Grid Import and Export Over Time')
    plt.xlabel('Time Period (Hour)')
    plt.ylabel('Grid Import/Export (MW)')
    plt.grid()
    plt.legend()

    Grid_IMax_scaled = np.array(Grid_IMax_values) / 1000

    plt.subplot(4, 1, 4)  # Peak Demand Charge
    plt.plot(range(1,len(Grid_IMax_values)+1), Grid_IMax_scaled, label='Peak Demand Charge', color='cyan')
    plt.scatter(range(1, len(Grid_IMax_values) + 1), Grid_IMax_scaled, color='k')
    plt.title('Peak Demand Charge Over Time')
    plt.xlabel('Months')
    plt.ylabel('Peak Demand Charge (MW)')
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.savefig('battery_results_plot.png')
    plt.show()
