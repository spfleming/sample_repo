url <- "netflix.com"



netflix <- read_html(url) |> as.data.frame() |> 
mutate(mean = mean(movie.length))
