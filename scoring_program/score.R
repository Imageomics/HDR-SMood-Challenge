# install packages

library(score4cast) # remotes::install_github("eco4cast/score4cast")
library(jsonlite)  # for JSON I/O

# Read paths
args <- commandArgs(trailingOnly = TRUE)
input_dir  <- args[1]
output_dir <- args[2]

solution_dir <- file.path(input_dir, "ref")
prediction_dir <- file.path(input_dir, "res")

print(paste("Using input_dir:", input_dir))
print(paste("Using solutions:", solution_dir))
print(paste("Using prediction_dir:", prediction_dir))
print(paste("Using output_dir:", output_dir))

# Read solutions
solution_file <- file.path(solution_dir, "ref.csv")
sol_df <- read.csv(solution_file, stringsAsFactors = FALSE)

# Read predictions
prediction_file <- file.path(prediction_dir, "predictions.csv")
pred_df <- read.csv(prediction_file, stringsAsFactors = FALSE)
# Add a new column 'family' with the value 'normal' for all rows
pred_df$family <- "normal"
pred_df$datetime <- sol_df$datetime[match(pred_df$eventID, sol_df$eventID)]
pred_df$site_id <- sol_df$site_id[match(pred_df$eventID, sol_df$eventID)]

# Scoring
# filter sol_df for in-domain (ID) data
sol_id_df <- sol_df[sol_df$domain == "True", ]

# filter pred_df for in-domain (ID) data
pred_id_df <- pred_df[pred_df$eventID %in% sol_id_df$eventID, ]

# calculating crps scoring summary using score4cast package
scoring_id <- score4cast::crps_logs_score(
  target = sol_id_df,
  forecast = pred_id_df)

# print(scoring_id)

# Avg across event
scoring_id_mean = aggregate(crps ~ variable, data = scoring_id, FUN = mean, na.rm = FALSE)

report_id <- setNames(as.list(scoring_id_mean$crps), paste0("in_domain_", scoring_id_mean$variable))

# Do the same for out-of-domain (OOD) data
sol_ood_df <- sol_df[sol_df$domain == "False", ]
pred_ood_df <- pred_df[pred_df$eventID %in% sol_ood_df$eventID, ]
scoring_ood <- score4cast::crps_logs_score(
  target = sol_ood_df,
  forecast = pred_ood_df)
scoring_ood_mean = aggregate(crps ~ variable, data = scoring_ood, FUN = mean, na.rm = FALSE)
report_ood <- setNames(as.list(scoring_ood_mean$crps), paste0("out_of_domain_", scoring_ood_mean$variable))

report <- c(report_id, report_ood) #combine two dictionaries
# Root-Mean-Square aggregation (no normalisation)
rms <- sqrt(mean(unlist(report)^2))
# Append the headline score to the same list
report$rms <- rms

print(report)

# Write the reporting results to a JSON file
output_file <- file.path(output_dir, "scores.json")
write_json(report, output_file, auto_unbox = TRUE)