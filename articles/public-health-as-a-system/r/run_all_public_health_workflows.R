# Run all base R public health workflows from the article root.
# This runner avoids fragile sys.frame() path logic.

resolve_root <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- "--file="
  script_args <- args[startsWith(args, file_arg)]
  if (length(script_args) > 0) {
    script_path <- normalizePath(sub(file_arg, "", script_args[[1]]), mustWork = FALSE)
    return(normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE))
  }
  cwd <- normalizePath(getwd(), mustWork = FALSE)
  if (basename(cwd) == "r") {
    return(normalizePath(file.path(cwd, ".."), mustWork = FALSE))
  }
  return(cwd)
}

root <- resolve_root()
setwd(root)

needed <- file.path(root, "outputs", "tables", "public_health_system_timeseries.csv")
if (!file.exists(needed)) {
  py_runner <- file.path(root, "python", "run_all_public_health_workflows.py")
  py_bin <- Sys.which("python3")
  if (py_bin == "") py_bin <- Sys.which("python")
  if (file.exists(py_runner) && py_bin != "") {
    cat("Required CSV missing; running Python workflow first...\n")
    status <- system2(py_bin, py_runner)
    if (!identical(status, 0L)) {
      stop("Python workflow failed while preparing R inputs.")
    }
  }
}

if (!file.exists(needed)) {
  stop(paste0("Missing ", needed, ". Run python/run_all_public_health_workflows.py first."))
}

source(file.path(root, "r", "public_health_system_diagnostics.R"), chdir = FALSE)
cat("\nAll base R public health workflows completed.\n")
