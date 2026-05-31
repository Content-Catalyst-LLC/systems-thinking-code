frames <- read.csv("data/raw/synthetic_intervention_frames.csv")
frames$frame_class <- ifelse(frames$redesign_score >= 0.75, "structural redesign", ifelse(frames$redesign_score >= 0.5, "partial", "linear or pressure-based"))
write.csv(frames[order(-frames$redesign_score), ], "outputs/tables/r_intervention_frame_outputs.csv", row.names = FALSE)
cat("Wrote outputs/tables/r_intervention_frame_outputs.csv\n")
