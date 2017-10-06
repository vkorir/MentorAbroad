# given a mentee, return the 3 best matching mentors to the mentee
def find_match(mentee):
    result = [["", 0]] * 3          # [highest, middle, lowest] ==> (key=mentor_id, v=score)

    # will load mentors and mentees from db
    mentors = data["mentors"]
    mentees = data["mentees"]

    keys, weights = ["major", "uni", "country", "home"], [4, 3, 2, 1]       # associate the weight with the categories
    
    # calculate the weight of each mentor to determine their preference
    for me in mentors:
        uni, major, country, home = me["uni"], me["major"], me["country"], me["home"]
        score = 0

        # get the index/position of the mentor's attributes in the metees preference else -1 if not in the list
        get_index = lambda key, val: mentee[key].index(val) if val in mentee[key] else -1
        indices = [get_index("major", major), get_index("uni", uni), get_index("country", country), get_index("home", home)]

        # calculate the mentors weight basing on the mentee's preference list
        for index in range(len(indices)):
            ind = indices[index]
            if ind != -1:
                score += (((len(mentee[keys[index]]) - ind) / len(mentee[keys[index]])) * weights[index]) / 10

        # update the result and maintain the 3 most preferred mentors
        if score > result[0][1]:
            result = [[me["id"], score]] + result
            result = result[:3]
        elif score > result[1][1]:
            result = [result[0], [me["id"], score], result[1]]
        elif score > result[2][1]:
            result = result[1:]
            result.append([me["id"], score])

    return [best[0] for best in result]   # return a list of mentor ids

# sample json data in a dictionary
data = {
    "mentors": [
        {
            "id": "1",
            "uni": "stanford",
            "major": "eecs",
            "country": "usa",
            "home": "kenya"
        },
        {
            "id": "2",
            "uni": "berkeley",
            "major": "cs",
            "country": "usa",
            "home": "drc"
        },
        {
            "id": "3",
            "uni": "mit",
            "major": "eecs",
            "country": "usa",
            "home": "kenya"
        }
    ],
    "mentees": [
        {
            "uni": ["mit", "berkeley", "stanford"],
            "major": ["eecs", "cs"],
            "country": ["usa", "canada"],
            "home": ["kenya"],
            "mentor": None,
            "preference": []
        }
    ]
}