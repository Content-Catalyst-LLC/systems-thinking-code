# Visualize leading and lagging indicators.
ind <- read.csv("../data/processed/indicators.csv")
png("../outputs/figures/leading_lagging_indicators.png", width = 900, height = 600)
plot(ind$month, ind$leading_indicator, type = "b", ylim = range(c(ind$leading_indicator, ind$lagging_indicator)), xlab = "Month", ylab = "Indicator value", main = "Leading and Lagging Indicators")
lines(ind$month, ind$lagging_indicator, type = "b", lty = 2)
legend("bottomright", legend = c("Leading", "Lagging"), lty = c(1, 2), pch = 1)
dev.off()
