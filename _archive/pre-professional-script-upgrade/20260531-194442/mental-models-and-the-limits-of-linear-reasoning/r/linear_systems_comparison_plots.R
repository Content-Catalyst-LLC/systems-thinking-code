models <- read.csv("data/raw/synthetic_mental_models.csv")
models$systems_quality <- with(models, (feedback_score + boundary_score + power_awareness_score + (1 - linear_score)) / 4)
write.csv(models[order(-models$systems_quality), ], "outputs/tables/r_mental_model_quality.csv", row.names = FALSE)
cat("Wrote outputs/tables/r_mental_model_quality.csv\n")
