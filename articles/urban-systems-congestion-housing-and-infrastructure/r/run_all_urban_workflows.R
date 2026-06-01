# Run all base R urban systems workflows with safe path handling.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = FALSE)
  root_dir <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
} else {
  cwd <- normalizePath(getwd(), mustWork = FALSE)
  if (basename(cwd) == "r") {
    root_dir <- normalizePath(file.path(cwd, ".."), mustWork = FALSE)
  } else {
    root_dir <- cwd
  }
}

old_wd <- getwd()
setwd(root_dir)
on.exit(setwd(old_wd), add = TRUE)

if (!file.exists(file.path("outputs", "tables", "urban_systems_timeseries.csv"))) {
  py <- Sys.which("python3")
  if (py == "") py <- Sys.which("python")
  if (py != "") {
    system2(py, file.path("python", "urban_systems_model.py"))
  }
}

source(file.path("r", "urban_systems_diagnostics.R"), local = TRUE)
cat("\nAll base R urban systems workflows completed.\n")
