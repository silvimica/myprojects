library("MASS")
library(fitdistrplus)


real_distr <- c()
result<-c()

fun_chi_square <- function(alpha1,alpha2, alpha3, beta,n,  weight1, weight2, weight3) 
{
  for (x in 1:1000) {   
    
    n<-n
    alpha<- alpha1 
    alpha1<-alpha2
    alpha2<- alpha3
    beta<-beta
    weight1<-weight1
    weight2<-weight2
    weight3<-weight3
    z_theor<- c(rgamma(round(weight1 *n, digits = 0), alpha, beta), rgamma(round(weight2 *n, digits = 0), alpha2, beta), rgamma(round(weight3 *n, digits = 0), alpha1, beta))              #rweibull(n, alpha, beta)        #rlnorm(n, alpha, beta)
    parameters<-fitdist(z_theor, distr = "gamma", method = "mle", lower = c(0, 0), start = list(scale = 1, shape = 1))
    alpha_t = unname(parameters$estimate["shape"])
    
    beta_t =unname(parameters$estimate["scale"])
    theor_max <-qgamma(0.99, alpha_t, beta_t)
    theor_min <- qgamma(0.01, alpha_t, beta_t)
    tiers <- array()
    for (x in 1:10)
    {tiers[x] =  x *(theor_max)/10 }
    observed_counts <- c()
    expected_counts <-c()
    observed_counts[1]=sum(z_theor< tiers[1])
    expected_counts[1]=round(pgamma(tiers[1], alpha_t, beta_t)*n)
    
    for(x in 2:10) {
      observed_counts[x] <- sum(z_theor< tiers[x]) - sum(z_theor< tiers[x-1])
      expected_counts[x] <-round(pgamma(tiers[x], alpha, beta)*n - pgamma(tiers[x-1], alpha, beta)*n, digits=0) 
    }
    
    chi_sq <-sum((observed_counts-expected_counts)^2/expected_counts)
    chi_sq_theor<-qchisq(p=.05, df=length(observed_counts)-1, lower.tail=FALSE)

    if(!is.na(chi_sq)) { 
      real_distr=append(real_distr, TRUE)
      if (chi_sq < chi_sq_theor) {result=append(result, FALSE)  
      } else {
        result=append(result, TRUE)}}
  }
  power <- sum(result)/sum(real_distr)
  return(pr)
  
}

power <-fun_chi_square(1,2,3,1, 500, 0.9, 0.05,0.05)
power
