def f(n):
    a = list(primes(10^7))
    b = []
    for num in a:
        b.append(num%n)
    return b

b = f(15)
stats.TimeSeries(b).plot_histogram()

#some other examples
#b = f(16)
#stats.TimeSeries(b).plot_histogram()

#b = f(20)
#stats.TimeSeries(b).plot_histogram()

#b = f(27)
#stats.TimeSeries(b).plot_histogram()


""" For n = 15 it appears that there are an equivalent amount of primes congruent to 1,2,4,7,8,11,13, and 14.
Each of these numbers are coprime with 15. If the primes continue this pattern and there are infintely many primes then we can conclude that there are an infinite amount
of primes which are congruent to any numbers coprime with 15 modulo 15.

After trying a few different numbers we can see that for any n there are 'infinite' primes congruent with a modulo n, so long as a is coprime with n.
There will only be an 'infinite' amount of these numbers if the primes continue to show this behavior for numbers greater than 10^7."""
