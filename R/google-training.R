#  https://posit.cloud/content/yours?sort=name_asc


# tidyverse_update()
# update.packages()
# install.packages("name...")
print("hi")

x <- c(1,2,4)

is.integer(x)
typeof(x)

y <- list(12,"text",34)
typeof(y)

# structure (str)




str(y)


install.packages("tidyverse")
library(tidyverse)
# https://rawgit.com/rstudio/cheatsheets/master/lubridate.pdf
# https://lubridate.tidyverse.org/index.html
library(lubridate)
t1 <- now()

t1

m <- matrix(c(1:6), nrow = 2)
m


# files -- https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/files


x <- 3.5
x
!x

x <- 0
!x

if ( x == 0){
  print("x equals zero")
} else if( 12 == 13){
  print("whooops...")
}

# find packages installed

installed.packages()

# base ready to use
# recommended - installed - not loaded

# to load --
#library(name-of-package)

# CRAN  -  comprehensive R Archive ---


# make your own r package   https://r-pkgs.org/


# ggplot2 - data viz, plots, 
# tidyr - used for data  (data frame) cleaning to make your data tidy
# dplyr -consistent set of functions for common data manipulation; select, filter,
# readr  - importing data read_csv()
# tibble -- data frames
# purrr  -- functions and vectors
# stringr -- working with strings
# forcats -- common problems with factors (categorical data)


# PIPES

#  %>%  


library(lubridate)
ymd("2021-01-20")
