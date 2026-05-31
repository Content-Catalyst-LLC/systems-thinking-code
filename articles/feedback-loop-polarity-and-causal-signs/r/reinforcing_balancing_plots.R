# Basic base-R loop polarity plot.
loops <- read.csv("data/synthetic_feedback_loops.csv")
counts <- table(loops$loop_polarity)
png("outputs/loop_polarity_counts.png", width = 900, height = 600)
barplot(counts, main = "Loop Polarity Counts", xlab = "Loop polarity", ylab = "Count")
dev.off()
