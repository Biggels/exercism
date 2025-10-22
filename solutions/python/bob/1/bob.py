def response(hey_bob):
    hey_bob = hey_bob.strip()
    is_question = hey_bob.endswith("?")
    is_yelled = hey_bob.isupper()
    is_silence = hey_bob == ""
    
    if is_question and is_yelled:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    if is_yelled:
        return "Whoa, chill out!"
    if is_silence:
        return "Fine. Be that way!"
    return "Whatever."