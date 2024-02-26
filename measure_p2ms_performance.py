import subprocess
import csv
import sys
import matplotlib.pyplot as plt

# Check for command-line argument for number of runs, default to 1000 if not provided
num_runs = int(sys.argv[2]) if len(sys.argv) > 2 else 1000

def measure_performance(script_file, num_runs):
    exec_cmd = f'./main.py {script_file} 1 {num_runs}'
    result = subprocess.run(exec_cmd, shell=True, capture_output=True, text=True)
    avg_time = float(result.stdout.split()[-2])  # Extract average time from output
    return avg_time

def plot_performance(labels, mapping_times, no_mapping_times):
    plt.figure(figsize=(15, 6))
    indices = range(len(labels))
    
    plt.plot(indices, mapping_times, label='Mapping', marker='o', linestyle='-', color='blue')
    plt.plot(indices, no_mapping_times, label='No Mapping', marker='o', linestyle='-', color='red')

    unique_ms = set(label.split(" of ")[1] for label in labels)
    display_labels = [f"1 of {m}" for m in sorted(unique_ms, key=int)]
                
    display_indices = [labels.index(label) for label in display_labels if label in labels]
    
    plt.xticks(display_indices, display_labels, rotation=45, ha="right")

    plt.xlabel('N of M')
    plt.ylabel('Average Runtime (s)')
    plt.title('P2MS Performance Comparison')
    plt.legend()
    plt.tight_layout()

    plt.savefig("p2ms_performance_comparison.png")
    plt.show()

def main():
    results = [("N of M", "Avg Runtime Mapping (s)", "Avg Runtime No Mapping (s)", "Speed Up Factor")]
    total_mapping_time, total_no_mapping_time, total_factors = 0, 0, 0
    
    num_combinations = 0  # Track the number of N, M combinations
    num_scripts = int(sys.argv[1]) if len(sys.argv) > 1 else 10  # Default to 10 scripts if not specified

    for m in range(1, 16):  # M can be 15 at max
        for n in range(1, m + 1):  # N has to be less than or equal to M
            total_time_mapping, total_time_no_mapping = 0, 0
            for _ in range(num_scripts):  # Generate and execute scripts per combination
                generate_script_cmd = f'./generate_p2ms_script.py {n} {m}'
                subprocess.run(generate_script_cmd, shell=True)
                
                total_time_mapping += measure_performance("p2ms_script_mapping", num_runs)
                total_time_no_mapping += measure_performance("p2ms_script", num_runs)
            
            avg_time_mapping = total_time_mapping / num_scripts
            avg_time_no_mapping = total_time_no_mapping / num_scripts
            speed_up_factor = avg_time_no_mapping / avg_time_mapping if avg_time_mapping else 0
            
            results.append((f"{n} of {m}", avg_time_mapping, avg_time_no_mapping, speed_up_factor))
            total_mapping_time += avg_time_mapping
            total_no_mapping_time += avg_time_no_mapping
            total_factors += speed_up_factor
            num_combinations += 1

    # Calculate overall averages
    overall_avg_mapping = total_mapping_time / num_combinations
    overall_avg_no_mapping = total_no_mapping_time / num_combinations
    overall_speed_up_factor = total_factors / num_combinations

    # Append overall averages to the results
    results.append(("Overall Avg", overall_avg_mapping, overall_avg_no_mapping, overall_speed_up_factor))

    # Write results to CSV
    with open("p2ms_performance.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(results)

    # Generate and show the plot
    plot_performance([r[0] for r in results[1:-1]], [r[1] for r in results[1:-1]], [r[2] for r in results[1:-1]])

if __name__ == "__main__":
    main()
