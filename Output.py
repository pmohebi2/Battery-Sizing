import pyomo.environ as pyo
import matplotlib.pyplot as plt
import pandas as pd
def save_and_plot_results(model):
    # Extract results
    B_State_values = [pyo.value(model.B_State[t]) for t in model.T]
    Charge_R_values = [pyo.value(model.Charge_R[t]) for t in model.T]
    Discharge_R_values = [pyo.value(model.Discharge_R[t]) for t in model.T]
    Grid_I_values = [pyo.value(model.Grid_I[t]) for t in model.T]
    Grid_E_values = [pyo.value(model.Grid_E[t]) for t in model.T]

    # Prepare data for CSV
    results_df = pd.DataFrame({
        'Time Period': list(model.T),
        'B_State': B_State_values,
        'Charge_R': Charge_R_values,
        'Discharge_R': Discharge_R_values,
        'Grid_I': Grid_I_values,
        'Grid_E': Grid_E_values
    })

    # Add capacity and execution time to the DataFrame
    results_df['Max_Cap'] = max_cap_value
    results_df['Execution_Time'] = execution_time
    
    # Save results to CSV
    results_df.to_csv('battery_optimization_results.csv', index=False)

    # Plot results
    plt.figure(figsize=(12, 10))

    plt.subplot(4, 1, 1)
    plt.plot(results_df['Time Period'], results_df['B_State'], label='Battery State', color='blue')
    plt.title('Battery State Over Time')
    plt.xlabel('Time Period')
    plt.ylabel('Battery State (kW)')
    plt.grid()
    plt.legend()

    plt.subplot(4, 1, 2)
    plt.plot(results_df['Time Period'], results_df['Charge_R'], label='Charge Rate', color='green')
    plt.title('Charge Rate Over Time')
    plt.xlabel('Time Period')
    plt.ylabel('Charge Rate (kW)')
    plt.grid()
    plt.legend()

    plt.subplot(4, 1, 3)
    plt.plot(results_df['Time Period'], results_df['Discharge_R'], label='Discharge Rate', color='red')
    plt.title('Discharge Rate Over Time')
    plt.xlabel('Time Period')
    plt.ylabel('Discharge Rate (kW)')
    plt.grid()
    plt.legend()

    plt.subplot(4, 1, 4)
    plt.plot(results_df['Time Period'], results_df['Grid_I'], label='Grid Import', color='orange')
    plt.plot(results_df['Time Period'], results_df['Grid_E'], label='Grid Export', color='purple')
    plt.title('Grid Import and Export Over Time')
    plt.xlabel('Time Period')
    plt.ylabel('Energy (kW)')
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.savefig('battery_results_plot.png')
    plt.show()
