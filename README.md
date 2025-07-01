# Multi-Objective Optimization Case Study: NSGA-II vs SMS-EMOA

A comprehensive benchmarking study comparing NSGA-II and SMS-EMOA algorithms on DTLZ test problems using Python and pymoo library.

## Project Overview

This project implements a systematic comparison of two state-of-the-art multi-objective evolutionary algorithms:
- **NSGA-II** (Non-dominated Sorting Genetic Algorithm II)
- **SMS-EMOA** (S-Metric Selection Evolutionary Multi-objective Optimization Algorithm)

The algorithms are evaluated on three continuous DTLZ test functions (DTLZ1, DTLZ2, DTLZ4) with:
- Decision space dimension: 10 variables
- Objective space dimension: 3 objectives
- 30 independent runs per configuration for statistical significance

## Project Structure

```
├── src/
│   ├── algorithms/          # NSGA-II and SMS-EMOA implementations
│   ├── problems/           # DTLZ test problems
│   ├── metrics/            # HV and IGD calculations
│   └── experiments/        # Experiment runner
├── notebooks/
│   └── analysis.ipynb      # Results analysis and visualization
├── results/
│   ├── indicators/         # Performance metrics (CSV)
│   ├── plots/             # Generated visualizations
│   └── raw/               # Raw experimental data
├── environment.yml         # Conda environment
└── README.md
```

## Quick Start

### 1. Environment Setup

Create and activate the conda environment:

```bash
# Create environment from yml file
conda env create -f environment.yml

# Activate environment
conda activate moo25

# Verify installation
python -c "import pymoo; print(f'pymoo version: {pymoo.__version__}')"
```

### 2. Run Benchmark Study

Execute the complete benchmark (this will take several minutes):

```bash
# Run from project root
python -m src.experiments.runner
```

This will:
- Run NSGA-II and SMS-EMOA on DTLZ1, DTLZ2, and DTLZ4
- Execute 30 independent runs per algorithm-problem combination
- Save Pareto fronts and convergence histories
- Compute and record HV (Hypervolume) and IGD (Inverted Generational Distance)
- Save results for later visualization and statistical comparison

### 3. Analyze Results

Open and run the Jupyter notebook for analysis:

```bash
jupyter lab notebooks/analysis.ipynb
```

## Performance Indicators

The benchmark evaluates algorithms using:

- **Hypervolume (HV)**: Volume of objective space dominated by the solution set
- **Inverted Generational Distance (IGD)**: Average distance from true Pareto front
- **Generational Distance (GD)**: Average distance to true Pareto front
- **Spread**: Diversity measure of solution distribution

## Algorithm Configurations

### NSGA-II Parameters
- Population size: 100
- Crossover: SBX with η=15, pc=0.9
- Mutation: Polynomial with η=20
- Generations: 250

### SMS-EMOA Parameters
- Population size: 100
- Crossover: SBX with η=15, pc=0.9
- Mutation: Polynomial with η=20
- Reference point: [1.2, 1.2, 1.2]
- Generations: 250

## Results

Results are automatically saved to:
- `results/indicators/summary.csv` - Main performance metrics
- `results/raw/*.npz` - Individual run Pareto fronts
- `results/plots/*.png` - Generated visualizations

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure conda environment is activated
   ```bash
   conda activate moo25
   ```

2. **Missing Packages**: Reinstall environment
   ```bash
   conda env update --file environment.yml --prune
   ```

3. **Pandas/NumPy Incompatibility**: Force reinstall
   ```bash
   pip uninstall pandas -y
   conda install --force-reinstall pandas numpy
   ```

4. **Permission Errors**: Ensure write access to results directory
   ```bash
   mkdir -p results/{raw,indicators,plots}
   ```

## Dependencies

Core packages:
- Python 3.11
- PyMOO 0.6.1
- NumPy, Pandas, Matplotlib, Seaborn
- Jupyter Lab

## License

Academic use only. Based on course requirements for Multi-Objective Optimization.

## Acknowledgments

- **pymoo** library developers for excellent MOO framework
- Course instructors for guidance and computational resources
- DTLZ benchmark problem developers

---

**Note**: This benchmark study is designed for educational purposes as part of a Multi-Objective Optimization course. Results may vary based on hardware and random seed