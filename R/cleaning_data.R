install.packages("tidyverse")
install.packages("skimr")
install.packages("janitor")

library(tidyverse)
library(skimr)
library(janitor)

 
my_path = dirname(rstudioapi::getSourceEditorContext()$path)

# https://stat.ethz.ch/R-manual/R-patched/library/base/html/paste.html

bookings_df <- read_csv(paste(my_path,"/hotel_bookings.csv", sep=''))

head(bookings_df)
str(bookings_df)
glimpse(bookings_df)
colnames(bookings_df)
skim_without_charts(bookings_df)

trimmed_df <- bookings_df %>% 
  select( hotel, is_canceled , lead_time) %>%
  rename( hotel_type = hotel)



example_df <- bookings_df %>%
  select(arrival_date_year, arrival_date_month) %>% 
  unite(arrival_month_year, c("arrival_date_month", "arrival_date_year"), sep = " ")



example_df <- bookings_df %>%
  mutate(guests = adults + children + babies)

head(example_df)


example_df <- bookings_df %>%
  summarize(number_canceled = sum(is_canceled), average_lead_time = ave(lead_time))
  
head(example_df)


# ---- 
hotel_bookings <- read_csv("c:/project/learning/R/hotel_bookings.csv")

head(hotel_bookings)
str(hotel_bookings)
glimpse(hotel_bookings)
colnames(hotel_bookings)
arrange(hotel_bookings, desc(lead_time))
head(hotel_bookings)


hotel_bookings_v2 <-
  arrange(hotel_bookings, desc(lead_time))


head(hotel_bookings_v2)

max(hotel_bookings$lead_time)

min(hotel_bookings$lead_time)
mean(hotel_bookings$lead_time)
