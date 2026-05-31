loops <- read.csv("data/raw/synthetic_feedback_loops.csv")
summary <- aggregate(delay_strength ~ domain + loop_type, data = loops, FUN = mean)
write.csv(summary, "outputs/tables/r_feedback_delay_summary.csv", row.names = FALSE)
cat("Wrote outputs/tables/r_feedback_delay_summary.csv\n")
