article_root <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- "--file="
  script_path <- NULL
  for (arg in args) {
    if (startsWith(arg, file_arg)) {
      script_path <- normalizePath(sub(file_arg, "", arg), mustWork = FALSE)
    }
  }
  if (is.null(script_path)) {
    return(normalizePath(getwd(), mustWork = FALSE))
  }
  return(normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE))
}

ensure_dirs <- function(root) {
  dir.create(file.path(root, "outputs", "tables"), recursive = TRUE, showWarnings = FALSE)
  dir.create(file.path(root, "outputs", "figures"), recursive = TRUE, showWarnings = FALSE)
}

latest_by_scenario <- function(df) {
  do.call(rbind, lapply(split(df, df$scenario), function(x) x[which.max(x$year), ]))
}
