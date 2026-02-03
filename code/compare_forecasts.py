#!/usr/bin/env python3
"""
Compare ARIMA and LSTM 14-day forecasts: load forecast CSVs and actuals,
compute sMAPE and MASE, and produce a comparison table and plot.

Expects:
  - lstm_forecast_14day.csv: columns date, actual, forecast (LSTM)
  - arima_forecast_14day.csv: columns date, forecast (point forecast)
  - finalproject.csv (optional): for MASE scale (naive one-step MAE on training)

Outputs:
  - Printed table (ARIMA vs LSTM: sMAPE %, MASE)
  - comparison_table.csv and comparison_plot.png in docs/hw4-5/data/ or code/
"""

import argparse
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def smape(actual: np.ndarray, forecast: np.ndarray) -> float:
    """Symmetric MAPE in percent."""
    num = np.abs(actual - forecast)
    denom = (np.abs(actual) + np.abs(forecast)) / 2
    denom[denom == 0] = 1e-8
    return float(np.mean(num / denom) * 100)


def mase(actual: np.ndarray, forecast: np.ndarray, train_naive_mae: float) -> float:
    """MASE scaled by naive one-step MAE on training data."""
    if train_naive_mae == 0:
        return np.nan
    mae_f = np.mean(np.abs(actual - forecast))
    return float(mae_f / train_naive_mae)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare ARIMA and LSTM 14-day forecasts")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "docs" / "hw4-5" / "data",
        help="Directory containing forecast CSVs and optional finalproject.csv",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory for table and plot (default: same as data-dir)",
    )
    args = parser.parse_args()
    data_dir = args.data_dir
    out_dir = args.out_dir or data_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    # Paths
    lstm_path = data_dir / "lstm_forecast_14day.csv"
    arima_path = data_dir / "arima_forecast_14day.csv"
    full_path = data_dir / "finalproject.csv"

    if not lstm_path.exists():
        print(f"LSTM forecast not found: {lstm_path}")
        print("Run lstm_forecast.qmd first and ensure it writes lstm_forecast_14day.csv to docs/hw4-5/data/.")
        return

    # Load LSTM (has date, actual, forecast)
    lstm = pd.read_csv(lstm_path)
    lstm["date"] = pd.to_datetime(lstm["date"])
    actual = lstm["actual"].values
    lstm_forecast = lstm["forecast"].values
    dates = lstm["date"]

    # Naive one-step MAE on training (all but last 14)
    if full_path.exists():
        full = pd.read_csv(full_path)
        full["pickup_date"] = pd.to_datetime(full["pickup_date"])
        full = full.sort_values("pickup_date")
        train_vals = full["avg_duration_min"].values[:-14]
        train_naive_mae = float(np.mean(np.abs(np.diff(train_vals))))
    else:
        train_vals = actual  # fallback: use test period (wrong scale but avoids crash)
        train_naive_mae = float(np.mean(np.abs(np.diff(actual))))
        if len(actual) < 2:
            train_naive_mae = 1.0

    # LSTM metrics
    lstm_smape = smape(actual, lstm_forecast)
    lstm_mase = mase(actual, lstm_forecast, train_naive_mae)

    # Load ARIMA if present
    merge = None
    if arima_path.exists():
        arima = pd.read_csv(arima_path)
        date_col = "Date" if "Date" in arima.columns else "date"
        arima["date"] = pd.to_datetime(arima[date_col])
        fc_col = None
        for c in ("forecast", "point_forecast", "Point Forecast"):
            if c in arima.columns:
                fc_col = c
                break
        if fc_col is None:
            fc_col = [x for x in arima.columns if x.lower() != "date"][0]
        arima_fc_col = "arima_forecast"
        arima_renamed = arima[["date", fc_col]].rename(columns={fc_col: arima_fc_col})
        merge = lstm[["date", "actual"]].merge(arima_renamed, on="date", how="inner")
        if len(merge) == 0:
            print("Warning: no common dates between LSTM and ARIMA; check date formats.")
            arima_smape = arima_mase = np.nan
            arima_plot_dates = arima_forecast = None
        else:
            actual_aligned = merge["actual"].values
            arima_forecast = merge[arima_fc_col].values
            arima_plot_dates = merge["date"].values
            arima_smape = smape(actual_aligned, arima_forecast)
            arima_mase = mase(actual_aligned, arima_forecast, train_naive_mae)
    else:
        print(f"ARIMA forecast not found: {arima_path}")
        print("Export ARIMA 14-day point forecast to arima_forecast_14day.csv (columns: date, forecast).")
        arima_smape = arima_mase = np.nan
        arima_plot_dates = arima_forecast = None

    # Table
    rows = [
        ("ARIMA", arima_smape, arima_mase),
        ("LSTM", lstm_smape, lstm_mase),
    ]
    table = pd.DataFrame(rows, columns=["Model", "sMAPE (%)", "MASE"])
    print(table.to_string(index=False))
    table.to_csv(out_dir / "comparison_table.csv", index=False)

    # Plot: actual vs ARIMA vs LSTM
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, actual, "o-", label="Actual", color="#332288", linewidth=1.5)
    ax.plot(dates, lstm_forecast, "s--", label="LSTM forecast", color="#EE7733", linewidth=1)
    if arima_plot_dates is not None and arima_forecast is not None:
        ax.plot(arima_plot_dates, arima_forecast, "^-.", label="ARIMA forecast", color="#009988", linewidth=1)
    ax.set_xlabel("Date")
    ax.set_ylabel("Avg trip duration (minutes)")
    ax.set_title("14-day forecast: Actual vs ARIMA vs LSTM")
    ax.legend(loc="best")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plot_path = out_dir / "comparison_plot.png"
    plt.savefig(plot_path, dpi=150)
    plt.close()
    table_path = out_dir / "comparison_table.csv"
    table.to_csv(table_path, index=False)
    print(f"Saved: {table_path}")
    print(f"Saved: {plot_path}")


if __name__ == "__main__":
    main()
