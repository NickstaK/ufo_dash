# data_summary ufo.R
setwd("/home/NickstaK/ufo_dash")

install.packages(c("tidyverse","lubridate","skimr","DataExplorer"))
install.packages("readr")
install.packages("dplyr")

library(tidyverse)     # read/manipulate data
library(lubridate)     # date/time helpers
library(skimr)         # quick tabular summary
library(DataExplorer)# auto-report generator
library(readr)         # read in csv
library(dplyr)         # part of tidyverse

df <- read_csv("/home/NickstaK/ufo_dash/data/raw/complete.csv")

glimpse(df)           # column names, types, first few rows
summary(df)           # min/mean/max for numerics, factor counts
skim(df)              # nice table of missingness, distributions

#create data report
create_report(df,
              output_file = "data/summary_report.html",
              report_title = "UFO Data Overview"
)
