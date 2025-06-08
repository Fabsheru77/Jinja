def movie_stars(movie_dict):
  for movie in movie_dict:
    movie["stars"] = add_stars(movie["rating"])
  return movie_dict

def add_stars(rating):
  my_return = ""
  for x in range(5):
   #/ x+=1 # Line # 9 and 10 are working togather#/
    #/checked = "checked" if rating >= x else ""# use > x /
    checked = "checked" if rating > x else ""
    my_return += f"<span class=\"fa fa-star {checked}\"></span>"
  return my_return