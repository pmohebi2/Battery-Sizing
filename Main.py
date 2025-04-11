# Imports
import pyomo.environ as pyo
import time
from Input import initialize_data
from optimizer import optimizer
from Output import save_and_plot_results

# import data
file_path = 'data.csv'
Netload_values, Tou_price, battery_cost, roundtrip_efficiency, Rate, self_discharge, \
Projectlife, charge_power_capacity, discharge_power_capacity, electricity_sell_price_ratio, CRF = initialize_data(file_path)

if __name__ == "__main__":
    # Import data
    file_path = 'data.csv'
    Netload_values, Tou_price, battery_cost, roundtrip_efficiency, Rate, self_discharge, \
    Projectlife, charge_power_capacity, discharge_power_capacity, electricity_sell_price_ratio, CRF = initialize_data(file_path)

    # Start time
    start_time = time.time()

    # Call the optimizer
    model = optimizer(Netload_values, Tou_price, battery_cost, roundtrip_efficiency, 
                              Rate, self_discharge, Projectlife, charge_power_capacity, 
                              discharge_power_capacity, electricity_sell_price_ratio, CRF)

    # End time
    end_time = time.time()

    # Save results and plot
    save_and_plot_results(model)

    # Accessing the value of Max_Cap
    max_cap_value = pyo.value(model.Max_Cap)

    # Calculate the total execution time
    execution_time = time.time() - start_time

print("Optimal value of Max_Cap:", max_cap_value)
print(f"Total execution time: {execution_time:.2f} seconds")

