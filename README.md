# uwf-idc6940-capstone

## R packages (both QMD files)

Install the following in R so that `code/time_series_forecast.qmd` and `code/lstm_forecast.qmd` run:

```r
# Time series & ARIMA
install.packages(c("forecast", "tseries"))

# Plotting & data
install.packages(c("ggplot2", "scales", "dplyr", "tidyr"))

# Evaluation metrics (sMAPE, MASE)
install.packages(c("Metrics", "yardstick"))
```

- **time_series_forecast.qmd** uses: `forecast`, `tseries`, `ggplot2`, `scales`, `dplyr`, `Metrics`, `yardstick`.
- **lstm_forecast.qmd** also uses: `keras`, `tensorflow` (see below), `tidyr`.

## R setup (ggplot2 / rlang)

If you see `object 'ffi_list2' not found` when running the time series forecast (e.g. with `geom_line()`), reinstall rlang and ggplot2 using binaries:

```r
install.packages("rlang", type = "binary")
install.packages("ggplot2", type = "binary")
```

Restart R after installing, then re-run the document.

## TensorFlow (for LSTM forecast)

To run `code/lstm_forecast.qmd` you need TensorFlow and Python installed for R. Follow [TensorFlow for R - Quick start](https://tensorflow.rstudio.com/install/). In R, run:

```r
install.packages("remotes")
remotes::install_github("rstudio/tensorflow")
reticulate::install_python()
library(tensorflow)
install_tensorflow(envname = "r-tensorflow")
```

Restart R after installing. To verify: `library(tensorflow); tf_config()`. The default install (Python 3.12, TensorFlow 2.16+) works with the current LSTM code (functional API and direct `$compile`/`$fit`/`$predict` calls).
