# Lambda + Filter to Get Only Positive Numbers

numbers = [-5, 3, 0, 7, -2, 8]
postive_no=list(filter(lambda x:x>0 , numbers))
print(f"Positive Numbers are {postive_no}")