# Basic base-R sign count plot.
edges <- read.csv("data/synthetic_signed_edges.csv")
counts <- table(edges$sign)
png("outputs/causal_sign_counts.png", width = 900, height = 600)
barplot(counts, main = "Causal Sign Counts", xlab = "Sign", ylab = "Count")
dev.off()
