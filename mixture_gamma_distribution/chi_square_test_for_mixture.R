library(MASS)
library(fitdistrplus)

simulate_chi_square <- function(dist_type, alpha1, alpha2, alpha3, beta, n, weight1, weight2, weight3) {
  results <- numeric(1000)
  
  for (i in 1:1000) {
    if (dist_type == "gamma_mixture") {
      # Generate data from a mixture of Gamma distributions
      sample_sizes <- round(n * c(weight1, weight2, weight3))
      samples <- c(rgamma(sample_sizes[1], alpha1, beta),
                   rgamma(sample_sizes[2], alpha2, beta),
                   rgamma(sample_sizes[3], alpha3, beta))
    } else {
      # Generate data from a single distribution type
      samples <- switch(dist_type,
                        "gamma" = rgamma(n, alpha1, beta),
                        "weibull" = rweibull(n, alpha1, beta),
                        "lognormal" = rlnorm(n, alpha1, beta),
                        stop("Unsupported distribution type"))
    }
    
    # Fit a gamma distribution to the generated data
    fit <- fitdist(samples, distr = "gamma", method = "mle", lower = c(0, 0), start = list(scale = 1, shape = 1))
    est_shape <- fit$estimate["shape"]
    est_scale <- fit$estimate["scale"]
    
    # Calculate Chi-square statistic
    hist_info <- hist(samples, breaks = "FD", plot = FALSE)
    observed <- hist_info$counts
    breaks <- hist_info$breaks
    midpoints <- (breaks[-length(breaks)] + breaks[-1]) / 2
    expected <- dgamma(midpoints, est_shape, est_scale) * length(samples) * diff(breaks)

    chi_sq <- sum((observed - expected)^2 / expected)
    results[i] <- ifelse(chi_sq > qchisq(0.95, df = length(observed) - 1), 1, 0)
  }
  
  return(sum(results) / length(results))  # Returning the power of the test
}

# Example usage
power_gamma_mixture <- simulate_chi_square("gamma_mixture", 1, 2, 3, 1, 500, 0.4, 0.3, 0.3)
power_gamma <- simulate_chi_square("gamma", 2, NA, NA, 1, 500, NA, NA, NA)
power_weibull <- simulate_chi_square("weibull", 2, NA, NA, 1, 500, NA, NA, NA)
power_lognormal <- simulate_chi_square("lognormal", 0, NA, NA, 1, 500, NA, NA, NA)

print(power_gamma_mixture)
print(power_gamma)
print(power_weibull)
print(power_lognormal)

