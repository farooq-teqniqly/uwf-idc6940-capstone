# uwf-idc6940-capstone

## R setup

If you see `object 'ffi_list2' not found` when running the time series forecast (e.g. with `geom_line()`), reinstall rlang and ggplot2 using binaries:

```r
install.packages("rlang", type = "binary")
install.packages("ggplot2", type = "binary")
```

Restart R after installing, then re-run the document.
