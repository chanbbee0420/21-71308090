def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if (maximum_score_index == None) or (search_list[idx] > search_list[maximum_score_index]):
      maximum_score_index = idx
    #  return idx
  return maximum_score_index

def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index

