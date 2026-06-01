# Capacity erosion table.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = TRUE)
df <- read.csv(file.path(root, "data", "synthetic_capacity_stocks.csv"))
df$capacity_change_from_start <- df$capacity_stock - df$capacity_stock[1]
write.csv(df, file.path(root, "outputs", "tables", "capacity_erosion_table.csv"), row.names = FALSE)
print(tail(df, 3))
