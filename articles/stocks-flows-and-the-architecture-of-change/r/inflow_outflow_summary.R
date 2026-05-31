# Summarize net flow by stock.
root <- normalizePath(file.path(getwd(), "articles", "stocks-flows-and-the-architecture-of-change"), mustWork = FALSE)
if (!dir.exists(root)) root <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)
flows <- read.csv(file.path(root, "data", "synthetic_system_flows.csv"))
flows$signed_rate <- ifelse(flows$flow_type == "inflow", flows$baseline_rate, -flows$baseline_rate)
print(aggregate(signed_rate ~ stock_id, data = flows, sum))
