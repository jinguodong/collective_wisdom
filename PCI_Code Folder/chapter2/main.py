import recommendations as re

res = re.topMatches(re.critics, 'Lisa Rose')
print res

res_rec = re.getRecommendations(re.critics, 'Toby')
print res_rec

movies = re.transformPrefs(re.critics)
print movies

res_mo = re.topMatches(movies, 'Superman Returns')
print res_mo

res_mo_rec = re.getRecommendations(movies, 'Just My Luck')
print res_mo_rec

print "Simlar"
itemsim = re.calculateSimilarItems(re.critics)
print itemsim

print "Tody"
print re.critics['Toby']

print "rec Items"
res_item_rec = re.getRecommendedItems(re.critics, itemsim, 'Toby')
print res_item_rec