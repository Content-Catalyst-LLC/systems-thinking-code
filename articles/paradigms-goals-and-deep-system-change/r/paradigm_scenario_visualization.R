# Paradigm scenario visualization placeholder.

data_path <- file.path("data", "synthetic_paradigm_assumptions.csv")
paradigms <- read.csv(data_path)
print(paradigms[, c("paradigm_name", "possible_risk")])
