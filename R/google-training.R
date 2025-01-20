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

