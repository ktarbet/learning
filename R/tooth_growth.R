# tooth growth in guinna pigs
#  https://rpubs.com/dsasas/tooth

data("ToothGrowth")
browseVignettes("ToothGrowth")
View(ToothGrowth)


install.packages("dplyr")
library(dplyr)
f_tg <- filter(ToothGrowth, dose == 0.5)

arrange(f_tg, len)

distinct_items <- unique(ToothGrowth$supp)
print(distinct_items)

f <- ToothGrowth %>%  
  filter(dose == 0.5) %>% 
  arrange(len)

f