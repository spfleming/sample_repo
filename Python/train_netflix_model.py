netflix.mod <- lm(movieLength ~ years, data = netflix_clean)

save(netflix.mod, "models\netflix_mod.rds")