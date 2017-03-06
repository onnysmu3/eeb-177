
cocoli.dat
sizes_in_94 <- cocoli_dat$dbh1
names(sizes_in_94) <- cocoli_dat$tag
sizes_in_94["000009"]
sizes_in_94[c("000009", "000099")]

hist(sizes_in_94, xlab = "DBH (mm)", main = "Distribution of tree sizes in Cocoli (1994)")

plot(x = sizes_in_94, y = sizes_in_97, main = "Scatter plot of sizes" 
     xlab = "Size in 1994 (mm)", ylab = "Size in 1997 (mm)", pch = 19, col = "darkgreen")

```{r}
library(dplyr)


# %>% is identical to the   |  in terminal
cocoli.dat
sizes_in_94 %>% filter(sizes_in_94)

cocoli_dat
cocoli_dat %>% filter(dbh1 > 0) %>% arrange(-dbh1)

?plot
cocoli_dat %>% filter(dbh1 > 0) %>% group_by((spcode)) %>% 
  summarize(mean_dbh_1994 = mean(dbh1))

cocoli_dat %>% filter(dbh1 > 0) %>% group_by((spcode)) %>% 
  summarize(sum_dbh_1994 = sum((dbh1/2)^2*pi)) %>% arrange(-area_dbh_)