install.packages("ggplot2")
housing <- read.csv("/home/eeb177-student/Desktop/eeb-177/
                    lab-work/exercise-8_1/Rgraphics/dataSets/
                    landdata-states.csv")
head(housing[1:5])
hist(housing$Home.Value)
library(ggplot2)
ggplot(housing, aes(x = Home.Value)) + geom_histogram()
plot(Home.Value ~ Date, data=subset(housing, State == "MA"))
points(Home.Value ~ Date, col="red", 
       data=subset(housing, State == "TX"))
legend(1975, 400000,
       c("MA", "TX"), title="State",
       col=c("black", "red"),
       pch=c(1, 1))
ggplot(subset(housing, State %in% c("MA", "TX")),
       aes(x=Date,
           y=Home.Value,
           color=State))+
  geom_point()
help.search("geom_", package = "ggplot2")
