# data frames

install.packages("tidyverse")
library(ggplot2)
data(diamonds)
View(diamonds)
head(diamonds)

colnames(diamonds)

library(tidyverse)
# tibbles are immutable.., 

mutate(diamonds,carat_2=carat*100)
x = mutate(diamonds,carat_2=carat*100)
View(x)


names <- c("joe", "fred", "mary", "pat")
age <- c(12,44,19,22)
people <- data.frame(names, age)
head(people)
people
str(people)
glimpse(people)
colnames(people)

m = mutate(people, age_in_20 = age + 20)


# fruits...

fruits <- c("raspberry","strawberry","apple","cantalope","blueberry")
rank  <-  c(1,3,4,5,2)
df = data.frame(fruits,rank)
 

# https://r4ds.had.co.nz/data-import.html

data(mtcars)

readr_example()

read_csv(readr_example("mtcars.csv"))

library(readxl)
readxl_example()         

read_excel(readxl_example("type-me.xlsx"))
excel_sheets(readxl_example("type-me.xlsx"))
x = read_excel(readxl_example("type-me.xlsx"), sheet = "numeric_coercion")


setwd("c:/project/learning/r")
bookings_df <- read_csv("hotel_bookings.csv")
str(bookings_df)
colnames(bookings_df)
new_df <- select(bookings_df, `adr`, adults)
x = mutate(new_df, total = `adr` / adults)

read_csv("hotel_bookings.csv")


install.packages("here")
library("here")
install.packages("skimr")
library("skimr")
install.packages(("janitor"))
library("janitor")
install.packages("dplyr")
library("dplyr")
install.packages("palmerpenguins")
library("palmerpenguins")
skim_without_charts(penguins)
glimpse(penguins)
head(penguins)
skim(penguins)

penguins %>% select(-species)  # all columns except species
penguins %>% select(species)  # only species column

penguins %>% rename(island_new=island)   # rename column name

rename_with(penguins,toupper)   

rename_with(penguins,tolower)   
a = colnames(penguins)
clean_names(penguins)  # names will only have char,numbers, and underscores


# operators --- same as Java/C#  except:

#  %% modulus   a %% b
# integer division   12 %/% 5.6   -> 2

> TRUE & FALSE
# [1] FALSE
> TRUE | FALSE
# [1] TRUE

penguins
library(tidyverse)
penguins %>% arrange(bill_length_mm)  # sort by bill_length_mm
penguins %>% arrange(-bill_length_mm)  # sort descending

penguins2 <- penguins %>% arrange(-bill_length_mm)

# group by island , and summarize.

penguins %>% 
  group_by(island) %>% 
  drop_na() %>% 
  summarise(mean_bill_length_mm = mean(bill_length_mm))

penguins %>% 
  group_by(island) %>% 
  drop_na() %>% 
  summarise(max_bill_length_mm = max(bill_length_mm))


penguins %>% 
  group_by(species, island) %>% 
  drop_na() %>% 
  summarise(max_bl = max(bill_length_mm), mean_bl = mean(bill_length_mm))

penguins %>% filter(species =="Adelie")

