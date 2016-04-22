# 2016-04-21

Got a little bit of the search interface setup, enough to make me realise I've gotten far too used to elastic search and
this project is way too small (and non-commercial) for me to consider ElasticSearch so spent some time this evening
searching for alternatives that are a lot more light weight in terms of server resources. Found out there is a Python
package called [Woosh](https://pypi.python.org/pypi/Whoosh/) which looks pretty good. Documentation for it is
[here](https://whoosh.readthedocs.org/en/latest/). Not going to worry about trying to implement it right now however
instead I'm going to focus on actually getting some data for this and just storing it in mySQL with simple search..
Later on I'll add in woosh! WOOOSH! ^_^

# 2016-04-13

Kind of burned out and finding it hard to actually get to the data processing side of this.

- Category page useless, send to faceted search instead.
- Going to get data from USA initially.
- Need to build admin area to input basic info about charity and then start harvest of data.
- Zero idea on how I'm actually going to programatically work through these PDF's and store as records right now.
      Need a way to store that will work for any country rather than jusdt being USA/Form 990 specific.

# 2016-04-06

I've realised that just getting IRS 990s while okay is not perfect as most organisations operate in multiple countries
so not all their income and spending is reflected in just the IRS 990. So now I'm going to proceed with initially using
the 990's but will have to get global data alot sooner than anticipated.