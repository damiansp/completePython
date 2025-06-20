data {
    int<lower=0> N;
    array[N] int<lower=0, upper=1> y;
} 
parameters {
    real<lower=0, upper=1> theta;
}
model {
    theta ~ beta(1, 1);
    y ~ bernoulli(theta);
}
generated quantities {
    array[N] int post_pred;
    vector[N] log_lik;

    for (n in 1:N){
        log_lik[n] = bernoulli_lpmf(y[n] | theta);
        post_pred[n] = bernoulli_rng(theta);
    }
}
