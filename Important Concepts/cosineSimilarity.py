def cosine(sen1, sen2):

    vec1 = {i: sen1.count(i) for i in sen1.split(" ")}
    vec2 = {i: sen2.count(i) for i in sen2.split(" ")}

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x]*vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x]**2 for x in list(vec2.keys())])
    denominator = sum1**(1/2)*sum2**(1/2)

    if not denominator:
        return 0
    else:
        return float(numerator)/denominator


print(cosine("pepsi is what i like", "i like pepsi"))
