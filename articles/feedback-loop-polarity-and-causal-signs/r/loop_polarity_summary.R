# Summarize reinforcing and balancing loop counts.
loops <- read.csv("data/synthetic_feedback_loops.csv")
print(table(loops$loop_polarity))
