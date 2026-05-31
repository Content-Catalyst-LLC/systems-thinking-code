# Administrative burden table summary.
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
input <- file.path(root, "outputs", "tables", "administrative_burden_diagnostics.csv")
out <- file.path(root, "outputs", "tables", "administrative_burden_sorted.csv")
if (file.exists(input)) {
  df <- read.csv(input)
  df <- df[order(-df$contribution), ]
  write.csv(df, out, row.names = FALSE)
  message("Wrote ", out)
} else {
  message("Run python/administrative_burden_diagnostics.py first.")
}
