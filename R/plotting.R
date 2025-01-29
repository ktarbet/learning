# Aesthetics   - visual property of object in your plot (size,shape,color of points)
# Geom    - geometric object used to represent your data (point, bar, line,..)
# Facets - display smaller groups, subsets (sub plots)
# Label and Annotate -- titles, captions, highligh data


#  https://ggplot2.tidyverse.org/

install.packages('ggplot2') 
install.packages('palmerpenguins')
library(ggplot2)
library(palmerpenguins)
View(penguins)

ggplot(data = penguins) + geom_point(mapping = aes(x = flipper_length_mm, y = body_mass_g))


# aes   is aesthetic mappings 

library(tibble)
f <- function(n) {
  return(seq(1, n) ^ 2)   
}
set.seed(123)  # For reproducibility
df <- tibble(
  timestamp = seq.POSIXt(from = Sys.time(), by = "hour", length.out = 20),
  value = f(20)
)


ggplot(data = df) + geom_point(mapping = aes(x=timestamp, y=value))



