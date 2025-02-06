# Aesthetics   - visual property of object in your plot (size,shape,color of points)
# Geom    - geometric object used to represent your data (point, bar, line,..)
# Facets - display smaller groups, subsets (sub plots)
# Label and Annotate -- titles, captions, highligh data


#  https://ggplot2.tidyverse.org/

install.packages('ggplot2') 

install.packages('palmerpenguins')
library(ggplot2)
library(palmerpenguins)

install.packages('tidyverse')
library(tidyverse)

ggplot(data = penguins) +
  geom_point(mapping = 
               aes(x = flipper_length_mm, 
                   y = body_mass_g, 
                   alpha=species))

p <- ggplot(data = penguins) +
  geom_point(mapping = 
               aes(x = flipper_length_mm, 
                   y = body_mass_g, 
                   color=species))+
  labs(title="Palmer Penguins: Body Mass vs. Flipper Length", 
       subtitle="Sample of three Penguin Specie y=s",
       caption="Data Collected by ;: Dr.")+
    annotate("text",x=220,y=3500, label="The Gentoos are the largest", 
    fontface="bold",color="purple", size = 4.5, angle=45)



p+annotate("text",x=220,y=3000,label="check out this")

ggsave("Three_penguin_species.png")


ggplot(data = penguins) +
  geom_point(mapping = 
               aes(x = flipper_length_mm, 
                   y = body_mass_g ), color ="purple")

ggplot(data = penguins) +
  geom_point(mapping = 
               aes(x = flipper_length_mm, 
                   y = body_mass_g, 
                   shape=species, 
                   color=species,
                   size=species))


ggplot(data = penguins) +
  geom_smooth(mapping = 
               aes(x = flipper_length_mm, 
                   y = body_mass_g ), color ="purple")+
  geom_point(mapping = 
                aes(x = flipper_length_mm, 
                    y = body_mass_g ))



ggplot(data = penguins) +
  geom_smooth(mapping = 
                aes(x = flipper_length_mm, 
                    y = body_mass_g , linetype=species))




ggplot(data = penguins) +
  geom_smooth(mapping = 
                aes(x = flipper_length_mm, 
                    y = body_mass_g , linetype=species))


ggplot(data = penguins) +
  geom_jitter(mapping = 
                aes(x = flipper_length_mm, 
                    y = body_mass_g))


# bar chart defaults to counting (rows) on y-axis
ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut, fill=cut))


# stacked bar chart  
ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut, fill=clarity))




ggplot(data = penguins) +
  geom_point(mapping = 
               aes(x = flipper_length_mm, 
                   y = body_mass_g, 
                   shape=species,
                   color=species,
                   size=species))+
  facet_wrap(~species)



ggplot(data = diamonds) +
  geom_bar(mapping = aes(x =color, fill=cut))+
  facet_wrap(~cut)



ggplot(data = diamonds) +
  geom_bar(mapping = aes(x =color, fill=cut))+
  facet_wrap(~clarity)



ggplot(data = penguins,aes(x = flipper_length_mm, y = body_mass_g))+
                    geom_point(aes(color=species)) + 
                   facet_wrap(~species)


# grid with multiple plots.

ggplot(data = penguins)+
  geom_point(mapping=aes(x = flipper_length_mm, y = body_mass_g, color=species))+
  facet_grid(sex~species)

 


ggplot(data = penguins)+
  geom_point(mapping=aes(x = flipper_length_mm, y = body_mass_g, color=species))+
  facet_grid(~sex)




hotel_bookings <- read.csv("hotel_bookings.csv")
ggplot(data = hotel_bookings) +
  geom_bar(mapping = aes(x = distribution_channel))



ggplot(data = hotel_bookings) +
  geom_bar(mapping = aes(x = distribution_channel, fill=market_segment))



ggplot(data = hotel_bookings) +
  geom_bar(mapping = aes(x = distribution_channel, fill=market_segment))+
  facet_wrap(~deposit_type) +
  theme(axis.text.x = element_text(angle = 45))



ggplot(data = hotel_bookings) +
  geom_bar(mapping = aes(x = distribution_channel)) +
  facet_wrap(~market_segment) +
  theme(axis.text.x = element_text(angle = 45))


ggplot(data = hotel_bookings) +
  geom_bar(mapping = aes(x = distribution_channel)) +
  facet_grid(~deposit_type) +
  theme(axis.text.x = element_text(angle = 45))



ggplot(data = hotel_bookings) +
  geom_bar(mapping = aes(x = distribution_channel)) +
  facet_wrap(~deposit_type~market_segment) +
  theme(axis.text.x = element_text(angle = 45))

mindate <- min(hotel_bookings$arrival_date_year)
maxdate <- max(hotel_bookings$arrival_date_year)

ggplot(data = hotel_bookings) +
  geom_bar(mapping = aes(x = market_segment)) +
  facet_wrap(~hotel) +
  labs(title="count , hotel type and market segment",
       caption=paste0("Data From: ",mindate, " to ",maxdate),
       x="market segment", y="number of hotel bookings")

ggsave('hotel_booking_chart.png', width=7,
       height=7)

head(hotel_bookings)

ggplot(data = hotel_bookings) +
  geom_point(mapping = aes(x = lead_time, y = children))

ggplot(data = hotel_bookings) +
  geom_bar(mapping = aes(x = hotel))+
  facet_wrap(~market_segment)


onlineta_city_hotels <- filter(hotel_bookings, 
                               (hotel=="City Hotel" & 
                                  hotel_bookings$market_segment=="Online TA"))



onlineta_city_hotels_v2 <- hotel_bookings %>%
  filter(hotel=="City Hotel") %>%
  filter(market_segment=="Online TA")

ggplot(data = onlineta_city_hotels_v2) +
  geom_point(mapping = aes(x = lead_time, y = children))




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



