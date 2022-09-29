

"""
1. Generate the journal files for up to num_future_dates.
    If YYYY-MM-DD already exists, skip.
    Else:
        Make that file
        Read in an interpolate the variables, pulling a random item from the
        pool of things in the yaml file.
        Commit, and repeat for num_future_dates.

Use re.sub to input in journal prompts and quotes.
Raise error: unrecognised journal item: '...'
Don't forget to document how this all works.

## Stream of consciousness
> What are the thoughts in your mind saying?


## {{prompt}}


## What's one thing you're grateful for?


"""
