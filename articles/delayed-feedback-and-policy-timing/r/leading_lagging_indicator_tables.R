# Create a leading-lagging indicator summary table.
ind <- read.csv("../data/processed/indicators.csv")
ind$indicator_gap <- ind$leading_indicator - ind$lagging_indicator
write.csv(ind, "../outputs/tables/leading_lagging_indicator_table.csv", row.names = FALSE)
