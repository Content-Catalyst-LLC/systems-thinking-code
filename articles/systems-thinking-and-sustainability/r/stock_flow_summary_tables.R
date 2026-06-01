root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
stocks <- read.csv(file.path(root, "data", "synthetic_ecological_stocks.csv"))
outputs <- file.path(root, "outputs", "tables")
dir.create(outputs, recursive = TRUE, showWarnings = FALSE)
summary <- data.frame(
  variable = c("carbon_stock", "groundwater_stock", "biodiversity_index", "soil_health"),
  start_value = c(stocks$carbon_stock[1], stocks$groundwater_stock[1], stocks$biodiversity_index[1], stocks$soil_health[1]),
  end_value = c(tail(stocks$carbon_stock, 1), tail(stocks$groundwater_stock, 1), tail(stocks$biodiversity_index, 1), tail(stocks$soil_health, 1))
)
summary$change <- summary$end_value - summary$start_value
write.csv(summary, file.path(outputs, "stock_flow_summary_table.csv"), row.names = FALSE)
