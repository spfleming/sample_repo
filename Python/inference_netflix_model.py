load("models/netflix_mod.rds")

dat$preds <- predict(netflix.mod, new.data = dat)