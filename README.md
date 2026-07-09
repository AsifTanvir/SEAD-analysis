SEAD is an unsupervised anomaly detection method for smart IoT environments. It detects and removes anomalous sensor events from historical datasets by analyzing sensor event frequencies within a dynamically selected time window, improving downstream sensor-relationship inference and policy generation.

---

## How It Works

1. **Event frequency computation** — The total number of sensor events within a fixed time window is computed, resampling the raw multivariate binary sensor data into a frequency-based representation.
2. **Anomaly detection** — Isolation Forest is applied to the resampled frequency data to detect anomalous windows without requiring labeled data.
3. **Anomaly removal** — All sensor events within flagged windows are removed from the dataset, producing a clean filtered dataset.
4. **Dynamic window selection** — Algorithm 2 iterates over candidate time windows (1–12 hours), passes each filtered dataset through the SeReIn-M sensor grouping method, and selects the window that maximizes the composite clustering quality score across the Calinski-Harabász (CH), Silhouette (SI), and Davis-Bouldin (DB) metrics.

---

## Evaluation

SEAD is evaluated on three custom smart environment datasets and the public CASAS HH101 dataset using clustering quality metrics:

- **Calinski-Harabász Score** (higher is better)
- **Silhouette Score** (higher is better)
- **Davis-Bouldin Index** (lower is better)

Results are compared against the BTSD baseline across all four testbeds.

---

## Requirements

```
Python 3.8+
scikit-learn
numpy
pandas
```

---

## Usage

```Jupyter Notebook
# 1. Load your binary sensor event dataset
# 2. Run each notebook for each dataset chronologically

```

---

## Citation

If you use SEAD in your work, please cite:

```
M. A. Tanvir, F. A. Irfan, and R. Iqbal, "SEAD: Sensor Event-Based Anomaly
Detection for Smart Home Automation," in 2025 IEEE 49th Annual Computers,
Software, and Applications Conference (COMPSAC), 2025, pp. 1492–1497.
```

---
