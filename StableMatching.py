import sys
import random
import People

MEN_NAMES = ['albert','bryan','conor','devin','eric','frank','george','herman','iosef','jake','kent']
WOMAN_NAMES = ['alice','beatrix','cassie','denise','ellen','francine','gwen','hellen','ione','jess','kelly']

def create_random_preferences(people):
  preferences = {}
  lpeople = people[:]
  random.shuffle(lpeople)
  for i in range(len(lpeople)):
    preferences[i] = lpeople[i] 

  return preferences

def print_preferences(people):
  for p in people:
    print 'preferences for %(person)s' % { "person" : p.name }
    for key,value in p.partner_preferences.iteritems():
        print ('\t %(person)s, %(ranking)s' %
          { "person" : key, "ranking" : value })

def print_partnerships(matching_list):
  for pair in matching_list:
    print ('%(person)s is married to %(partner)s'
      % { "person" : pair[0], "partner" :  pair[1] })

def build_matching_list(people):
  matchingList = []
  for p in people:
    matchingList.append((p, p.partner))
  return matchingList
      

if __name__ == "__main__":
    verbose = len(sys.argv) > 1 and sys.argv[1] == "-v"

    males = []
    females = []
    number_of_people = random.randint(3, 6)

    #create people
    i = number_of_people
    while i > 0 :
      p = People.Man(MEN_NAMES[i])
      males.append(p)
      p = People.Woman(WOMAN_NAMES[i])
      females.append(p)
      i -= 1

    #assign preferences
    for male in males:
      male.partner_preferences = create_random_preferences(females)
    for female in females:
      female.partner_preferences = create_random_preferences(males)
      female.assign_rankings()
    if verbose:
      print_preferences(females)      
      print_preferences(males)      

    #Gale Shapley Stable Matching algorithm
    #Initially all m E M and w E W are free
    #While there is a man m who is free and hasn't proposed to every woman
    #Choose such a man m
    #Let W be the highest-ranked woman in m's preference list to whom m has not yet proposed
    #If W is free then
    #  (m, w) become engaged
    #Else w is currently engaged to m'
    #  If w prefers m' to m then
    #    m remains free
    #  Else w prefers m to mt
    #    (m, w) become engaged
    #  mt becomes free
    #  Endif
    #Endif
    #Endwhile
    #Return the set S of engaged pairs

    free_males = males 
    while len(free_males) > 0:
      man = free_males[0]
      woman = man.partner_preferences[man.preference_index]
      if verbose : print '%(man)s proposes to %(woman)s ' % {"man":man.name, "woman": woman.name}
      #low rank number indicates high preference
      if woman.partner==None or woman.ranking[man]<woman.ranking[woman.partner]:
        if woman.partner != None:
          ex = woman.partner
          ex.partner = None
          free_males.append(ex)
          action = ('%(woman)s is engaged to %(ex)s, but accepts %(man)s proposal' % 
            {"man":man.name, "woman": woman.name, "ex": ex.name })
        else: 
          action = ('%(woman)s is not engaged, so accepts %(man)s proposal ' % 
            {"man":man.name, "woman": woman.name})
        woman.partner = man
        man.partner = woman
        free_males.remove(man)
      else:
        action =  ('%(woman)s turns down %(man)s proposal (she likes %(partner)s more)'  % 
          {"man":man.name, "woman": woman.name, "partner": woman.partner })
      if verbose: print '\t %(action)s' % { "action": action }
      man.preference_index += 1

    matching_list = build_matching_list(females)

    if verbose: print_partnerships(matching_list)
